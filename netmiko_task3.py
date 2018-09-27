from netmiko import ConnectHandler
import sys
import time

cisco_cloud_router = {'device_type': 'cisco_ios',
                      'ip': '10.0.0.5',
                      'username': 'ignw',
                      'password': 'ignw'}
connection = ConnectHandler(**cisco_cloud_router)

config_commands = ['interface loopback 1',
                   'description Internet Device',
                   'ip address 8.8.4.4 255.255.255.255',
                   'no shut']
connection.send_config_set(config_commands)
connection.config_mode()
connection.send_config_set(config_commands)
time.sleep(2)

output = connection.send_command('show interface desc | i Lo1')
if output.count('up') == 2:
    print(config_commands[0] + ' is up!')
else:
    print('You did something wrong, go back and fix it!')
    sys.exit()
print("Moving on to next item...")
config_commands = ['interface Gig2',
                   'desc To ASA Outside',
                   'ip address 203.0.113.1 255.255.255.192',
                   'no shut']
connection.send_config_set(config_commands)
time.sleep(2)

output = connection.send_command('show int desc | i ^Gi2')
if output.count('up') == 2:
    print(config_commands[0] + ' is up!')
else:
    print("It didn't work, try again.")
    sys.exit()

route_commands = ['ip route 10.255.255.2 255.255.255.255 203.0.113.2']
connection.send_config_set(route_commands)
output = connection.send_command('show ip route 10.255.255.2')
if '10.255.255.2' in output:
    print('Route added to routing table.')
elif 'Network not in table' in output:
    print('Route add failed.')
else:
    print('error')
connection.send_command('wr mem')
connection.disconnect()
