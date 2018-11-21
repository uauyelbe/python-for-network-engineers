from os import listdir
from os.path import isfile, join

def parse_cdp_neighbors():
    mypath = "cdp"
    #filename = [f for f in listdir(mypath) if isfile(join(mypath, f))]
    result = {}
    key = []
    item = []
    for f in listdir(mypath):
        if isfile(join(mypath, f)):
            print(mypath)
            print(f)
            with open(f, "r") as cdp:
                cdp = cdp.readlines()
                a = [i.split(">") for i in cdp if "show cdp neighbors" in i]
                hostname = a[0][0]
                rindex = 1
                for i in cdp:
                    if "Eth" in i:
                        b = i.strip().split()
                        R = b[0]
                        bport = b[1] + b[2]
                        rport = b[-2] + b[-1]
                        rindex = rindex + 1
                        if (hostname, bport) not in key:
                            result[hostname, bport] = (R, rport)
                        tmp = (R, rport)
                        key.append(tmp)

    return result

print(parse_cdp_neighbors())