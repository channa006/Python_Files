from netmiko import ConnectHandler
from getpass import getpass
from datetime import datetime

password = getpass()


def display_output(output):
    print()
    print("#" * 80)
    print("Configure")
    print(output)
    print("#" * 80)
    print()

if __name__ == '__main__':

    password = getpass()
    nxos1 ={
        "host":"nxos1.lasthop.io",
        "username":"pyclass",
        "password":password,
        "device_type":"cisco_nxos",
    }

    nxos2 ={
        "host":"nxos2.lasthop.io",
        "username":"pyclass",
        "password":password,
        "device_type":"cisco_nxos",
    }

    for dev in (nxos1,nxos2):
       net_connect = ConnectHandler(**dev)
       output = net_connect.send_config_from_file("vlans.txt")
       display_output(output)
       net_connect.save_config()
       net_connect.disconnect() 

