network_statistics = "netstat -t;netstat -tuln"
socket_statistics = "ss -tuln;ss -tr;ss -ntr"
# nmap TCP SYN Scan
nmap_T3_C = "sudo nmap -sS -T3 -Pn 192.168.0.0/24"
nmap_T4_A = "sudo nmap -sS -T4 -Pn 10.0.0.0/24"
# cat commands
mqtt_cat_commands = "cat /etc/mosquitto/mosquitto.conf;cat /etc/mosquitto/conf.d;cat /var/lib/mosquitto/mosquitto.db;cat /var/log/mosquitto/mosquitto.log; cat /var/log/syslog;cat /var/log/syslog"
nmap_mqtt_commands = "sudo /usr/bin/nmap -sS -T2 -Pn -p 1883,8883 10.0.0.0/24"
nmap_banner_commands = "sudo nmap -sS -T3 -f -Pn -p 1883,8883 --script banner 10.0.0.0/24"
nmap_sub_commands = "sudo nmap -p 1883,8883 --script mqtt-subscribe 10.0.0.0/24"
