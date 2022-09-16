from netmiko import ConnectHandler
from getpass import getpass
import os, datetime 
from pprint import pprint

password = getpass()

cisco4 = {
    "host":"cisco4.lasthop.io",
    "username":"pyclass",
    "password":password,
    "device_type":"cisco_xe",
    }

net_connect = ConnectHandler(**cisco4)
cmds = ["show version","show lldp neighbors" ]

output = net_connect.find_prompt()

for cmd in cmds:
    output = net_connect.send_command(cmd,use_textfsm=True)
    print(cmd)
    print('#' * 80)
    print(output)
    print('#' * 80)
    
    if cmd == "show lldp neighbors":
        print("LLDP Data Structure {}".format(type(output)))
        print("HPE Switch Connection Port {}".format(output[0]["neighbor_interface"]))

print()
net_connect.disconnect()
