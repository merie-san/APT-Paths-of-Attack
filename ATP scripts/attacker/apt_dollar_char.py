import pickle
import random
import pytz
import time
from datetime import datetime
import apts


# def initial_access(phase_number, pause):
#    start_time = datetime.now(tz=pytz.UTC)
#    commands = "netstat -t;netstat -tuln;ss -tuln;ss -tr;ss -ntr;sudo nmap -sS -T1 -Pn 192.168.1.0/24;sudo nmap -sS -T1  -Pn 192.168.0.0/24;sudo nmap  -sS -T1 -Pn 10.0.0.0/24"
#    commands_list = commands.split(';')
#    ssh.ssh_commands(target, "ope", "maint", commands_list, 1, 5, "./out.log", 9999)
#    end_time = datetime.now(tz=pytz.UTC)
#    experiment = {
#        "phase_number": phase_number,
#        "attack_name": "empty_connection_dos",
#        "phase_name": "network_discovery",
#        "start_time": start_time,
#        "end_time": end_time
#    }
#    time.sleep(pause)

#    return experiment


# def mqtt_discovery(phase_number, pause):
#    start_time = datetime.now(tz=pytz.UTC)
#    commands = "cat /etc/mosquitto/mosquitto.conf;cat /etc/mosquitto/conf.d;cat /var/lib/mosquitto/mosquitto.db;cat /var/log/mosquitto/mosquitto.log; cat /var/log/syslog;cat /var/log/syslog;sudo /usr/bin/nmap -sS -T1 -Pn -p 1883,8883 10.0.0.0/24;sleep 20;sudo nmap -sS -T1 -f -Pn -p 1883,8883 --script banner 10.0.0.0/24;sudo nmap -p 1883,8883 --script mqtt-subscribe 10.0.0.0/24"
#    commands_list = commands.split(';')
#    ssh.ssh_commands(target, "ope", "maint", commands_list, 1, 5, "./out1.log", 6666)
#    end_time = datetime.now(tz=pytz.UTC)
#    experiment = {
#        "phase_number": phase_number,
#        "attack_name": "empty_connection_dos",
#        "phase_name": "mqtt_discovery",
#        "start_time": start_time,
#        "end_time": end_time
#    }
#    time.sleep(pause)
#    return experiment


def main():
    experiments_details = []
    target = "10.0.0.7"
    attack_name = "dollar_char"
    start_time_all = datetime.now(tz=pytz.UTC)

    # 1) INITIAL ACCESS
    # ----------------------------------------------------------------------------------------------
    commands = "netstat -t;netstat -tuln;ss -tuln;ss -tr;ss -ntr;sudo nmap -sS -T1 -Pn 192.168.1.0/24;sudo nmap -sS -T1  -Pn 192.168.0.0/24;sudo nmap  -sS -T1 -Pn 10.0.0.0/24"
    command_list = commands.split(";")
    experiment = apts.initial_access(target, 1.0, command_list, attack_name, pause_commands=True,
                                     sup_conclusion_pause=60)
    experiments_details.append(experiment)
    time.sleep(random.randint(0, 180))

    # 1) INITIAL ACCESS
    # ----------------------------------------------------------------------------------------------
    experiment = apts.initial_access(target, 1.1, command_list, attack_name, sup_conclusion_pause=60)
    experiments_details.append(experiment)
    time.sleep(random.randint(0, 120))

    # 1opt) SSH BRUTEFORCE
    # ----------------------------------------------------------------------------------------------
    experiment = apts.brute_force(2.0, attack_name, 30)
    experiments_details.append(experiment)
    time.sleep(random.randint(0, 120))

    # 1opt) SSH BRUTEFORCE
    # ----------------------------------------------------------------------------------------------
    experiment = apts.brute_force(2.1, attack_name, 30)
    experiments_details.append(experiment)

    # 2) MQTT DISCOVERY
    # ---------------------------------------------------------------------------------------------
    commands2 = "cat /etc/mosquitto/mosquitto.conf;cat /etc/mosquitto/conf.d;cat /var/lib/mosquitto/mosquitto.db;cat /var/log/mosquitto/mosquitto.log; cat /var/log/syslog;cat /var/log/syslog;sudo /usr/bin/nmap -sS -T1 -Pn -p 1883,8883 10.0.0.0/24;sleep 20;sudo nmap -sS -T1 -f -Pn -p 1883,8883 --script banner 10.0.0.0/24;sudo nmap -p 1883,8883 --script mqtt-subscribe 10.0.0.0/24"
    command_list2 = commands2.split(";")
    experiment = apts.mqtt_discovery(target, 3, command_list2, attack_name, pause_commands=True,
                                     sup_conclusion_pause=60, interval=3, start_pausing=5)
    experiments_details.append(experiment)

    # 3) DOLLAR CHAR DOS
    # ----------------------------------------------------------------------------------------------
    experiment = apts.dollar_char(target, 4, 20)
    experiments_details.append(experiment)

    experiment = apts.dollar_char(target, 5, 20)
    experiments_details.append(experiment)

    experiment = apts.dollar_char(target, 6, 20)
    experiments_details.append(experiment)

    experiment = apts.dollar_char(target, 7, 10)
    experiments_details.append(experiment)
    experiment = apts.dollar_char(target, 8, 10)
    experiments_details.append(experiment)
    experiment = apts.dollar_char(target, 9, 10)
    experiments_details.append(experiment)
    experiment = apts.dollar_char(target, 10, 5)
    experiments_details.append(experiment)
    experiment = apts.dollar_char(target, 11, 5)
    experiments_details.append(experiment)
    experiment = apts.dollar_char(target, 12, 5)
    experiments_details.append(experiment)
    end_time_all = datetime.now(tz=pytz.UTC)
    experiment = {
        "phase_number": 0,
        "attack_name": attack_name,
        "phase_name": "all_steps",
        "start_time": start_time_all,
        "end_time": end_time_all
    }
    experiments_details.append(experiment)
    with open('./output/exp_details.pkl', 'wb') as f:
        pickle.dump(experiments_details, f)
    print(experiments_details)


if __name__ == '__main__':
    main()
