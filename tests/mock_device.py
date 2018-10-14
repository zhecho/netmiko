from netmiko import ConnectHandler
from netmiko.cisco.cisco_ios import CiscoIosSSH


def write_channel(self, *args, **kwargs):
    print("Hello write_channel")


def read_channel(self, *args, **kwargs):
    print("Hello read_channel")


mock_methods = {"write_channel": write_channel, "read_channel": read_channel}


def ClassFactory(BaseClass):
    return type("MockNetmiko", (BaseClass,), mock_methods)
