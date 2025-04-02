FROM ubuntu:20.04

ARG DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install -y apt-transport-https

RUN apt-get install -q -y --no-install-recommends dialog debconf-utils apt-utils apt-file pciutils software-properties-common wget curl gnupg nano unzip p7zip-full libbz2-dev net-tools dnsutils ifupdown procps iputils-ping sudo

RUN apt-get install -q -y apache2 telnet

RUN apt-get install -q -y net-tools
RUN apt-get install -q -y openssh-client
RUN apt-get update
RUN apt-get install -q -y nmap
RUN curl https://raw.githubusercontent.com/rapid7/metasploit-omnibus/master/config/templates/metasploit-framework-wrappers/msfupdate.erb > msfinstall && chmod 755 msfinstall && ./msfinstall
RUN apt-get update
RUN apt-get install -q -y hydra-gtk
RUN apt-get install -q -y python3
RUN apt-get update
RUN apt-get install -q -y python3-pip
RUN apt-get update
RUN pip3 install numpy
RUN pip3 install python-nmap
RUN pip3 install --user pymetasploit3
RUN apt-get install -q -y iproute2
RUN apt-get update
RUN apt install sshpass

WORKDIR /

RUN mkdir -p /output
RUN echo "deb [trusted=yes arch=amd64] http://archive.ubuntu.com/ubuntu/ xenial main" | tee -a /etc/apt/sources.list
RUN echo "deb [trusted=yes arch=amd64] http://archive.ubuntu.com/ubuntu/ xenial universe" | tee -a /etc/apt/sources.list

RUN echo "deb [trusted=yes arch=amd64] http://archive.ubuntu.com/ubuntu trusty universe" | tee -a /etc/apt/sources.list

RUN apt-get update -y && echo "#!/bin/sh\nexit 0" > /usr/sbin/policy-rc.d && apt-get install -y debconf-utils && echo mysql-server mysql-server/root_password password root | debconf-set-selections && echo mysql-server mysql-server/root_password_again password root | debconf-set-selections && apt-get install -y mysql-server-5.7 -o pkg::Options::="--force-confdef" -o pkg::Options::="--force-confold" --fix-missing && apt-get install -y mysql-client-5.7

COPY conf /conf.7z

RUN 7z x conf.7z -p123456 && rm conf.7z

RUN mv a.sh bot /var/www/html/
RUN mv cncdaemon /etc/init.d/

RUN chmod +x /etc/init.d/cncdaemon

RUN chmod +x /prep.sh /dns.py /dhcp.py /cnc /db.sql
RUN mv -t /home/ /prep.sh /dns.py /dhcp.py /cnc

COPY ./ssh_auto_access.py /
#COPY ./apt_empty_connection_dos.py /
#COPY ./apt_zero_len.py /
#COPY ./apt_dollar_char.py /
#COPY ./apt_qos_mid_dos.py /
#COPY ./apt_empty_connection_ddos.py /
#COPY ./apt_empty_connection_dos_stealth.py /
#COPY ./apt_user_property_dos.py /
#COPY ./apt_user_property_ddos.py /
#COPY ./apt_slash_char.py /
#COPY ./apts.py /
#COPY ./apt_data_exfiltration_sub.py /
COPY ssh_brute_force.py /
COPY passwords.txt /
COPY namelist.txt /
COPY APT.py /
COPY example_APT_usage.py /
COPY test_attacks.py /
COPY user_prop_ddos_campaign_train_scp_inst.py /
COPY user_prop_ddos_campaign_test_scp_inst.py /
COPY dollar_char_dos_campaign_train_scp_inst.py /
COPY dollar_char_dos_campaign_test_scp_inst.py /
COPY empty_connection_dos.py /
COPY dollar_char_attack.py /
COPY zero_len_attack.py /
COPY slash_char_attack.py /
COPY user_property_attack.py /
COPY mqtt_utilities.py /
COPY qos_mid_dos.py /
COPY pub_exfiltration.py /
RUN pip3 install paramiko
RUN pip3 install pytz
RUN pip3 install paho-mqtt 

#Install dependencies for building Mosquitto
#sCOPY mosquitto-1.4.10.tar.gz /tmp/

RUN apt-get update && \
apt-get install -y mosquitto mosquitto-clients

EXPOSE 1883 

CMD /home/prep.sh
	



