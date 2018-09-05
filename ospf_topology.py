from os import listdir
from os.path import isfile, join

def parse_ospf_topology():
    mypath = "ospf"
    #filename = [f for f in listdir(mypath) if isfile(join(mypath, f))]
    result = {} #final result as dictionary
    key = [] #saves keys of the dictionary

    """checks is it file in directory and analyzes content of the file"""
    for f in listdir(mypath):
        if isfile(join(mypath, f)):
            with open(mypath + "/" + f, "r") as ospf:
                ospf = ospf.readlines()
                #a = [i.split(">") for i in cdp if "show cdp neighbors" in i]
                hostname = f.split(".txt")[0] #takes names of file
                for i in ospf:
                    b = i.strip().split()
                    interface = b[1] #takes ospf interface
                    id = b[3] #takse router id of the neighbor
                    if (hostname, interface) not in key:
                        result[hostname, interface] = (id)
                    key.append(id)

    for key in result:
        id = key[0]
        port_id = key[1]
        n_id = result[key]
        for key1 in result:
            id1 = key1[0]
            port_id1 = key1[1]
            n_id1 = result[key1]
            if n_id == id1 and n_id1 == id:
                result[id, port_id] = (n_id, port_id1)

    result1 = {}
    for key in result:
        id = key[0]
        port_id = key[1]
        n_id = result[key][0]
        port_id1 = result[key][1]
        if len(result[key]) != 2:
            pass
        else:
            result1[id, port_id] = (n_id, port_id1)

    return result1