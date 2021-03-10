import requests
from requests.auth import HTTPBasicAuth

url = 'https://andlchaos300l.princeton.edu:8080/FROST-Server/v1.0/'
auth_user = ''
auth_pass = ''

obj = "Datastreams"
idx = "14"
ds_json = {"unitOfMeasurement": {
                                    "name": "g/kg",
                                    "symbol": "g/kg",
                                    "definition": "the amount of grams in a kg of air"
                                }
            }
r = requests.patch(url+ obj + "(" + idx +  ")", auth=HTTPBasicAuth(auth_user, auth_pass), 
                  json=ds_json, verify=True)
print(r.text)