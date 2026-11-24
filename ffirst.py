from getpass import getpass
from netmiko import ConnectHandler

# Define device parameters (example uses Cisco ios)
device ={
    "device_type": "cisco_ios",
    "host":"192.168.1.1",
    "username":"admin",
    "password":getpass("Enter SSH password: ")
}

# Connect and execute commands
with ConnectHandler(**device) as conn:
    version_output = conn.send_command("show version")
    print("---SHOW VERSION---")
    print(version_output)

    # Push config changes (handles config mode automatically)
    config_commands = [
        "interface Loopback100",
        "description Configured via Netmiko on macOS",
    ]
    config_output = conn.send_config_set(config_commands)
    print("--CONFIG OUTPUT--")
    print(config_output)

    # Save running-config to startup-config
    conn.save_config()
