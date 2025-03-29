import os
import random

import pytz
import time
from datetime import datetime
import apts
import pickle


def main():
    iteration = str(int(os.getenv("empty_connection_ddos_num_it")) + 1)
    os.putenv("empty_connection_ddos_num_it", iteration)
    experiments_details = []
    access_target = "10.0.0.20"
    attack_name = "empty_connection_ddos"
    start_time_all = datetime.now(tz=pytz.UTC)

    # 1) INITIAL ACCESS
    # ----------------------------------------------------------------------------------------------
    commands = "sudo nmap -sS -T3 -Pn 192.168.1.0/24;sudo nmap -sS -T3 -Pn 192.168.0.0/24;sudo nmap -sS -T3 -Pn 10.0.0.0/24"
    command_list = commands.split(";")
    experiment = apts.initial_access(access_target, "1.1", command_list, attack_name, "nmap_T3", iteration,
                                     pause_commands=True, sup_conclusion_pause=60)
    experiments_details.append(experiment)

    time.sleep(random.randint(0, 120))

    # 1) INITIAL ACCESS
    # ----------------------------------------------------------------------------------------------
    experiment = apts.initial_access(access_target, "1.2", command_list, attack_name, "nmap_T3", iteration,
                                     sup_conclusion_pause=60)
    experiments_details.append(experiment)
    time.sleep(random.randint(0, 180))

    # 1opt) SSH BRUTEFORCE
    # ----------------------------------------------------------------------------------------------
    experiments = apts.brute_force("1.3", "empty_connection_ddos", iteration, is_distributed=True)
    experiments_details.append(experiments)

    time.sleep(random.randint(0, 120))

    # 1opt) SSH BRUTEFORCE
    # ----------------------------------------------------------------------------------------------
    experiments = apts.brute_force("1.4", "empty_connection_ddos", iteration, is_distributed=True)
    experiments_details.append(experiments)

    prefix = "10.0.0."
    targets = []
    for i in range(4, 23):
        targets.append(prefix + str(i))

    # 2) MQTT DISCOVERY
    # ---------------------------------------------------------------------------------------------
    commands2 = "cat /etc/mosquitto/mosquitto.conf;cat /etc/mosquitto/conf.d;cat /var/lib/mosquitto/mosquitto.db;cat /var/log/mosquitto/mosquitto.log; cat /var/log/syslog;cat /var/log/syslog;sudo /usr/bin/nmap -sS -T3 -Pn -p 1883,8883 10.0.0.0/24;sudo nmap -sS -T3 -f -Pn -p 1883,8883 --script banner 10.0.0.0/24;sudo nmap -p 1883,8883 --script mqtt-subscribe 10.0.0.0/24"
    command_list2 = commands2.split(";")
    experiments = apts.mqtt_discovery(targets[random.randint(0, len(targets))], "1.5", command_list2, attack_name,
                                      "mqtt_cat", iteration,
                                      sup_conclusion_pause=60, pause_commands=True, interval=3, start_pausing=6)
    experiments_details.append(experiments)
    time.sleep(random.randint(100, 160))

    # 2) MQTT DISCOVERY
    # ---------------------------------------------------------------------------------------------
    experiments = apts.mqtt_discovery(targets[random.randint(0, len(targets))], "1.6", command_list2, attack_name,
                                      "mqtt_cat", iteration,
                                      sup_conclusion_pause=60, pause_commands=True, interval=3, start_pausing=6)
    experiments_details.append(experiments)

    # 3) EMPTY CONNECTION DOS
    # ----------------------------------------------------------------------------------------------
    experiment = apts.empty_connection_ddos(targets, "2.1", 10, iteration)
    experiments_details.append(experiment)
    experiment = apts.empty_connection_ddos(targets, "2.2", 20, iteration)
    experiments_details.append(experiment)
    experiment = apts.empty_connection_ddos(targets, "2.3", 15, iteration)
    experiments_details.append(experiment)
    experiment = apts.empty_connection_ddos(targets, "2.4", 20, iteration)
    experiments_details.append(experiment)
    experiment = apts.empty_connection_ddos(targets, "2.5", 20, iteration)
    experiments_details.append(experiment)
    experiment = apts.empty_connection_ddos(targets, "2.6", 20, iteration)
    experiments_details.append(experiment)
    experiment = apts.empty_connection_ddos(targets, "2.7", 15, iteration)
    experiments_details.append(experiment)
    experiment = apts.empty_connection_ddos(targets, "2.8", 20, iteration)
    experiments_details.append(experiment)
    experiment = apts.empty_connection_ddos(targets, "2.9", 10, iteration)
    experiments_details.append(experiment)
    experiment = apts.empty_connection_ddos(targets, "2.10", 20, iteration)
    experiments_details.append(experiment)
    experiment = apts.empty_connection_ddos(targets, "2.11", 25, iteration)
    experiments_details.append(experiment)
    experiment = apts.empty_connection_ddos(targets, "2.12", 30, iteration)
    experiments_details.append(experiment)

    time.sleep(60)

    # 2) MQTT DISCOVERY
    # ---------------------------------------------------------------------------------------------
    experiments = apts.mqtt_discovery(targets[random.randint(0, len(targets))], "1.7", command_list2, attack_name,
                                      "mqtt_cat", iteration,
                                      sup_conclusion_pause=60)
    experiments_details.append(experiments)

    # 3) EMPTY CONNECTION DOS
    # ----------------------------------------------------------------------------------------------
    experiment = apts.empty_connection_ddos(targets, "2.13", 20, iteration)
    experiments_details.append(experiment)
    experiment = apts.empty_connection_ddos(targets, "2.14", 10, iteration)
    experiments_details.append(experiment)

    experiment = apts.empty_connection_ddos(targets, "2.15", 20, iteration)
    experiments_details.append(experiment)
    experiment = apts.empty_connection_ddos(targets, "2.16", 25, iteration)
    experiments_details.append(experiment)
    experiment = apts.empty_connection_ddos(targets, "2.17", 30, iteration)
    experiments_details.append(experiment)

    # 2) MQTT DISCOVERY
    # ---------------------------------------------------------------------------------------------
    experiments = apts.mqtt_discovery(targets[random.randint(0, 3)], "1.8", command_list2, attack_name, "mqtt_cat",
                                      iteration, sup_conclusion_pause=60)

    experiments_details.append(experiments)

    # 3) EMPTY CONNECTION DOS
    # ----------------------------------------------------------------------------------------------
    experiment = apts.empty_connection_ddos(targets, "2.18", 20, iteration)
    experiments_details.append(experiment)
    experiment = apts.empty_connection_ddos(targets, "2.19", 10, iteration)
    experiments_details.append(experiment)
    experiment = apts.empty_connection_ddos(targets, "2.20", 20, iteration)
    experiments_details.append(experiment)
    experiment = apts.empty_connection_ddos(targets, "2.21", 25, iteration)
    experiments_details.append(experiment)
    experiment = apts.empty_connection_ddos(targets, "2.22", 30, iteration)
    experiments_details.append(experiment)
    experiment = apts.empty_connection_ddos(targets, "2.23", 10, iteration)
    experiments_details.append(experiment)
    experiment = apts.empty_connection_ddos(targets, "2.24", 20, iteration)
    experiments_details.append(experiment)
    experiment = apts.empty_connection_ddos(targets, "2.25", 15, iteration)
    experiments_details.append(experiment)
    experiment = apts.empty_connection_ddos(targets, "2.26", 20, iteration)
    experiments_details.append(experiment)
    experiment = apts.empty_connection_ddos(targets, "2.27", 20, iteration)
    experiments_details.append(experiment)
    experiment = apts.empty_connection_ddos(targets, "2.28", 20, iteration)
    experiments_details.append(experiment)
    experiment = apts.empty_connection_ddos(targets, "2.29", 15, iteration)
    experiments_details.append(experiment)
    experiment = apts.empty_connection_ddos(targets, "2.30", 20, iteration)
    experiments_details.append(experiment)
    experiment = apts.empty_connection_ddos(targets, "2.31", 10, iteration)
    experiments_details.append(experiment)
    experiment = apts.empty_connection_ddos(targets, "2.32", 20, iteration)
    experiments_details.append(experiment)
    experiment = apts.empty_connection_ddos(targets, "2.33", 25, iteration)
    experiments_details.append(experiment)
    experiment = apts.empty_connection_ddos(targets, "2.34", 30, iteration)
    experiments_details.append(experiment)

    print(experiments_details)
    end_time_all = datetime.now(tz=pytz.UTC)
    experiment = {
        "phase_number": 0,
        "attack_name": "empty_connection_ddos",
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
