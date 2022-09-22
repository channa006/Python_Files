from netmiko import ConnectHandler
from getpass import getpass
from datetime import datetime

host_ips = []

def displayoutput(output,hostname):
    print("#" * 80)
    print(output)
    print("#" * 80)
    with open(hostname+".txt","w") as fwrite:
            fwrite.write(output) 
   

with open('hostnames.txt','r') as file:
    for line in file:
        line = line.strip()
        #print(line,end='')
        host_ips.append(line)

print(host_ips)

password = getpass()

for dev in host_ips:
    dev1={
    "host":dev,
    "username":"pyclass",
    "password":password,
    "device_type":"cisco_xe",
    }
    net_connect = ConnectHandler(**dev1)
    hostname = net_connect.find_prompt()
    output = net_connect.send_command('show version')
    displayoutput(output,hostname)


net_connect.disconnect()
