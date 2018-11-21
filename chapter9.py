"""
def access_port(access, psec=False):
    access_template = ['switchport mode access',
                       'switchport access vlan',
                       'switchport nonegotiate',
                       'spanning-tree portfast',
                       'spanning-tree bpduguard enable']

    port_security = ['switchport port-security maximum 2',
                     'switchport port-security violation restrict',
                     'switchport port-security']

    result = {}

    if psec:
        access_template = access_template + port_security

    for port, vlan in access.items():
        l = []
        for command in access_template:
            if "access vlan" in command:
                a = command + " " + str(vlan)
                l.append(a)
            else:
                l.append(command)
        result[port] = l
    return result

def trunk_port(trunk):
    trunk_template = ['switchport trunk encapsulation dot1q',
                      'switchport mode trunk',
                      'switchport trunk native vlan 999',
                      'switchport trunk allowed vlan']

    result = {}

    for port, vlan in trunk.items():
        l = []
        for command in trunk_template:
            if "allowed vlan" in command:
                v = [str(s) for s in vlan]
                a = command + " " + " ".join(v)
                l.append(a)
            else:
                l.append(command)
        result[port] = l
    return result
"""

from sys import argv

def get_int_vlan_map(argv):
    with open(argv[1]) as vmap:
        f = vmap.readlines()
        result = {}
        index = 0
        for line in f:
            a = line.split()
            if line.startswith(" switchport trunk allowed vlan"):
                result[f[index-4].strip()] = a[-1]
            index += 1
    return result

access_dict = { 'FastEthernet0/12':10,
'FastEthernet0/14':11,
'FastEthernet0/16':17,
'FastEthernet0/17':150 }

trunk_dict = { 'FastEthernet0/1':[10,20,30],
'FastEthernet0/2':[11,30],
'FastEthernet0/4':[17] }

#print(access_port(access_dict))
#print(trunk_port(trunk_dict))
print(get_int_vlan_map(argv))