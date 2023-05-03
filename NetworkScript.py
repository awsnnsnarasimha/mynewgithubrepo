#### Python Script using netmiko to run command in cisco ios####

import netmiko
connection= netmiko.ConnectHandler(ip="172.16.6.254", device_type="cisco_ios", username="admin", password="Bscl@789")

print(connection.send_command("show ip int br"))
print(connection.send_command("show ip route"))
connection.disconnect()



