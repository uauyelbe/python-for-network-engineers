ip = input("Enter ip address and prefix:")
slash = ip.index("/")
def ipbin():
    ipaddr = ip[:slash]
    print(ipaddr)
    s = ipaddr.split(".")
    sp = ""
    ipt = ""
    iptemplate = """{:15}"""
    bintemplate = """{:15}"""
    for i in s:
        sp = sp + iptemplate.format(i) + " "
        ipt = ipt + bintemplate.format(bin(int(i))) + " "
    print("network:")
    return sp + "\n" + ipt

def macbin():
    mask = int(ip[slash+1:])
    print("mask:")
    c = 1
    m = 0
    m1 = m2 = m3 = m4 = 255
    if mask == 32:
        m4 = 255
    else:
        if mask <= 32 and mask >= 24:
            for i in range(31, mask - 1, -1):
                m4 = m4 - c
                c = c * 2
            print(m4)
        elif mask < 24 and mask >= 16:
            m4 = 0
            for i in range(23, mask - 1, -1):
                m3 = m3 - c
                c = c * 2
        elif mask < 16 and mask >= 8:
            m3 = m4 = 0
            for i in range(15, mask - 1, -1):
                m2 = m2 - c
                c = c * 2
        else:
            m2 = m3 = m4 = 0
            for i in range(7, mask - 1, -1):
                m4 = m4 - c
                c = c * 2
    return "{}{:15}{:15}{:15}".format(m1, m2, m3, m4) + "\n" + "{:15}{:15}{:15}{:15}".format(str(bin(m1)), str(bin(m2)),
                                                                                             str(bin(m3)), str(bin(m4)))

def devinfo():
    london_co = {
        'r1': {
            'location': '21 New Globe Walk',
            'vendor': 'Cisco',
            'model': '4451',
            'ios': '15.4',
            'ip': '10.255.0.1'
        },
        'r2': {
            'location': '21 New Globe Walk',
            'vendor': 'Cisco',
            'model': '4451',
            'ios': '15.4',
            'ip': '10.255.0.2'
        },
        'sw1': {
            'location': '21 New Globe Walk',
            'vendor': 'Cisco',
            'model': '3850',
            'ios': '3.6.XE',
            'ip': '10.255.0.101',
            'vlans': '10,20,30',
            'routing': True
        }
    }

    dev = input("enter device name:")
    param = input("enter device parameters(ios, model, vendor, location, ip):").lower()

    return london_co[dev][param]

def template():
    porttype = input("enter port type:")
    portname = input("enter port name:")

    access_template = ['switchport mode access',
                       'switchport access vlan {}',
                       'switchport nonegotiate',
                       'spanning-tree portfast',
                       'spanning-tree bpduguard enable']
    trunk_template = ['switchport trunk encapsulation dot1q',
                      'switchport mode trunk',
                      'switchport trunk allowed vlan {}']

    interface = "interface {}".format(portname)

    if porttype == "access":
        vlan = input("Enter VLAN number:")
        tmp = interface + "\n" + "\n".join(access_template).format(vlan)
    else:
        vlan = input("Enter allowed VLANs:")
        tmp = interface + "\n" + "\n".join(trunk_template).format(vlan)

    return tmp

def lastindex():
    num_list = [10, 2, 30, 100, 10, 50, 11, 30, 15, 7]
    word_list = ['python', 'ruby', 'perl', 'ruby', 'perl', 'python', 'ruby', 'perl']
    element = int(input("enter number for num_list:"))
    element_word = input("enter word for word_list:")
    item = 0
    item2 = ""
    for i in range(len(num_list)-1,-1,-1):
        if element == num_list[i]:
            item = i
            break

    for j in range(len(word_list)-1,-1,-1):
        if element_word == word_list[j]:
            item2 = j
            break

    return item, item2

print(ipbin())
print(macbin())
print(devinfo())
print(template())
print(lastindex())