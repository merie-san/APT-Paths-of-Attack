import pickle
from datetime import datetime
import pytz
import apts


# def initial_access(phase_number, pause):

# start_time = datetime.utcnow()
# commands = "netstat -t;netstat -tuln;ss -tuln;ss -tr;ss -ntr;nmap -T0 -sI -f 192.168.1.0/24;nmap -T5 -sP 192.168.0.0/24;nmap -T5 -sP 10.0.0.0/24;nmap -T5 -sP 192.168.0.0/24"
# commands_list = commands.split(';')
# ssh.ssh_commands("10.0.0.7", "ope", "maint", commands_list, 1, 5, "./out.log", 9999)
# end_time = datetime.utcnow()
# experiment = {
# "phase_number": phase_number,
# "attack_name": "empty_connection_dos",
# "phase_name": "network_discovery",
# "start_time": start_time,
# "end_time": end_time
# }
# time.sleep(pause)

# return experiment


# def mqtt_discovery(phase_number, pause):
#    start_time = datetime.utcnow()
#   commands = "cat /etc/mosquitto/mosquitto.conf;cat /etc/mosquitto/conf.d;cat /var/lib/mosquitto/mosquitto.db;cat /var/log/mosquitto/mosquitto.log; cat /var/log/syslog;cat /var/log/syslog;/usr/bin/nmap -T5 -p 1883,8883 -sV 10.0.0.0/24;sleep 20;nmap -T5 -p 1883,8883 -sV --script banner 10.0.0.0/24; nmap -p 1883,8883 --script mqtt-subscribe 10.0.0.0/24"
#  commands_list = commands.split(';')
# ssh.ssh_commands("10.0.0.7", "ope", "maint", commands_list, 1, 5, "./out1.log", 6666)
# end_time = datetime.utcnow()
# experiment = {
#	"phase_number": phase_number,
#	"attack_name": "empty_connection_dos",
#	"phase_name": "mqtt_discovery",
#	"start_time": start_time,
#	"end_time": end_time
#	}
# time.sleep(pause)

# return experiment


# def brute_force(phase_number, pause):
#    start_time = datetime.utcnow()
#    os.system('python3 ssh_brute_force.py')
#    end_time = datetime.utcnow()
#    experiment = {
#		"phase_number": phase_number,
# "attack_name": "empty_connection_dos",
# "phase_name": "ssh_brute_force",
# "start_time": start_time,
# "end_time": end_time
# }
# time.sleep(pause)

# return experiment


# def empty_connection_dos(phase_number, pause):

#   start_time = datetime.utcnow()
#  commands = "python3 empty_connection_ddos.py"
# commands_list = commands.split(';')
# ssh.ssh_commands("10.0.0.7", "ope", "maint", commands_list, 1, 5, "./out1.log", 6666)
# end_time = datetime.utcnow()
# experiment = {
#	"phase_number": phase_number,
#	"attack_name": "empty_connection_dos",
#	"phase_name": "empty_connection_dos",
#	"start_time": start_time,
#	"end_time": end_time
#	}
# time.sleep(pause)

# return experiment


def main():
    experiments_details = []
    target = "10.0.0.7"
    attack_name = "empty_connection_dos_stealth"
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

    # 3) EMPTY CONNECTION DOS
    # ----------------------------------------------------------------------------------------------
    experiment = apts.empty_connection_dos(target, 3, 60)
    experiments_details.append(experiment)

    print(experiments_details)
    end_time_all = datetime.now(tz=pytz.UTC)
    experiment = {
        "phase_number": 0,
        "attack_name": "empty_connection_dos_stealth",
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
