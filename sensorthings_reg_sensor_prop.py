import requests
from requests.auth import HTTPBasicAuth

url = 'https://andlchaos300l.princeton.edu:8080/FROST-Server/v1.0/'
auth_user = ''
auth_pass = ''

#========================================================================
#observed property
#========================================================================
observed_prop1 = {"name": "wind speed",
                 "description": "speed of air movement",
                 "definition": ""
                 }

# r1 = requests.post(url+"ObservedProperties", 
#                   auth=HTTPBasicAuth(auth_user, auth_pass), 
#                   json=observed_prop1)

# print(r1)

#========================================================================
#sensor
#========================================================================
sensor_data1 = {"name": "DS18B20",
                "description": "digital waterproof sensor",
                "encodingType": "url",
                "metadata": "https://www.adafruit.com/product/642"
                }

r1 = requests.post(url+"Sensors", 
                  auth=HTTPBasicAuth(auth_user, auth_pass), 
                  json=sensor_data1)
print(r1)