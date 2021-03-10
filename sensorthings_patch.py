import requests
from requests.auth import HTTPBasicAuth

url = 'https://andlchaos300l.princeton.edu:8080/FROST-Server/v1.0/'
auth_user = ''
auth_pass = ''


things_json = {'description': 'changed2'}

ds_json = {"unitOfMeasurement": {
                                    "name": "g/kg",
                                    "symbol": "g/kg",
                                    "definition": "the amount of grams in a kg of air"
                                }
            }


r = requests.patch(url+"Datastreams(14)", auth=HTTPBasicAuth(auth_user, auth_pass), 
                  json=ds_json, verify=True)

print(r.text)