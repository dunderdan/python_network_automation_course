#!/usr/bin/env python
"""
1. In the lab environment use Netmiko to connect to one of the Cisco NX-OS devices. 
You can find the IP addresses and username/passwords of the Cisco devices in the 
'Lab Environment' email or alternatively in the ~/.netmiko.yml file. Simply print the 
router prompt back from this device to verify you are connecting to the device properly.
"""
from netmiko import ConnectHandler
from getpass import getpass


nx_device = {
    'host': 'nxos2.lasthop.io',
    'username': 'pyclass',
    'password': getpass(),
    'device_type': 'cisco_nxos',
}

net_connect = ConnectHandler(**nx_device)
print(net_connect.find_prompt())
net_connect.disconnect()

