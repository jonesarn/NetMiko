from getpass import getpass
from netmiko import ConnectorHandler
import os
import ipaddress

# I want to be build a python script SSHes into a network device
# I want to back up my configs on github and show anychanges to my network in real time
from ipaddress import IPv4Address, AddressValueError

while True:
    try:
        host = str(IPv4Address(input("Device IPv4 address:").strip()))
    except AddressValueError:
        print("Enter a valid IPv4 Address")

