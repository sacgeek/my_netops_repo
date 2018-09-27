from netmiko import ConnectHandler

cisco_cloud_router = {'device_type': 'cisco_ios',
                      'ip': '10.0.0.5',
                      'username': 'ignw',
                      'password': 'ignw'}
connection = ConnectHandler(**cisco_cloud_router)

config_commands = ['interface loopback 0', 'description I made this in Python!', 'ip address 172.16.1.1 255.255.255.255']
connection.send_config_set(config_commands)

print(connection.send_command('show run int loopback0'))

print(connection.send_command('show interface desc | i Lo0'))
#print(output)
connection.disconnect()
