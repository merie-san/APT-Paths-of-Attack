import apts
import random
import time
import pickle
import pytz
from datetime import datetime


def main():
    experiments_details = []
    access_target = "10.0.0.7"
    attack_name = "user_property_dos"
    start_time_all = datetime.now(tz=pytz.UTC)

    # 1) INITIAL ACCESS
    # ----------------------------------------------------------------------------------------------
    commands = "sudo nmap -sS -T3 -Pn 192.168.1.0/24;sudo nmap -sS -T3  -Pn 192.168.0.0/24;sudo nmap  -sS -T3 -Pn 10.0.0.0/24"
    command_list = commands.split(";")
    experiment = apts.initial_access(access_target, 1.0, command_list, attack_name, pause_commands=True,
                                     sup_conclusion_pause=60, sup_interval_pause=5)
    experiments_details.append(experiment)

    time.sleep(random.randint(0, 200))

    # 1) INITIAL ACCESS
    # ----------------------------------------------------------------------------------------------
    experiment = apts.initial_access(access_target, 1.1, command_list, attack_name, sup_conclusion_pause=60)
    experiments_details.append(experiment)
    time.sleep(random.randint(0, 200))

    # 1opt) SSH BRUTEFORCE
    # ----------------------------------------------------------------------------------------------
    experiments = apts.brute_force(2.0, attack_name, 10, is_distributed=True)
    experiments_details.append(experiments)

    time.sleep(random.randint(0, 100))

    # 1opt) SSH BRUTEFORCE
    # ----------------------------------------------------------------------------------------------
    experiments = apts.brute_force(2.1, attack_name, 10, is_distributed=True)
    experiments_details.append(experiments)

    time.sleep(random.randint(0, 100))

    # 1opt) SSH BRUTEFORCE
    # ----------------------------------------------------------------------------------------------
    experiments = apts.brute_force(2.2, attack_name, 10, is_distributed=True)
    experiments_details.append(experiments)

    targets = ["10.0.0.4", "10.0.0.5", "10.0.0.6", "10.0.0.7"]

    # 2) MQTT DISCOVERY
    # ---------------------------------------------------------------------------------------------
    commands2 = "cat /etc/mosquitto/mosquitto.conf;cat /etc/mosquitto/conf.d;cat /var/lib/mosquitto/mosquitto.db;cat /var/log/mosquitto/mosquitto.log; cat /var/log/syslog;cat /var/log/syslog;sudo /usr/bin/nmap -sS -T3 -Pn -p 1883,8883 10.0.0.0/24;sudo nmap -sS -T3 -f -Pn -p 1883,8883 --script banner 10.0.0.0/24;sudo nmap -p 1883,8883 --script mqtt-subscribe 10.0.0.0/24"
    command_list2 = commands2.split(";")
    experiments = apts.mqtt_discovery(targets[random.randint(0, 3)], 3, command_list2, attack_name
                                      , pause_commands=True, sup_conclusion_pause=20, interval=5, start_pausing=6,
                                      sup_interval_pause=5)
    experiments_details.append(experiments)
    time.sleep(random.randint(80, 120))

    # 2) MQTT DISCOVERY
    # ---------------------------------------------------------------------------------------------
    experiments = apts.mqtt_discovery(targets[random.randint(0, 3)], 3.1, command_list2, attack_name,
                                      sup_conclusion_pause=10, pause_commands=True, interval=3, start_pausing=6,
                                      sup_interval_pause=5)
    experiments_details.append(experiments)
    time.sleep(random.randint(80, 120))

    # 3) USER PROPERTIES DOS
    # ---------------------------------------------------------------------------------------------

    experiment = apts.user_property_ddos(targets, 4, 20)
    experiments_details.append(experiment)
    experiment = apts.user_property_ddos(targets, 5, 20)
    experiments_details.append(experiment)
    experiment = apts.user_property_ddos(targets, 6, 20)
    experiments_details.append(experiment)
    experiment = apts.user_property_ddos(targets, 7, 40)
    experiments_details.append(experiment)
    experiment = apts.user_property_ddos(targets, 8, 20)
    experiments_details.append(experiment)
    experiment = apts.user_property_ddos(targets, 9, 20)
    experiments_details.append(experiment)
    experiment = apts.user_property_ddos(targets, 10, 40)
    experiments_details.append(experiment)
    experiment = apts.user_property_ddos(targets, 11, 20)
    experiments_details.append(experiment)
    experiment = apts.user_property_ddos(targets, 12, 20)
    experiments_details.append(experiment)
    experiment = apts.user_property_ddos(targets, 13, 40)
    experiments_details.append(experiment)

    # 2) MQTT DISCOVERY
    # ---------------------------------------------------------------------------------------------
    command_list2 = commands2.split(";")
    experiments = apts.mqtt_discovery(targets, 14, command_list2, attack_name
                                      , pause_commands=True, sup_conclusion_pause=30, interval=1, start_pausing=5,
                                      sup_interval_pause=10)
    experiments_details.append(experiments)

    # 3) USER PROPERTIES DOS
    # ---------------------------------------------------------------------------------------------
    experiment = apts.user_property_ddos(targets, 15, 10)
    experiments_details.append(experiment)
    experiment = apts.user_property_ddos(targets, 16, 10)
    experiments_details.append(experiment)
    experiment = apts.user_property_ddos(targets, 17, 20)
    experiments_details.append(experiment)
    experiment = apts.user_property_ddos(targets, 18, 40)
    experiments_details.append(experiment)
    experiment = apts.user_property_ddos(targets, 19, 80)
    experiments_details.append(experiment)
    experiment = apts.user_property_ddos(targets, 20, 80)
    experiments_details.append(experiment)
    experiment = apts.user_property_ddos(targets, 21, 40)
    experiments_details.append(experiment)
    experiment = apts.user_property_ddos(targets, 22, 20)
    experiments_details.append(experiment)
    experiment = apts.user_property_ddos(targets, 23, 10)
    experiments_details.append(experiment)
    experiment = apts.user_property_ddos(targets, 24, 10)
    experiments_details.append(experiment)

    # 2) MQTT DISCOVERY
    # ---------------------------------------------------------------------------------------------
    command_list2 = commands2.split(";")
    experiments = apts.mqtt_discovery(targets, 14, command_list2, attack_name
                                      , pause_commands=True, sup_conclusion_pause=20, interval=1, start_pausing=5,
                                      sup_interval_pause=15)
    experiments_details.append(experiments)

    # 3) USER PROPERTIES DOS
    # ---------------------------------------------------------------------------------------------
    experiment = apts.user_property_ddos(targets, 25, 5)
    experiments_details.append(experiment)
    experiment = apts.user_property_ddos(targets, 26, 10)
    experiments_details.append(experiment)
    experiment = apts.user_property_ddos(targets, 27, 20)
    experiments_details.append(experiment)
    experiment = apts.user_property_ddos(targets, 28, 40)
    experiments_details.append(experiment)
    experiment = apts.user_property_ddos(targets, 29, 10)
    experiments_details.append(experiment)
    experiment = apts.user_property_ddos(targets, 30, 10)
    experiments_details.append(experiment)
    experiment = apts.user_property_ddos(targets, 31, 40)
    experiments_details.append(experiment)
    experiment = apts.user_property_ddos(targets, 32, 20)
    experiments_details.append(experiment)
    experiment = apts.user_property_ddos(targets, 33, 10)
    experiments_details.append(experiment)
    experiment = apts.user_property_ddos(targets, 34, 5)
    experiments_details.append(experiment)

    print(experiments_details)
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
