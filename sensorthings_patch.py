import requests
from requests.auth import HTTPBasicAuth

url = 'https://andlchaos300l.princeton.edu:8080/FROST-Server/v1.0/'
auth_user = ''
auth_pass = ''

obj = 'Datastreams'
idx = '29'
ds_json = {'name': 'A003_co2'}
r = requests.patch(url+ obj + '(' + idx +  ')', auth=HTTPBasicAuth(auth_user, auth_pass), 
                  json=ds_json, verify=True)
