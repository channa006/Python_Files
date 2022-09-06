from netmiko import ConnectHandler
from getpass import getpass

device1 = {
    "host":"cisco3.lasthop.io",
    "username":"pyclass",
    "password":getpass(),
    "device_type":"cisco_xe"
    }

net_connect = ConnectHandler(**device1)

print(net_connect.find_prompt())

output = net_connect.send_command('show ip int brief')
#print(output)

with open('showversion.txt','w') as f:
    f.write(output)
