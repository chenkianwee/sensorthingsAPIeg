import requests
from requests.auth import HTTPBasicAuth

url = 'https://andlchaos300l.princeton.edu:8080/FROST-Server/v1.0/'
auth_user = ''
auth_pass = ''

#========================================================================
#thing + location
#========================================================================
for i in range(1):
    sid = str(33)
    delete = requests.delete(url+"Things(" + sid + ")", auth=HTTPBasicAuth(auth_user, auth_pass))
    content = delete.content
    print(content)

# delete = requests.delete(url+"Things(53648)", auth=HTTPBasicAuth(auth_user, auth_pass))
# content = delete.content
# print(content)