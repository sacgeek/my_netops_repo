import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
import json

url = 'https://10.0.0.8/api/'
username = 'ignw'
password = 'ignw'

resp = requests.get(f'{url}objects/networkobjects', auth=(username, password), verify=False)
print(resp)
print(resp.status_code)
#print(dir(resp))
#print(resp.text)
resp = requests.get(f'{url}interfaces/physical', auth=(username, password), verify=False)
print(resp)
#print(resp.text)

resp_dict = json.loads(resp.text)
#print(resp_dict)

int_qty = resp_dict['rangeInfo']['total']
int_names = []
for x in resp_dict['items']:
    int_names.append(x['hardwareID'])

print(f"The ASAv has {int_qty} interfaces, named as follows: ")
print(int_names)
