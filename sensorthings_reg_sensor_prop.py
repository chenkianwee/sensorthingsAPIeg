import requests
from requests.auth import HTTPBasicAuth

url = 'https://andlchaos300l.princeton.edu:8080/FROST-Server/v1.0/'
auth_user = ''
auth_pass = ''

#========================================================================
#observed property
#========================================================================
observed_prop1 = {"name": "Flow rate",
                 "description": "The fluid flow rate at the point",
                 "definition": "https://en.wikipedia.org/wiki/Volumetric_flow_rate"
                 }

r1 = requests.post(url+"ObservedProperties", 
                  auth=HTTPBasicAuth(auth_user, auth_pass), 
                  json=observed_prop1)

print(r1)

#========================================================================
#sensor
#========================================================================
sensor_data1 = {"name": "Generic Flow Meter",
               "description": "Use this flow meter if unsure of the exact sensor",
               "encodingType": "string",
               "metadata": "generic flow meter"
               }

r1 = requests.post(url+"Sensors", 
                  auth=HTTPBasicAuth(auth_user, auth_pass), 
                  json=sensor_data1)
print(r1)