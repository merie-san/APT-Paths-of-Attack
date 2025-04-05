import time
import sys
import socket
import subprocess
from typing import List, Optional

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
        print(f"Broker received the message with mid {mid}.\tReason code: {reason_code}", flush=True)
    else:
        print(f"Broker didn't receive the message with mid {mid}.\tReason code: {reason_code}", flush=True)


def on_connect(client, userdata, flags, reason_code, properties):
    if reason_code == 0:
        print(f"Connected successfully.\tReason code: {reason_code}\tSession present: {flags.session_present}",
              flush=True)
    else:
        print(f"Connection failed.\tReason code: {reason_code}", flush=True)


def on_disconnect(client, userdata, flags, reason_code, properties):
    if reason_code == 0:
        print("Disconnected correctly from broker")
    else:
        print("Disconnected due to unexpected errors")


def connect_client_v3(client, reconnection_delay=5, timeout=300):
    start_time = time.time()
    while True:
        try:
            print(f"Attempting to connect to {broker}:{port}...", flush=True)
            client.connect(broker, port)
            print("successfully connected to the broker", flush=True)
            client.loop_start()
            return True
        except (socket.error, Exception) as e:
            print(f"Failed to connect to the broker, exception: {e}", flush=True)
        time_elapsed = time.time() - start_time
        if time_elapsed >= timeout:
            print("Timed out" + str(time_elapsed), flush=True)
            return False
        else:
            print(
                f"Retrying connection in {reconnection_delay} seconds...", flush=True)
            time.sleep(reconnection_delay)


def connect_client(client, input_clean_start=3, input_properties=None, reconnection_delay=5, timeout=300):
    start_time = time.time()
    while True:
        try:
            print(f"Attempting to connect to {broker}:{port}...", flush=True)
            client.connect(broker, port, clean_start=input_clean_start,
                           properties=input_properties)
            print("successfully connected to the broker")
            client.loop_start()
            return True
        except (socket.error, Exception) as e:
            print(
                f"Failed to connect to the broker, exception: {e}", flush=True)
        time_elapsed = time.time() - start_time
        if time_elapsed >= timeout:
            print("Timed out" + str(time_elapsed), flush=True)
            return False
        else:
            print(
                f"Retrying connection in {reconnection_delay} seconds...", flush=True)
            time.sleep(reconnection_delay)


def on_subscribe(client, userdata, mid, reason_code_list, properties):
    if reason_code_list[0].is_failure:
        print(
            f"Broker rejected your subscription request with mid {mid}, reason code: {reason_code_list[0]}", flush=True)
    else:
        print(
            f"Broker accepted your subscription request with mid {mid}, granting it a qos of {reason_code_list[0].value}",
            flush=True)


def on_unsubscribe(client, userdata, mid, reason_code_list, properties):
    if len(reason_code_list) == 0 or not reason_code_list[0].is_failure:
        print(f"unsubscribe request with mid {mid} succeeded", flush=True)
    else:
        print(
            f"Broker replied with failure to the unsubscribe request with mid {mid}, reason code: {reason_code_list[0]}",
            flush=True)


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


def get_accessible_topics(username: str) -> Optional[List[str]]:
    if username == 'root':
        result = []
        for value in TOPIC_MAP.values():
            result += value
        return result
    elif username == 'client1':
        return TOPIC_MAP['10.0.0.20']
    elif username == 'client2':
        return TOPIC_MAP['10.0.0.21']
    elif username == 'client3':
        return TOPIC_MAP['10.0.0.22']
    elif username == 'client4':
        return TOPIC_MAP['10.0.0.23']
    else:
        return None
