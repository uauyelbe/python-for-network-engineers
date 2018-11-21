from sys import argv
from operator import itemgetter

def ospffromtext():
    with open("ospf.txt", "r") as ospf:
        ospf_route = ospf.read().split()
        template = """
                            Protocol: OSPF
                            Prefix: {}
                            AD/Metric: {}
                            Next-Hop: {}
                            Last update {}
                            Outbound Interface {}
                            """.format(ospf_route[1], ospf_route[2], ospf_route[4], ospf_route[5], ospf_route[6])
        return template

def swconfig():
    with open("config_sw1.txt", "r") as sw:
        ignore = ['duplex', 'alias', 'Current configuration']
        f = sw.readlines()
        with open("config_sw1_output.txt", "a") as out:
            for i in f:
                if not i.startswith("!") and len(i.strip()) != 0 and not any(s in i for s in ignore):
                    out.write(i.strip() + "\n")
    return

def camtable():
    with open("cam_table.txt", "r") as cam:
        f = cam.readlines()
        a = []
        with open("cam_table_output.txt", "a") as out:
            for i in f:
                if "DYNAMIC" in i:
                    a.append(i.replace("DYNAMIC", "").strip().split())
                    s = i.replace("DYNAMIC", "").strip().split()
            out.write(str(sorted(a)))
    return sorted(a)

print(ospffromtext())
print(swconfig())
print(camtable())