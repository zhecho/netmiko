from netmiko import ConnectHandler
from netmiko.cisco.cisco_ios import CiscoIosSSH


def write_channel(self, *args, **kwargs):
    print("Hello write_channel")


def read_channel(self, *args, **kwargs):
    print("Hello read_channel")


mock_methods = {"write_channel": write_channel, "read_channel": read_channel}


def ClassFactory(BaseClass):
    return type("MockNetmiko", (BaseClass,), mock_methods)


# DynamicClass = ConnectHandler(host='cisco1.lasthop.ip', username='admin', password='foo', device_type='cisco_ios', mock=True)

# MockNetmiko = type("MockNetmiko", (CiscoIosSSH,), mock_methods)
# a = MockNetmiko(host='cisco1.lasthop.io', username='pyclass', password='88newclass', device_type='cisco_ios', mock=True)
