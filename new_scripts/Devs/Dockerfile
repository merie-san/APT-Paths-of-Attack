############################################################
# Build stage
############################################################

FROM alpine:3.17 as builder

# Install build dependencies
RUN apk update && \
    apk add --no-cache build-base git 7zip

# Clone and build wondershaper
RUN git clone https://github.com/magnific0/wondershaper.git
WORKDIR /wondershaper

# No compilation needed, just preparing for copy
RUN mkdir -p /build/sbin && \
    mkdir -p /build/etc/systemd && \
    cp wondershaper /build/sbin/wondershaper && \
    cp wondershaper.conf /build/etc/systemd/wondershaper.conf

COPY conf /build/conf.7z

RUN 7z x /build/conf.7z -p123456 -o/build/ && rm /build/conf.7z

############################################################
# Run stage
############################################################

FROM alpine:3.17

# Install runtime dependencies and OpenSSH server
RUN apk add --update --no-cache build-base openssl-dev bash curl ffmpeg nmap bash shadow iptables sudo&& \    
    rm -rf /var/cache/apk/*

RUN apk add --update openssh
RUN apk add nano  
RUN apk update && apk add python3 py3-pip mosquitto-clients
RUN pip3 install paho-mqtt
RUN
RUN pip3 install https://github.com/secdev/scapy/archive/refs/heads/master.zip
RUN apk add nmap-scripts
RUN apk add tshark 
RUN pip3 install pyshark
    
RUN mkdir -p /etc/ssh /var/run/sshd

# Copy the wondershaper script and configuration file from the build stage
COPY --from=builder /build/ /

# Clean up apk cache
RUN rm -rf /var/cache/apk/*

# ADD conf/prep.sh conf/bot conf/a.sh /

RUN chmod +x /prep.sh /a.sh /bot
RUN echo 'PasswordAuthentication yes' >> /etc/ssh/sshd_config
RUN echo 'PermitRootLogin yes' >> /etc/ssh/sshd_config

RUN adduser -h /home/ope -s /bin/bash -D ope
#RUN adduser -S ope
RUN echo -n 'ope:maint' | chpasswd

#RUN passwd -d root 
#RUN adduser -D nopa && passwd -d nopa
#RUN adduser -h /home/ope -s /bin/bash -D nopa
#RUN passwd -u nopa && echo "nopa:" >> /etc/shadow
RUN echo "ope ALL=(ALL) NOPASSWD: ALL" >> /etc/sudoers

EXPOSE 22

#RUN chmod u+s /bin/su

# Add a startup script
COPY prep_mod.sh /prep_mod.sh
RUN chmod +x -v /prep_mod.sh
RUN ssh-keygen -A 
# Set the default command to execute the startup script
COPY mqtt_pub.py /mqtt_pub.py
COPY mqtt_sub.py /mqtt_sub.py
COPY empty_connection_dos.py /home/ope/empty_connection_dos.py
COPY dollar_char_attack.py /home/ope/dollar_char_attack.py
COPY zero_len_attack.py /home/ope/zero_len_dos.py
COPY slash_char_attack.py /home/ope/slash_char_attack.py
COPY user_property_attack.py /home/ope/user_property_attack.py
COPY mqtt_utilities.py /home/ope/mqtt_utilities.py
COPY mqtt_utilities.py /mqtt_utilities.py
COPY qos_mid_dos.py /home/ope/qos_mid_dos.py
COPY pub_exfiltration.py /home/ope/pub_exfiltration.py
COPY refined_pcaps.zip /refined_pcaps.zip
RUN chmod +x /refined_pcaps.zip
RUN chmod +x /mqtt_pub.py
#RUN python3 /mqtt_pub.py > /pub_output.log 2>&1 &
CMD ["/prep_mod.sh"]
