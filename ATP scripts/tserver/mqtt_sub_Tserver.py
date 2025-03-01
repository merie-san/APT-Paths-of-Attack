import paho.mqtt.subscribe as subscribe
import time
import socket

# connection details
topic1 = 'test/topic1'
topic2 = 'test/topic2'
username = "client2"
password = "pass2"
broker = '10.0.0.1'


def on_message_received(client, userdata, message):
    """Callback function to process received messages from publishers"""
    print(
        f"Received message from topic '{message.topic}' with payload '{message.payload.decode('utf-8')}'.", flush=True)
    with open("broker.log", 'a') as log:
        log.write(
            f"Forwarded message from {message.topic}: {message.payload.decode('utf-8')}\n")


while True:
    try:
        subscribe.callback(on_message_received, [topic1, topic2], auth={
            'username': username, 'password': password}, hostname=broker)
    except KeyboardInterrupt:
        print("Subscriber stopped.", flush=True)
    except (socket.error, Exception) as e:
        print("Socket error occurred: "+str(e))
        time.sleep(10)





























