import subprocess
import ipaddress
from tabulate import tabulate
import re

ipaddr = "95.59.170.0-95.59.170.5"


def check_ip_address(ip):
    reachable = []
    unreachable = []
    for ipadr in ip:
        reply = subprocess.run(["ping", str(ipadr)], stdout=subprocess.DEVNULL)
        if reply.returncode == 0:
            reachable.append(str(ipadr))
        else:
            unreachable.append(str(ipadr))
    return reachable


def iprange():
    l = []
    iplist = ipaddr.split("-")
    newip = iplist[0]
    while str(newip) != iplist[-1]:
        newip = ipaddress.ip_address(newip) + 1
        l.append(str(newip))
    return l


a = iprange()
print(a)
columns = ["Reachable"]
numbers = [1, 2, 3, 4, 5]
print(tabulate([check_ip_address(a), numbers], headers=columns, tablefmt="pipe"))