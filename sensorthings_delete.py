import requests
from requests.auth import HTTPBasicAuth

url = ''
auth_user = ''
auth_pass = ''

#========================================================================
#thing + location
#========================================================================
for i in range(8):
    sid = str(i+256)
    delete = requests.delete(url+"Things(" + sid + ")", auth=HTTPBasicAuth(auth_user, auth_pass))
    content = delete.content
    print(content)

# delete = requests.delete(url+"Things(53648)", auth=HTTPBasicAuth(auth_user, auth_pass))
# content = delete.content
# print(content)