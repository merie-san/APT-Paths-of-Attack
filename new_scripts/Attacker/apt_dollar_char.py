import pickle
import random
import pytz
import time
from datetime import datetime
import apts
import os


def main():
    iteration = str(int(os.getenv("dollar_char_num_it")) + 1)
    os.putenv("dollar_char_num_it", iteration)
    target = "10.0.20"
    attack_name = "dollar_char"
    experiments_details = []
    start_time_all = datetime.now(tz=pytz.UTC)
    # 1) RECONNAISSANCE
    # ----------------------------------------------------------------------------------------------
    commands = "netstat -t;netstat -tuln;ss -tuln;ss -tr;ss -ntr; sudo nmap -sS -T1 -Pn 192.168.1.0/24"
    command_list = commands.split(";")
    experiment = apts.initial_access(target, "1.1", command_list, attack_name, "netstat", iteration,
                                     pause_commands=True, sup_conclusion_pause=2)
    experiments_details.append(experiment)
    time.sleep(random.randint(180, 360))

    with open('./output/exp_details.pkl', 'wb') as f:
        pickle.dump(experiments_details, f)

    # 1) RECONNAISSANCE
    # ----------------------------------------------------------------------------------------------
    commands = "sudo nmap  -sS -T2 -Pn 10.0.0/24"
    command_list = commands.split(";")
    experiment = apts.initial_access(target, "1.2", command_list, attack_name, "nmap_10", iteration,
                                     pause_commands=False, sup_conclusion_pause=2)
    experiments_details.append(experiment)
    time.sleep(random.randint(120, 420))

    with open('./output/exp_details.pkl', 'wb') as f:
        pickle.dump(experiments_details, f)

    # 1) RECONNAISSANCE
    # ----------------------------------------------------------------------------------------------
    commands = "netstat -t;netstat -tuln;ss -tuln;ss -tr;ss -ntr; sudo nmap -sS -T1 -Pn 192.168.1.0/24"
    command_list = commands.split(";")
    experiment = apts.initial_access(target, "1.3", command_list, attack_name, "netstat", iteration,
                                     pause_commands=True, sup_conclusion_pause=2)
    experiments_details.append(experiment)
    time.sleep(random.randint(1, 60))

    with open('./output/exp_details.pkl', 'wb') as f:
        pickle.dump(experiments_details, f)

    # 1) RECONNAISSANCE
    # ----------------------------------------------------------------------------------------------
    commands = "sudo nmap  -sS -T2 -Pn 10.0.0.0/24"
    command_list = commands.split(";")
    experiment = apts.initial_access(target, "1.4", command_list, attack_name, "nmap_10", iteration,
                                     pause_commands=False, sup_conclusion_pause=2)
    experiments_details.append(experiment)
    time.sleep(random.randint(60, 180))

    with open('./output/exp_details.pkl', 'wb') as f:
        pickle.dump(experiments_details, f)

    # 1) RECONNAISSANCE
    # ----------------------------------------------------------------------------------------------
    commands = "netstat -t;netstat -tuln;ss -tuln;ss -tr;ss -ntr; sudo nmap -sS -T1 -Pn 192.168.1.0/24"
    command_list = commands.split(";")
    experiment = apts.initial_access(target, "1.5", command_list, attack_name, "netstat", iteration,
                                     pause_commands=True, sup_conclusion_pause=2)
    experiments_details.append(experiment)
    time.sleep(random.randint(200, 260))

    with open('./output/exp_details.pkl', 'wb') as f:
        pickle.dump(experiments_details, f)

    # 1) RECONNAISSANCE
    # ----------------------------------------------------------------------------------------------
    commands = "sudo nmap  -sS -T2 -Pn 10.0.0/24"
    command_list = commands.split(";")
    experiment = apts.initial_access(target, "1.6", command_list, attack_name, "nmap_10", iteration,
                                     pause_commands=False, sup_conclusion_pause=2)
    experiments_details.append(experiment)
    time.sleep(random.randint(800, 1200))
    with open('./output/exp_details.pkl', 'wb') as f:
        pickle.dump(experiments_details, f)

    # 2) SSH BRUTEFORCE
    # ----------------------------------------------------------------------------------------------
    experiment = apts.brute_force("1.7", attack_name, iteration)
    experiments_details.append(experiment)
    time.sleep(random.randint(6, 120))

    with open('./output/exp_detail.pkl', 'wb') as f:
        pickle.dump(experiments_details, f)

    # 2) SSH BRUTEFORCE
    # ----------------------------------------------------------------------------------------------
    experiment = apts.brute_force("1.8", attack_name, iteration)
    experiments_details.append(experiment)
    time.sleep(random.randint(600, 1200))

    with open('./output/exp_details.pkl', 'wb') as f:
        pickle.dump(experiments_details, f)

    # 2) MQTT DISCOVERY
    # ---------------------------------------------------------------------------------------------
    commands2 = "cat /etc/mosquitto/mosquitto.conf;cat /etc/mosquitto/conf.d;cat /var/lib/mosquitto/mosquitto.db;cat /var/log/mosquitto/mosquitto.log; cat /var/log/syslog;cat /var/log/syslog;sudo /usr/bin/nmap -sS -T2 -Pn -p 1883,8883 10.0.0/24"
    command_list2 = commands2.split(";")
    experiment = apts.mqtt_discovery(target, "1.9", command_list2, attack_name, "nmap_mqtt", iteration,
                                     pause_commands=False, sup_conclusion_pause=60)
    experiments_details.append(experiment)
    time.sleep(random.randint(80, 160))

    with open('./output/exp_details.pkl', 'wb') as f:
        pickle.dump(experiments_details, f)

    # 2) MQTT DISCOVERY
    # ---------------------------------------------------------------------------------------------
    commands2 = "sudo nmap -sS -T2 -f -Pn -p 1883,8883 --script banner 10.0.0/24"
    command_list2 = commands2.split(";")
    experiment = apts.mqtt_discovery(target, "1.10", command_list2, attack_name, "nmap_banner",
                                     iteration, pause_commands=False)
    experiments_details.append(experiment)
    time.sleep(random.randint(60, 180))

    with open('./output/exp_details.pkl', 'wb') as f:
        pickle.dump(experiments_details, f)

    # 2) MQTT DISCOVERY
    # ---------------------------------------------------------------------------------------------
    commands2 = "sudo nmap -p 1883,8883 --script mqtt-subscribe 10.0.0/24"
    command_list2 = commands2.split(";")
    experiment = apts.mqtt_discovery(target, "1.11", command_list2, attack_name, "nmap_sub", iteration,
                                     pause_commands=False)
    experiments_details.append(experiment)
    time.sleep(random.randint(60, 180))

    with open('./output/exp_details.pkl', 'wb') as f:
        pickle.dump(experiments_details, f)

    # 3) DOLLAR CHAR DOS
    # ----------------------------------------------------------------------------------------------
    experiment = apts.dollar_char(target, "2.1", random.randint(120, 600), iteration)
    experiments_details.append(experiment)
    with open('./output/exp_details.pkl', 'wb') as f:
        pickle.dump(experiments_details, f)

    experiment = apts.dollar_char(target, "2.2", random.randint(800, 900), iteration)
    experiments_details.append(experiment)
    time.sleep(random.randint(280, 480))
    with open('./output/exp_details.pkl', 'wb') as f:
        pickle.dump(experiments_details, f)

    experiment = apts.dollar_char(target, "2.3", random.randint(60, 120), iteration)
    experiments_details.append(experiment)
    time.sleep(random.randint(400, 500))
    with open('./output/exp_details.pkl', 'wb') as f:
        pickle.dump(experiments_details, f)

    # 3) DOLLAR CHAR DOS
    # ----------------------------------------------------------------------------------------------
    experiment = apts.dollar_char(target, "2.4", random.randint(600, 1200), iteration)
    experiments_details.append(experiment)
    time.sleep(random.randint(60, 120))
    with open('./output/exp_details.pkl', 'wb') as f:
        pickle.dump(experiments_details, f)

    experiment = apts.dollar_char(target, "2.5", random.randint(800, 900), iteration)
    experiments_details.append(experiment)
    time.sleep(random.randint(60, 180))
    with open('./output/exp_details.pkl', 'wb') as f:
        pickle.dump(experiments_details, f)

    experiment = apts.dollar_char(target, "2.6", random.randint(600, 700), iteration)
    experiments_details.append(experiment)
    time.sleep(random.randint(60, 560))
    with open('./output/exp_details.pkl', 'wb') as f:
        pickle.dump(experiments_details, f)

        # 2) MQTT DISCOVERY
    # ---------------------------------------------------------------------------------------------
    commands2 = "cat /etc/mosquitto/mosquitto.conf;cat /etc/mosquitto/conf.d;cat /var/lib/mosquitto/mosquitto.db;cat /var/log/mosquitto/mosquitto.log; cat /var/log/syslog;cat /var/log/syslog;sudo /usr/bin/nmap -sS -T2 -Pn -p 1883,8883 10.0.0/24"
    command_list2 = commands2.split(";")
    experiment = apts.mqtt_discovery(target, "1.12", command_list2, attack_name, "nmap_mqtt", iteration,
                                     pause_commands=False, sup_conclusion_pause=60)
    experiments_details.append(experiment)
    time.sleep(random.randint(80, 160))

    with open('./output/exp_details.pkl', 'wb') as f:
        pickle.dump(experiments_details, f)

    # 2) MQTT DISCOVERY
    # ---------------------------------------------------------------------------------------------
    commands2 = "sudo nmap -sS -T2 -f -Pn -p 1883,8883 --script banner 10.0.0/24"
    command_list2 = commands2.split(";")
    experiment = apts.mqtt_discovery(target, "1.13", command_list2, attack_name, "nmap_banner",
                                     iteration, pause_commands=False)
    experiments_details.append(experiment)
    time.sleep(random.randint(60, 180))

    with open('./output/exp_details.pkl', 'wb') as f:
        pickle.dump(experiments_details, f)

    # 2) MQTT DISCOVERY
    # ---------------------------------------------------------------------------------------------
    commands2 = "cat /etc/mosquitto/mosquitto.conf;cat /etc/mosquitto/conf.d;cat /var/lib/mosquitto/mosquitto.db;cat /var/log/mosquitto/mosquitto.log; cat /var/log/syslog;cat /var/log/syslog;sudo /usr/bin/nmap -sS -T2 -Pn -p 1883,8883 10.0.0/24"
    command_list2 = commands2.split(";")
    experiment = apts.mqtt_discovery(target, "1.14", command_list2, attack_name, "nmap_mqtt", iteration,
                                     pause_commands=False, sup_conclusion_pause=60)
    experiments_details.append(experiment)
    time.sleep(random.randint(80, 160))

    with open('./output/exp_details.pkl', 'wb') as f:
        pickle.dump(experiments_details, f)

    # 2) MQTT DISCOVERY
    # ---------------------------------------------------------------------------------------------
    commands2 = "sudo nmap -sS -T2 -f -Pn -p 1883,8883 --script banner 10.0.0/24"
    command_list2 = commands2.split(";")
    experiment = apts.mqtt_discovery(target, "1.15", command_list2, attack_name, "nmap_banner",
                                     iteration, pause_commands=False)
    experiments_details.append(experiment)
    time.sleep(random.randint(60, 180))

    with open('./output/exp_details.pkl', 'wb') as f:
        pickle.dump(experiments_details, f)


    # 3) DOLLAR CHAR DOS
    # ----------------------------------------------------------------------------------------------
    experiment = apts.dollar_char(target, "2.7", random.randint(600, 750), iteration)
    experiments_details.append(experiment)
    time.sleep(random.randint(60, 120))
    with open('./output/exp_details.pkl', 'wb') as f:
        pickle.dump(experiments_details, f)

    experiment = apts.dollar_char(target, "2.8", random.randint(360, 450), iteration)
    experiments_details.append(experiment)
    time.sleep(random.randint(50, 120))
    with open('./output/exp_details.pkl', 'wb') as f:
        pickle.dump(experiments_details, f)

    # 3) DOLLAR CHAR DOS
    # ----------------------------------------------------------------------------------------------
    experiment = apts.dollar_char(target, "2.9", random.randint(180, 600), iteration)
    time.sleep(random.randint(60, 120))
    with open('./output/exp_details.pkl', 'wb') as f:
        pickle.dump(experiments_details, f)

    experiment = apts.dollar_char(target, "2.10", random.randint(160, 1000), iteration)
    experiments_details.append(experiment)
    with open('./output/exp_details.pkl', 'wb') as f:
        pickle.dump(experiments_details, f)

    experiment = apts.dollar_char(target, "2.11", random.randint(60, 360), iteration)
    experiments_details.append(experiment)
    with open('./output/exp_details.pkl', 'wb') as f:
        pickle.dump(experiments_details, f)
    time.sleep(random.randint(600, 800))

    # 3) DOLLAR CHAR DOS
    # ----------------------------------------------------------------------------------------------
    experiment = apts.dollar_char(target, "2.12", random.randint(120, 600), iteration)
    experiments_details.append(experiment)
    with open('./output/exp_details.pkl', 'wb') as f:
        pickle.dump(experiments_details, f)

    experiment = apts.dollar_char(target, "2.13", random.randint(800, 900), iteration)
    experiments_details.append(experiment)
    time.sleep(random.randint(280, 480))
    with open('./output/exp_details.pkl', 'wb') as f:
        pickle.dump(experiments_details, f)

    experiment = apts.dollar_char(target, "2.14", random.randint(60, 120), iteration)
    experiments_details.append(experiment)
    time.sleep(random.randint(400, 500))
    with open('./output/exp_details.pkl', 'wb') as f:
        pickle.dump(experiments_details, f)

    # 3) DOLLAR CHAR DOS
    # ----------------------------------------------------------------------------------------------
    experiment = apts.dollar_char(target, "2.15", random.randint(600, 1200), iteration)
    experiments_details.append(experiment)
    time.sleep(random.randint(60, 120))
    with open('./output/exp_details.pkl', 'wb') as f:
        pickle.dump(experiments_details, f)

    experiment = apts.dollar_char(target, "2.16", random.randint(800, 900), iteration)
    experiments_details.append(experiment)
    time.sleep(random.randint(60, 180))
    with open('./output/exp_details.pkl', 'wb') as f:
        pickle.dump(experiments_details, f)

    experiment = apts.dollar_char(target, "2.17", random.randint(600, 700), iteration)
    experiments_details.append(experiment)
    time.sleep(random.randint(60, 560))
    with open('./output/exp_details.pkl', 'wb') as f:
        pickle.dump(experiments_details, f)

    # 3) DOLLAR CHAR DOS
    # ----------------------------------------------------------------------------------------------
    experiment = apts.dollar_char(target, "2.18", random.randint(600, 750), iteration)
    experiments_details.append(experiment)
    time.sleep(random.randint(60, 120))
    with open('./output/exp_details.pkl', 'wb') as f:
        pickle.dump(experiments_details, f)

    experiment = apts.dollar_char(target, "2.19", random.randint(360, 450), iteration)
    experiments_details.append(experiment)
    time.sleep(random.randint(50, 120))
    with open('./output/exp_details.pkl', 'wb') as f:
        pickle.dump(experiments_details, f)

    # 3) DOLLAR CHAR DOS
    # ----------------------------------------------------------------------------------------------
    experiment = apts.dollar_char(target, "2.20", random.randint(180, 600), iteration)
    time.sleep(random.randint(60, 120))
    with open('./output/exp_details.pkl', 'wb') as f:
        pickle.dump(experiments_details, f)

    experiment = apts.dollar_char(target, "2.21", random.randint(160, 1000), iteration)
    experiments_details.append(experiment)
    with open('./output/exp_details.pkl', 'wb') as f:
        pickle.dump(experiments_details, f)

    experiment = apts.dollar_char(target, "2.22", random.randint(60, 360), iteration)
    experiments_details.append(experiment)
    with open('./output/exp_details.pkl', 'wb') as f:
        pickle.dump(experiments_details, f)
    time.sleep(random.randint(600, 800))

    # 3) DOLLAR CHAR DOS
    # ----------------------------------------------------------------------------------------------
    experiment = apts.dollar_char(target, "2.23", random.randint(120, 600), iteration)
    experiments_details.append(experiment)
    with open('./output/exp_details.pkl', 'wb') as f:
        pickle.dump(experiments_details, f)

    experiment = apts.dollar_char(target, "2.24", random.randint(800, 900), iteration)
    experiments_details.append(experiment)
    time.sleep(random.randint(280, 480))
    with open('./output/exp_details.pkl', 'wb') as f:
        pickle.dump(experiments_details, f)

    experiment = apts.dollar_char(target, "2.25", random.randint(60, 120), iteration)
    experiments_details.append(experiment)
    time.sleep(random.randint(400, 500))
    with open('./output/exp_details.pkl', 'wb') as f:
        pickle.dump(experiments_details, f)

    # 3) DOLLAR CHAR DOS
    # ----------------------------------------------------------------------------------------------
    experiment = apts.dollar_char(target, "2.26", random.randint(600, 1200), iteration)
    experiments_details.append(experiment)
    time.sleep(random.randint(60, 120))
    with open('./output/exp_details.pkl', 'wb') as f:
        pickle.dump(experiments_details, f)

    experiment = apts.dollar_char(target, "2.27", random.randint(800, 900), iteration)
    experiments_details.append(experiment)
    time.sleep(random.randint(60, 180))
    with open('./output/exp_details.pkl', 'wb') as f:
        pickle.dump(experiments_details, f)

    experiment = apts.dollar_char(target, "2.28", random.randint(600, 700), iteration)
    experiments_details.append(experiment)
    time.sleep(random.randint(60, 560))
    with open('./output/exp_details.pkl', 'wb') as f:
        pickle.dump(experiments_details, f)

    # 3) DOLLAR CHAR DOS
    # ----------------------------------------------------------------------------------------------
    experiment = apts.dollar_char(target, "2.29", random.randint(600, 750), iteration)
    experiments_details.append(experiment)
    time.sleep(random.randint(60, 120))
    with open('./output/exp_details.pkl', 'wb') as f:
        pickle.dump(experiments_details, f)

    experiment = apts.dollar_char(target, "2.30", random.randint(360, 450), iteration)
    experiments_details.append(experiment)
    time.sleep(random.randint(50, 120))
    with open('./output/exp_details.pkl', 'wb') as f:
        pickle.dump(experiments_details, f)

    # 3) DOLLAR CHAR DOS
    # ----------------------------------------------------------------------------------------------
    experiment = apts.dollar_char(target, "2.31", random.randint(180, 600), iteration)
    time.sleep(random.randint(60, 120))
    with open('./output/exp_details.pkl', 'wb') as f:
        pickle.dump(experiments_details, f)

    experiment = apts.dollar_char(target, "2.32", random.randint(160, 1000), iteration)
    experiments_details.append(experiment)
    with open('./output/exp_details.pkl', 'wb') as f:
        pickle.dump(experiments_details, f)

    experiment = apts.dollar_char(target, "2.33", random.randint(60, 360), iteration)
    experiments_details.append(experiment)
    with open('./output/exp_details.pkl', 'wb') as f:
        pickle.dump(experiments_details, f)
    time.sleep(random.randint(600, 800))

    # 3) DOLLAR CHAR DOS
    # ----------------------------------------------------------------------------------------------
    experiment = apts.dollar_char(target, "2.34", random.randint(120, 600), iteration)
    experiments_details.append(experiment)
    with open('./output/exp_details.pkl', 'wb') as f:
        pickle.dump(experiments_details, f)

    experiment = apts.dollar_char(target, "2.35", random.randint(120, 600), iteration)
    experiments_details.append(experiment)
    time.sleep(random.randint(280, 480))
    with open('./output/exp_details.pkl', 'wb') as f:
        pickle.dump(experiments_details, f)

    experiment = apts.dollar_char(target, "2.36", random.randint(60, 120), iteration)
    experiments_details.append(experiment)
    time.sleep(random.randint(400, 500))
    with open('./output/exp_details.pkl', 'wb') as f:
        pickle.dump(experiments_details, f)

    # 3) DOLLAR CHAR DOS
    # ----------------------------------------------------------------------------------------------
    experiment = apts.dollar_char(target, "2.37", random.randint(600, 1200), iteration)
    experiments_details.append(experiment)
    time.sleep(random.randint(60, 120))
    with open('./output/exp_details.pkl', 'wb') as f:
        pickle.dump(experiments_details, f)

    experiment = apts.dollar_char(target, "2.38", random.randint(800, 900), iteration)
    experiments_details.append(experiment)
    time.sleep(random.randint(60, 180))
    with open('./output/exp_details.pkl', 'wb') as f:
        pickle.dump(experiments_details, f)

    experiment = apts.dollar_char(target, "2.39", random.randint(600, 700), iteration)
    experiments_details.append(experiment)
    time.sleep(random.randint(60, 560))
    with open('./output/exp_details.pkl', 'wb') as f:
        pickle.dump(experiments_details, f)

    experiment = apts.dollar_char(target, "2.40", random.randint(600, 700), iteration)
    experiments_details.append(experiment)
    time.sleep(random.randint(60, 560))
    with open('./output/exp_details.pkl', 'wb') as f:
        pickle.dump(experiments_details, f)

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
    with open('./output/exp_details_long.pkl', 'wb') as f:
        pickle.dump(experiments_details, f)
    print(experiments_details)


if __name__ == '__main__':
    main()
