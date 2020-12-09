import requests
from requests.auth import HTTPBasicAuth

url = ''
auth_user = ''
auth_pass = ''


things_json = {'description': 'changed2'}

r = requests.patch(url+"Things(53610)", auth=HTTPBasicAuth(auth_user, auth_pass), 
                  json=things_json, verify=False)

print(r.headers)