def ipdefine():
    c = ""
    ip = input("Enter ip address:")
    first = int(ip.split(".")[0])
    trueip = False
    iplist = ip.split(".")
    while not trueip:
        if len(iplist) != 4:
            ip = input("enter again:")
            iplist = ip.split(".")
        else:
            trueip = True
    if first >=1 and first <=127:
        c = "A"
        iptype = "unicast"
    elif first >= 128 and first <= 191:
        c = "B"
        iptype = "unicast"
    elif first >= 192 and first <= 223:
        c = "C"
        iptype = "unicast"
    elif first >= 224 and first <= 239:
        c = "D"
        iptype = "multicast"
    else:
        if ip == "0.0.0.0":
            iptype = "unassigned"
        elif ip == "255.255.255.255":
            iptype = "local broadcast"
        else:
            iptype = "unused"
    return c, iptype

def macdefine():
    mac = ['aabb:cc80:7000', 'aabb:dd80:7340', 'aabb:ee80:7000', 'aabb:ff80:7000']
    mac_cisco = []

    for i in mac:
        newmac = i.replace(":", ".")
        mac_cisco.append(newmac)
    return mac_cisco

def trunk_template_config():
    trunk_template = ['switchport trunk encapsulation dot1q',
                      'switchport mode trunk',
                      'switchport trunk allowed vlan']
    fast_int = {'access': {'0/12': '10', '0/14': '11', '0/16': '17', '0/17': '150'},
                'trunk': {'0/1': ['add', '10', '20'],
                          '0/2': ['only', '11', '30'],
                          '0/4': ['del', '17']}}

    for intf, vlan in fast_int["trunk"].items():
        print("interface FastEthernet" + intf)
        for command in trunk_template:
            if command.endswith("allowed vlan"):
                if vlan[0] == "add":
                    print("{} add {}".format(command, " ".join(vlan[1:])))
                elif vlan[0] == "only":
                    print("{} {}".format(command, " ".join(vlan[1:])))
                else:
                    print("{} remove {}".format(command, " ".join(vlan[1:])))
            else:
                print("{}".format(command))

print(ipdefine())
print(macdefine())
print(trunk_template_config())