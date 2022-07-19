import requests
from requests.auth import HTTPBasicAuth

url = 'https://andlchaos300l.princeton.edu:8080/FROST-Server/v1.0/'
auth_user = ''
auth_pass = ''

#========================================================================
#thing + location
#========================================================================
obj = "Things"
idx = "104"
delete = requests.delete(url+ obj + "(" + idx + ")", auth=HTTPBasicAuth(auth_user, auth_pass))
content = delete.content
print(content)