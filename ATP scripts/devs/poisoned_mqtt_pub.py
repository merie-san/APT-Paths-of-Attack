import paho.mqtt.client as mqtt
import time
import sys
import socket
import random
import mqtt_utilities as util


port = 1883
publish_topic = "test/topic1"
s_username = "client1"
s_password = "pass1"
local_ip_address = util.get_local_ip()
targeted_ip_addresses = ["10.0.0.7"]
reconnect_delay = 10
connection = util.Connection_status()


def setup_client(connection):
    client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2, userdata=connection, protocol=mqtt.MQTTv5)
    client.username_pw_set(s_username, s_password)
    client.on_connect = util.on_connect
    client.on_disconnect = util.on_disconnect
    client.on_publish = util.on_publish
    return client


if local_ip_address in targeted_ip_addresses:
    while True:
        client = setup_client(connection)
        if util.connect_client(client, connection, reconnect_delay):
            util.spam_messages(
                client, publish_topic, prefix="modified message", span=10, fixed_span=True, ip_address=local_ip_address)
        else:
            print(f"Retrying connection in {reconnect_delay} seconds...")
            time.sleep(reconnect_delay)
else:
    print("This machine wasn't targeted in the attack")
