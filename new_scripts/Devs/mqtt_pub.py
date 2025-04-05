import time
import sys
import paho.mqtt.client as mqtt
import subprocess
import zipfile
import json


# MQTT Broker Details
BROKER_HOST = "10.0.0.1"
BROKER_PORT = 1883
USERNAME = "root"
PASSWORD = "root"
RECONNECT_DELAY = 10  # Delay in seconds between reconnection attempts


def get_system_ips():
    """
    Retrieves all IP addresses of the current system.
    """
    system_ips = []
    # Use `ip` command to list IPs (Linux example)
    try:
        result = subprocess.check_output(["ip", "-4", "addr"], text=True)
        lines = result.splitlines()
        for line in lines:
            if "inet" in line:
                parts = line.strip().split()
                ip_with_mask = parts[1]  # e.g., "192.168.1.100/24"
                ip = ip_with_mask.split('/')[0]
                system_ips.append(ip)
        ip = [ip for ip in system_ips if ip.startswith("10.0.0")]
    except Exception as e:
        print(f"Error retrieving IP addresses: {e}")
        
    ip_map = {
        "10.0.0.4" : "192.168.60.100",
        "10.0.0.5" : "192.168.60.101",
        "10.0.0.6" : "192.168.60.102",
        "10.0.0.7" : "192.168.60.103",
        "10.0.0.8" : "192.168.60.104",
        "10.0.0.9" : "192.168.60.105",
        "10.0.0.10" : "192.168.60.106",
        "10.0.0.11" : "192.168.60.107",
        "10.0.0.12" : "192.168.70.100",
        "10.0.0.13" : "192.168.70.101",
        "10.0.0.14" : "192.168.70.102",
        "10.0.0.15" : "192.168.70.103",
        "10.0.0.16" : "192.168.70.104",
        "10.0.0.17" : "192.168.70.105",
        "10.0.0.18" : "192.168.70.106",
        "10.0.0.19" : "192.168.70.107",
    }
    print(ip)
    ip = ip_map[ip[0]]
        
    return ip

def get_packets(ip):
    path = "./refined_pcaps"
    pkt_map = {
        "192.168.60.100" : "pub_pkts_192.168.60.100_file",
        "192.168.60.101" : "pub_pkts_192.168.60.101_file",
        "192.168.60.102" : "pub_pkts_192.168.60.102_file",
        "192.168.60.103" : "pub_pkts_192.168.60.103_file",
        "192.168.60.104" : "pub_pkts_192.168.60.104_file",
        "192.168.60.105" : "pub_pkts_192.168.60.105_file",
        "192.168.60.106" : "pub_pkts_192.168.60.106_file",
        "192.168.60.107" : "pub_pkts_192.168.60.107_file",
        "192.168.70.100" : "pub_pkts_192.168.70.100_file",
        "192.168.70.101" : "pub_pkts_192.168.70.101_file",
        "192.168.70.102" : "pub_pkts_192.168.70.102_file",
        "192.168.70.103" : "pub_pkts_192.168.70.103_file",
        "192.168.70.104" : "pub_pkts_192.168.70.104_file",
        "192.168.70.105" : "pub_pkts_192.168.70.105_file",
        "192.168.70.106" : "pub_pkts_192.168.70.106_file",
        "192.168.70.107" : "pub_pkts_192.168.70.107_file",
    }
    return pkt_map[ip]


def extract_subfolder_from_zip(zip_path, subfolder, extract_to):
    """
    Extract a specific subfolder from a ZIP archive.

    Args:
        zip_path (str): Path to the ZIP file.
        subfolder (str): The subfolder to extract (e.g., "my_subfolder/").
        extract_to (str): Path to extract the subfolder to.
    """
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        print(zip_ref.namelist())
        # List all files in the archive
        all_files = zip_ref.namelist()
        print(subfolder)
        # Filter files that belong to the specific subfolder
        for f in all_files:
           if f == subfolder:
               zip_ref.extract(f, extract_to)       

    print(f"Subfolder '{subfolder}' extracted to '{extract_to}'.")


def setup_client():
    """
    Setup and configure the MQTT client.
    """
    client = mqtt.Client(protocol=mqtt.MQTTv311)
    client.username_pw_set(USERNAME, PASSWORD)
    return client

def on_disconnect(client, userdata, rc):
    """
    Handle the disconnect event from the broker.
    """
    print(f"Disconnected with result code {rc}")

def main():
    time.sleep(60)
    machine_ip = get_system_ips()
    print(machine_ip)
    pkt_path = get_packets(machine_ip)
    print(pkt_path)
    
    zip_path = "/refined_pcaps.zip"
    extract_to = "./extracted"
    extract_subfolder_from_zip(zip_path, pkt_path, extract_to)
    
    with open("./extracted/"+ pkt_path, 'r') as f:
        mqtt_publish_packets_with_timing = json.load(f)
    
    if not mqtt_publish_packets_with_timing:
        print("No MQTT Publish packets found in the PCAP.")
        return

    # Setup the MQTT client
    client = setup_client()
    client.on_disconnect = on_disconnect  # Set the disconnect callback

    # Attempt to connect to the broker
    while True:
        try:
            client.connect(BROKER_HOST, BROKER_PORT, keepalive=60)
            print("Connected to MQTT broker.")
            break
        except Exception as e:
            print(f"Connection failed: {e}. Retrying in {RECONNECT_DELAY} seconds...")
            time.sleep(RECONNECT_DELAY)

    # Start the network loop in the background
    client.loop_start()

    # Start sending messages with the same timing
    last_timestamp = 1622780901.495940
    #last_timestamp = 1622871083.894820  # Example timestamp
    for packet in mqtt_publish_packets_with_timing:
        try:
            # Maintain original timing by computing the delay
            if last_timestamp is not None:
                delay = packet["timestamp"] - last_timestamp
                print(f"Delay: {delay}")
                time.sleep(max(0, delay))  # Ensure non-negative delay

            topic = packet["topic"]
            payload = packet["payload"]
            qos = packet["qos"]
            retain = packet["retain"]
            
            #properties = Properties(PacketTypes.PUBLISH)
            #properties.MessageExpiryInterval = 120
            
            print(f"Publishing to topic '{topic}' with QoS {qos}, retain={retain}.")
            print(f"Payload: {payload}")

            if client.is_connected():
                client.publish(topic, str(payload), qos=qos, retain=retain) #properties=properties)
            else:
                print("Client disconnected, skipping publish.")

            last_timestamp = packet["timestamp"]  # Update the last processed timestamp
        except Exception as e:
            print(f"Error publishing message: {e}")

    # Disconnect the client after all messages are published
    client.disconnect()
    print("All messages published and client disconnected.")

    # Stop the network loop
    client.loop_stop()
    print("Exiting program.")
    sys.exit(0)


if __name__ == "__main__":
    main()
