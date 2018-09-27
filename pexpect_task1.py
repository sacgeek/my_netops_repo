import pexpect
import re

username = 'ignw'
password = 'ignw'
device_ip = '10.0.0.5'

connection = pexpect.spawn(f'ssh {username}@{device_ip}')
connection.expect('Password:')
connection.sendline(password)
#connection.expect('ignw-csr#')
connection.expect('[a-z-]*[#]$')
#print(connection.before)
#print(connection.after)
host = connection.after[:-1]
print(host)
connection.sendline('show run interface g1')
connection.expect('[a-z-]*[#]$')
interface_output = connection.before
#print(interface_output)
split_output = interface_output.decode().split('\r\n')
print(split_output)
interface_desc = 'Not set'
interface_ip = 'Not set'
for a in split_output:
    if a.startswith('interface'):
        interface_name = a[10:]
    elif a.startswith(' ip address'):
        interface_ip = a[12:]
    elif a.startswith(' description '):
        interface_desc = a[13:]
print(interface_name)
print(interface_desc)
print(interface_ip)
