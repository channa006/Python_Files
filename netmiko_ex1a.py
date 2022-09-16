from netmiko import ConnectHandler
from getpass import getpass
import os

password = getpass()

device1={
    "host":"cisco4.lasthop.io",
    "username":"pyclass",
    "password":password,
    "device_type":"cisco_xe"
    }

net_connect = ConnectHandler(**device1)

output = net_connect.send_command_timing(
    "ping", strip_prompt=False, strip_command=False)

output += net_connect.send_command_timing("\n",strip_prompt = False,strip_command=False)
output += net_connect.send_command_timing("8.8.8.8",strip_prompt = False,strip_command=False)
output += net_connect.send_command_timing("\n",strip_prompt = False,strip_command=False)
output += net_connect.send_command_timing("\n",strip_prompt = False,strip_command=False)
output += net_connect.send_command_timing("\n",strip_prompt = False,strip_command=False)
output += net_connect.send_command_timing("\n",strip_prompt = False,strip_command=False)
output = net_connect.send_command_timing("\n",strip_prompt = False,strip_command=False)

net_connect.disconnect()
print()
print(output)
print()
