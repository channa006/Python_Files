from netmiko import ConnectHandler
from getpass import getpass
import os, datetime 
from pprint import pprint
from datetime import datetime

password = getpass()

start_time = datetime.now()

cisco4 = {
    "host":"cisco4.lasthop.io",
    "username":"pyclass",
    "password":password,
    "device_type":"cisco_xe",
    "fast_cli": True,
    }

net_connect = ConnectHandler(**cisco4)
cmd_set=[
"ip name-server 1.1.1.1",
"ip name-server 1.0.0.1",
"ip domain-lookup",
]
output = net_connect.send_config_set(cmd_set)

print()
print("#" * 80)
print("Configure the Device")
print(output)
print("#" * 80)

ping_output = net_connect.send_command("ping google.com")

if "!!" in ping_output:
    print("Ping Successful")
else:
    print("Ping Failed") 

net_connect.disconnect()

end_time = datetime.now()

print("Total Execution Time {}".format(end_time-start_time))

