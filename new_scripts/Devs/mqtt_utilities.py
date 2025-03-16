import time
import sys
import socket
import random
import subprocess


class Connection_status:
    def __init__(self) -> None:
        self.connected = False


broker = "10.0.0.1"
port = 1883

TOPIC_MAP = {
    "10.0.0.20": [
        "Building1/SolarPower/Voltage", "Building1/Floor1/Flame_Sensor", "Building1/Floor1/Gas_Sensor",
        "Building1/Floor1/Smoke_Sensor", "Building1/Floor1/Temperature_Humidity", "Building1/Garage/Sound_Sensor",
        "Building1/Outside/BMP_Sensor", "Building1/Outside/Light", "Building1/Outside/Motion",
        "Building1/Tank/Water_Level", "Building1/Window/Vibration_Sensor"
    ],
    "10.0.0.21": [
        "Building2/Floor1/Flame_Sensor", "Building2/Floor1/Gas_Sensor", "Building2/Floor1/Smoke_Sensor",
        "Building2/Floor1/Temperature_Humidity", "Building2/Garage/Sound_Sensor", "Building2/Outside/BMP_Sensor",
        "Building2/Outside/Light", "Building2/Outside/Motion", "Building2/SolarPower/Voltage",
        "Building2/Tank/Water_Level", "Building2/Window/Vibration_Sensor"
    ],
    "10.0.0.22": [
        "Building3/Floor1/Flame_Sensor", "Building3/Floor1/Gas_Sensor", "Building3/Floor1/Smoke_Sensor",
        "Building3/Floor1/Temperature_Humidity", "Building3/Garage/Sound_Sensor", "Building3/Outside/BMP_Sensor",
        "Building3/Outside/Light", "Building3/Outside/Motion", "Building3/SolarPower/Voltage",
        "Building3/Tank/Water_Level", "Building3/Window/Vibration_Sensor", "Building3/Door/Touch_Sensor"
    ],
    "10.0.0.23": [
        "Building4/Floor1/Flame_Sensor", "Building4/Floor1/Gas_Sensor", "Building4/Floor1/Smoke_Sensor",
        "Building4/Floor1/Temperature_Humidity", "Building4/Garage/Sound_Sensor", "Building4/Outside/BMP_Sensor",
        "Building4/Outside/Light", "Building4/Outside/Motion", "Building4/SolarPower/Voltage",
        "Building4/Tank/Water_Level", "Building4/Window/Vibration_Sensor", "Building4/Door/Touch_Sensor"
    ]
}


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
        userdata["connection"].connected = True
    else:
        print("Connection failed.\tReason code: " +
              str(reason_code), flush=True)
        userdata["connection"].connected = False


def on_disconnect(client, userdata, flags, reason_code, properties):
    userdata["connection"].connected = False
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


def get_ip():
    """Retrieves the system's IP address in the 10.0.0.x range."""
    try:
        result = subprocess.check_output(["ip", "-4", "addr"], text=True)
        lines = result.splitlines()
        for line in lines:
            if "inet" in line:
                parts = line.strip().split()
                ip_with_mask = parts[1]  # e.g., "192.168.1.100/24"
                ip = ip_with_mask.split('/')[0]
                if ip.startswith("10.0.0."):
                    return ip
    except Exception as e:
        print(f"Error retrieving IP address: {e}")
    return None


def get_accessible_topics(username: str) -> list[str]:
    if username == 'root':
        return TOPIC_MAP.values()
    elif username == 'client1':
        return TOPIC_MAP['10.0.0.20']
    elif username == 'client2':
        return TOPIC_MAP['10.0.0.21']
    elif username == 'client3':
        return TOPIC_MAP['10.0.0.22']
    elif username == 'client4':
        return TOPIC_MAP['10.0.0.23']
