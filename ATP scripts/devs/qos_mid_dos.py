from scapy.layers.inet import *
from scapy.all import *
from scapy.contrib.mqtt import MQTT, MQTTConnect, MQTTConnack, MQTTPublish, MQTTPubrec, MQTTDisconnect
import mqtt_utilities as util
import time

local_ip = util.get_local_ip()
broker_ip = "10.0.0.1"
port = 1883
username = b"client1"
password = b"pass1"
keep_alive = 120
protocol_name = b"MQTT"
client_id = b"my_client1_id"
duration = 10 #random.randint(5, 30)
start_time = time.time()

connect_packet = IP(dst=broker_ip, src=local_ip) / \
    TCP(dport=port, sport=RandShort(), flags='S')/MQTTConnect(
    protoname=protocol_name,
    protolevel=5,
    usernameflag=1,
    passwordflag=1,
    cleansess=1,
    klive=keep_alive,
    clientIdlen=len(client_id),
    clientId=client_id,
    userlen=len(username),
    username=username,
    passlen=len(password),
    password=password)
    
    
while True:
    elapsed_time = time.time() - start_time
    print(elapsed_time)
    if elapsed_time >= duration:
        print("time elapsed")
        break   
    answer = sr1(connect_packet)
    if answer:
        if answer.haslayer(MQTTConnack):
            if answer.getlayer(MQTTConnack).retcode == 0:
                print("Connected successfully.\tReason code: " + str(answer.getlayer(MQTTConnack).retcode))
            else:
                print("Connection failed.\tReason code: " + str(answer.getlayer(MQTTConnack).retcode))
        else:
            print("Unexpected reply form broker.")
    else:
        print("Broker did not answer.")

    disconnect_packet = IP(dst=broker_ip, src=local_ip) / \
    TCP(dport=port, sport=RandShort(), flags='F')/MQTTDisconnect()
    send(disconnect_packet)
    print("Connection closed")
