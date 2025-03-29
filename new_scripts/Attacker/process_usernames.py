i = 0
with open("usernames_l.txt", "r") as f:
    with open("namelist.txt", "w") as fout:
        for line in f:
            if i % 81 == 0:
                fout.write(line)
            i += 1
