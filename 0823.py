for i in range(1, 3):
    fo = open("/mnt/192.168.2." + str(i) + "/mnt/log.txt", "r")
    print("/mnt/192.168.2." + str(i) + "/mnt/log.txt")
    str = fo.readlines()
    print(str[i])
    fo.close()
