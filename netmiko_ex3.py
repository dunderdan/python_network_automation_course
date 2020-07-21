#!/usr/bin/env python
"""
3. For one of the Cisco IOS devices, use Netmiko and the send_command() method to retrieve 'show version'. Save this output to a file in the current working directory.
"""
from netmiko import ConnectHandler
from getpass import getpass


device = {
    "device_type": "cisco_ios",
    "host": "cisco3.lasthop.io",
    "username": "pyclass",
    "password": getpass(),
}

net_connect = ConnectHandler(**device)
output = net_connect.send_command('show version')
print(output)

net_connect.disconnect()
