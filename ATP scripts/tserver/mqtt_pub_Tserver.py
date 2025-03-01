import paho.mqtt.client as mqtt
import time
import mqtt_utilities as util

# Define the MQTT broker details
port = 1883
topic = "test/topic2"
username = "client2"
password = "pass2"

# Get the local Ip address
local_ip_address = util.get_local_ip()

publish_interval = 3  # Interval between messages in seconds
reconnect_delay = 5
connection = util.Connection_status()

# Create a new MQTT client instance
client = mqtt.Client(
    mqtt.CallbackAPIVersion.VERSION2, userdata=connection, protocol=mqtt.MQTTv5)

# Set the username and password
client.username_pw_set(username, password)
client.on_disconnect = util.on_disconnect
client.on_connect = util.on_connect
client.on_publish = util.on_publish


# Publish messages periodically
try:
    while True:
        if util.connect_client(client, connection, reconnect_delay):
            print("Beginning to send messages", flush=True)
            util.spam_messages(client, topic, span=publish_interval,
                               prefix="message", fixed_span=True, ip_adress=local_ip_address)
        else:
            print(f"Retrying connection in {reconnect_delay} seconds...")
            time.sleep(reconnect_delay)
except KeyboardInterrupt:
    print("Publisher stopped.", flush=True)
    client.disconnect()
