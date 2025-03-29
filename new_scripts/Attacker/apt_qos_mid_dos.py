import ssh_auto_access as ssh
import time
from datetime import datetime
import os
import apts


def main():
    iteration = str(int(os.getenv("qos_mid_dos_num_it")) + 1)
    os.putenv("qos_mid_dos_num_it", iteration)
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
    # ----------------------------------------------------------------------------------------------
    experiment = apts.qos_mid_dos(3, 10)
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
