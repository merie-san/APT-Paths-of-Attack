import mqtt_utilities as util
import paho.mqtt.client as mqtt
import time
import socket
import random

username = "client1"
password = "pass1"
targeted_ip_address = "10.0.0.7"
reconnect_delay = 10
connection = util.Connection_status()
duration = 20 #random.randint(5, 30)
start_time = time.time()
end_of_exec=False

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
        while connection.connected:    
            client.publish("$test/topic", "whatever")
            elapsed_time = time.time() - start_time
            print("Execution time: " + str(elapsed_time))
            time.sleep(0.05 * random.randint(1, 2))
            if elapsed_time >= duration:
                print("Time elapsed")
                client.disconnect()
                end_of_exec=True
                break          
    else:
        elapsed_time = time.time() - start_time
        print("Execution time: " + str(elapsed_time))
        if elapsed_time >= duration:
            print("time elapsed")
            break
        print(f"Resetting client and retrying connection in {reconnect_delay} seconds...", flush=True)
        time.sleep(random.randint(1, 10))
