import paho.mqtt.client as mqtt
import mqtt_utilities as util
import time

broker = "10.0.0.1"
port = 1883
subscribe_topic = "test/topic1"
s_username = "client1"
s_password = "pass1"
local_ip_address = util.get_local_ip()
targeted_ip_addresses = ["10.0.0.7"]
reconnect_delay = 10
connection = util.Connection_status()


def on_message(client, userdata, message):
    r_message = message.payload.decode('utf-8')
    print(f"Received message: " + r_message, flush=True)
    with open("mqtt_sub_log.txt", 'a') as log:
        log.write("Falsified activity\n")


if local_ip_address in targeted_ip_addresses:
    while True:
        client = mqtt.Client(
            mqtt.CallbackAPIVersion.VERSION2, userdata=connection, protocol=mqtt.MQTTv5)
        client.username_pw_set(s_username, s_password)
        client.on_connect = util.on_connect
        client.on_subscribe = util.on_subscribe
        client.on_unsubscribe = util.on_unsubscribe
        client.on_message = on_message
        client.on_disconnect = util.on_disconnect
        if util.connect_client(client, connection, reconnect_delay):
            client.subscribe(subscribe_topic)
            print("beginning to falsify activity")
            time.sleep(1000)
            client.unsubscribe(subscribe_topic)
            client.disconnect()
            break
        else:
            print(f"Retrying connection in {reconnect_delay} seconds...")
            time.sleep(reconnect_delay)
else:
    print("This machine wasn't targeted in the attack")