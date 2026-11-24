from getpass import getpass
from netmiko import ConnectorHandler
import ipv4_check
import os


device = {
    "device_type": "cisco_ios",
    "host": {ipv4_check},#any ip address that needs to be used
    "username":os.environ["NET_USER"],
    "password":os.environ["NET_PASS"],
    "secret": "enable_secret",
    "port":[22,23]
}

with ConnectorHandler(**device) as conn:
    
    output = conn.send_command("show ip interface brief")
    print(output)

    config_commands =[
        "interface Loopback100",
        "description Configures via Netmiko"
    ]

    config_output = conn.send_config_set(config_commands)
    print(config_output)

    conn.save_config()