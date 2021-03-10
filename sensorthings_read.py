import requests
from requests.auth import HTTPBasicAuth

url = 'https://andlchaos300l.princeton.edu:8080/FROST-Server/v1.0/'
auth_user = ''
auth_pass = ''

#========================================================================
#thing + location
#========================================================================
# get = requests.get(url+"Things", auth=HTTPBasicAuth(auth_user, auth_pass))
get = requests.get(url+"Things", auth=HTTPBasicAuth(auth_user, auth_pass))
content = get.json()
for thing in content['value']:
    print('=======================================================================================================')
    print('')
    print(thing)