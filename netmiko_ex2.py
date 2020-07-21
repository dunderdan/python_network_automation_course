#!/usr/bin/env python
"""
2. Add a second NX-OS device to your first exercise. Make sure you are using dictionaries 
to represent the two NX-OS devices. Additionally, use a for-loop to accomplish the 
Netmiko connection creation. Once again print the prompt back from the devices that 
you connected to.
"""
from netmiko import ConnectHandler
from getpass import getpass


# Get the password so not prompted twice when logging into devices. Assumes common password
password = getpass()

nx_device1 = {
    "device_type": "cisco_nxos",
    "host": "nxos1.lasthop.io",
    "username": "pyclass",
    "password": password,
}

nx_device2 = {
    "device_type": "cisco_nxos",
    "host": "nxos2.lasthop.io",
    "username": "pyclass",
    "password": password,
}

for device in (nx_device1, nx_device2):
    net_connect = ConnectHandler(**device)
    print(net_connect.find_prompt())
    net_connect.disconnect()
