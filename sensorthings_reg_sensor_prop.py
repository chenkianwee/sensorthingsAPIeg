import requests
from requests.auth import HTTPBasicAuth

url = ''
auth_user = ''
auth_pass = ''

#========================================================================
#observed property
#========================================================================
observed_prop1 = {"name": "Temperature",
                 "description": "The temperature at the position",
                 "definition": "https://en.wikipedia.org/wiki/Celsius"
                 }

r1 = requests.post(url+"ObservedProperties", 
                  auth=HTTPBasicAuth(auth_user, auth_pass), 
                  json=observed_prop1)

print(r1)

#========================================================================
#sensor
#========================================================================
sensor_data1 = {"name": "Temp Sensor1",
               "description": "Description of the Sensor Hardware",
               "encodingType": "Application/pdf",
               "metadata": "https://cdn-shop.adafruit.com/datasheets/DHT22.pdf"
               }   

sensor_data2 = {"name": "Light Sensor1",
               "description": "Description of the Sensor Hardware",
               "encodingType": "Application/pdf",
               "metadata": "https://cdn-shop.adafruit.com/datasheets/DHT22.pdf"
               }   

r1 = requests.post(url+"Sensors", 
                  auth=HTTPBasicAuth(auth_user, auth_pass), 
                  json=sensor_data1)
print(r1)