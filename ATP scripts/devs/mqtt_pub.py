import paho.mqtt.client as mqtt
import time
import mqtt_utilities as util
# Define MQTT broker details
publish_topic = "test/topic1"
username = "client1"
password = "pass1"

# Get the local Ip address
local_ip_address = util.get_local_ip()

publish_interval = 10
reconnect_delay = 10  # Delay between connection attempts
connection = util.Connection_status()

print("waiting", flush=True)
# time.sleep(120)
print("passed", flush=True)


def setup_client(connection):
    client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2, userdata=connection, protocol=mqtt.MQTTv5)
    client.username_pw_set(username, password)
    client.on_connect = util.on_connect
    client.on_disconnect = util.on_disconnect
    client.on_publish = util.on_publish
    return client


while True:
    client = setup_client(connection)
    if util.connect_client(client, connection, reconnect_delay):
        print("Beginning to send messages", flush=True)
        util.spam_messages(client, publish_topic, span=publish_interval,
                           prefix="message", fixed_span=True, ip_address=local_ip_address)
    else:
        print(
            f"Retrying connection in {reconnect_delay} seconds...", flush=True)
        time.sleep(reconnect_delay)
