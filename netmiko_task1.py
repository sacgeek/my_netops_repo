from netmiko import ConnectHandler
import re

cisco_cloud_router = {'device_type': 'cisco_ios',
                      'ip': '10.0.0.5',
                      'username': 'ignw',
                      'password': 'ignw'}
connection = ConnectHandler(**cisco_cloud_router)

#print(connection)
#print(type(connection))
#output = connection.send_command("show run interface g1")
#print(output)
hostname = 'N/A'
interface_name = 'N/A'
interface_desc = 'N/A'
interface_ip = 'N/A'
primary_ip = 'N/A'
secondary_ip = 'N/A'
hostname = connection.find_prompt()
print(hostname[:-1])
interface_name = connection.send_command('show run int g1 | i ^interface')[10:]
print(interface_name)
interface_desc = connection.send_command('show run int g1 | i ^ description')[13:]
print(interface_desc)
interface_ip = connection.send_command('show run int g1 | i ^ ip address')
#primary_ip = re.search('^ ip address \b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b \b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b$', interface_ip)
#secondary_ip = re.search('^ ip address \b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b \b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b secondary', interface_ip)
#print(primary_ip)
#print(secondary_ip)
#sii_split = interface_ip.split()
print(interface_ip)
#second_int_ip = connection.send_command('show run int g1 | i ^ ip address')
#sii_split = second_int_ip.split()
print(sii_split)
connection.disconnect()
