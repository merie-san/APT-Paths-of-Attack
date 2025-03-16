#!/usr/bin/env bash

touch /etc/mosquitto/mosqu
chmod 644 /etc/mosquitto/mosquitto.conf

#mosquitto_passwd -b /etc/mosquitto/mosquitto.passwd client1 pass1
#mosquitto_passwd -b /etc/mosquitto/mosquitto.passwd client2 pass2
#mosquitto_passwd -b /etc/mosquitto/mosquitto.passwd # whatever
printf 'pass123\npass123\n' | mosquitto_ctrl dynsec init /var/lib/mosquitto/dynamic-security.json myadmin
chown mosquitto:mosquitto /var/lib/mosquitto/dynamic-security.json
chmod 775 /var/lib/mosquitto/dynamic-security.json
mosquitto -c /etc/mosquitto/mosquitto.conf &
sleep 2
mosquitto_ctrl -u myadmin -P pass123 dynsec createRole roleRoot
mosquitto_ctrl -u myadmin -P pass123 dynsec createRole roleClient1
mosquitto_ctrl -u myadmin -P pass123 dynsec createRole roleClient2
mosquitto_ctrl -u myadmin -P pass123 dynsec createRole roleClient3
mosquitto_ctrl -u myadmin -P pass123 dynsec createRole roleClient4

mosquitto_ctrl -u myadmin -P pass123 dynsec createRole roleDollarExploit

mosquitto_ctrl -u myadmin -P pass123 dynsec addRoleACL roleRoot publishClientSend \# allow
mosquitto_ctrl -u myadmin -P pass123 dynsec addRoleACL roleRoot subscribePattern \# allow

mosquitto_ctrl -u myadmin -P pass123 dynsec addRoleACL roleClient1 publishClientSend Building1/\# allow
mosquitto_ctrl -u myadmin -P pass123 dynsec addRoleACL roleClient1 subscribePattern Building1/\# allow

mosquitto_ctrl -u myadmin -P pass123 dynsec addRoleACL roleClient2 publishClientSend Building2/\# allow
mosquitto_ctrl -u myadmin -P pass123 dynsec addRoleACL roleClient2 subscribePattern Building2/\# allow

mosquitto_ctrl -u myadmin -P pass123 dynsec addRoleACL roleClient3 publishClientSend Building3/\# allow
mosquitto_ctrl -u myadmin -P pass123 dynsec addRoleACL roleClient3 subscribePattern Building3/\# allow

mosquitto_ctrl -u myadmin -P pass123 dynsec addRoleACL roleClient4 publishClientSend Building4/\# allow
mosquitto_ctrl -u myadmin -P pass123 dynsec addRoleACL roleClient4 subscribePattern Building4/\# allow

printf 'root\nroot\n' | mosquitto_ctrl -u myadmin -P pass123 dynsec createClient root
printf 'pass1\npass1\n' | mosquitto_ctrl -u myadmin -P pass123 dynsec createClient client1
printf 'pass2\npass2\n' | mosquitto_ctrl -u myadmin -P pass123 dynsec createClient client2
printf 'pass3\npass3\n' | mosquitto_ctrl -u myadmin -P pass123 dynsec createClient client3
printf 'pass4\npass4\n' | mosquitto_ctrl -u myadmin -P pass123 dynsec createClient client4

mosquitto_ctrl -u myadmin -P pass123 dynsec addClientRole root roleRoot
mosquitto_ctrl -u myadmin -P pass123 dynsec addClientRole client1 roleClient1
mosquitto_ctrl -u myadmin -P pass123 dynsec addClientRole client2 roleClient2
mosquitto_ctrl -u myadmin -P pass123 dynsec addClientRole client3 roleClient3
mosquitto_ctrl -u myadmin -P pass123 dynsec addClientRole client4 roleClient4

mosquitto_ctrl -u myadmin -P pass123 dynsec addRoleACL roleDollarExploit publishClientSend \$test/test allow
mosquitto_ctrl -u myadmin -P pass123 dynsec addClientRole client1 roleDollarExploit

mosquitto_ctrl -u myadmin -P pass123 dynsec setDefaultACLAccess subscribe deny
mosquitto_ctrl -u myadmin -P pass123 dynsec setDefaultACLAccess unsubscribe allow
mosquitto_ctrl -u myadmin -P pass123 dynsec setDefaultACLAccess publishClientSend deny
mosquitto_ctrl -u myadmin -P pass123 dynsec setDefaultACLAccess publishClientReceive allow
# loop until we have IP
while true;
do
  IPPre=$(ifconfig eth0 | grep 'inet ' | cut -d: -f2 | awk '{ print $2}' | cut -f1 -d.)
  if [ -z "$IPPre" ]
  then
        sleep 2
  else
        if [ "$IPPre" -eq 10 ]; then break ; fi
        sleep 2
  fi
done

nginx -g "daemon off;" &

IP=$(ifconfig eth0 | grep 'inet ' | cut -d: -f2 | awk '{ print $2}') && ./ftp_server.py "$IP" &

service apache2 start
service apache2 start

while true;
do
  SEC=$((10 + RANDOM % 20))
  sleep $SEC;
done
