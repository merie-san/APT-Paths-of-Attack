import time
import sys
import socket
import random


class Connection_status:
    def __init__(self) -> None:
        self.connected = False


broker = "10.0.0.1"
port = 1883


def on_publish(client, userdata, mid, reason_code, properties):
    if reason_code == 0:
        print("Broker received the message.\tReason code: " +
              str(reason_code), flush=True)
    else:
        print("Broker didn't receive the message.\tReason code: " +
              str(reason_code), flush=True)


def on_connect(client, userdata, flags, reason_code, properties):
    if reason_code == 0:
        print("Connected successfully.\tReason code: " +
              str(reason_code) + "\tSession present: " + str(flags.session_present), flush=True)
        userdata.connected = True
    else:
        print("Connection failed.\tReason code: " +
              str(reason_code), flush=True)
        userdata.connected = False


def on_disconnect(client, userdata, flags, reason_code, properties):
    userdata.connected = False
    if reason_code == 0:
        print("Disconnected from broker")
    else:
        print("Disconnected due to unexpected errors")


def connect_client(client, connection, reconnect_delay, input_clean_start=3, input_properties=None):
    start_time = time.time()
    while True:
        try:
            print(f"Attempting to connect to {broker}:{port}...", flush=True)
            client.connect(broker, port, clean_start=input_clean_start,
                           properties=input_properties)
            client.loop_start()
            while not connection.connected:
                time.sleep(2)
                time_elapsed = time.time() - start_time
                print("Time waited: " + str(time_elapsed), flush=True)
                if time_elapsed >= 20:
                    client.loop_stop()
                    print("Failed to connect due to broker's refusal", flush=True)
                    return False
            else:
                print("Connected to broker")
                return True
        except (socket.error, Exception) as e:
            print(
                f"Failed to connect to the broker: {e}", file=sys.stderr, flush=True)
            time_elapsed = time.time() - start_time
            if time_elapsed >= 20:
                print("Timed out", flush=True)
                return False
            else:
                print(
                    f"Retrying connection in {reconnect_delay} seconds...", flush=True)
                time.sleep(reconnect_delay)


def spam_messages(client, topic, span=2, prefix="spam", fixed_span=False, ip_address="", qos=0):
    interval = span
    while True:
        try:
            message = f"{prefix.title()} at {time.strftime('%Y-%m-%d %H:%M:%S')} from {ip_address}"
            client.publish(topic, message, qos=qos)
            print(f"Sent: {message}", flush=True)
            if not fixed_span:
                interval = random.random() * span
            time.sleep(interval)
        except socket.error as e:
            print(
                f"Network error occurred while publishing on {ip_address}: {e}", file=sys.stderr)
            client.disconnect()
            return
        except Exception as e:
            print(
                f"Unexpected error occurred while publishing on {ip_address}: {e}", file=sys.stderr)
            client.disconnect()
            return


def on_subscribe(client, userdata, mid, reason_code_list, properties):
    if reason_code_list[0].is_failure:
        print(
            f"Broker rejected your subscription: {reason_code_list[0]}", flush=True)
    else:
        print(
            f"Broker granted the following QoS to your subscription request: {reason_code_list[0].value}", flush=True)


def on_unsubscribe(client, userdata, mid, reason_code_list, properties):
    if len(reason_code_list) == 0 or not reason_code_list[0].is_failure:
        print("unsubscribe succeeded", flush=True)
    else:
        print(
            f"Broker replied with failure: {reason_code_list[0]}", flush=True)
    client.disconnect()


def get_local_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    not_connected = True
    while not_connected:
        try:
            s.connect(('10.0.0.0', 0))
            not_connected = False
        except socket.error as e:
            time.sleep(10)
    return s.getsockname()[0]
