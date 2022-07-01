import requests
from requests.auth import HTTPBasicAuth

url = 'https://andlchaos300l.princeton.edu:8080/FROST-Server/v1.0/Datastreams'
#id of the datastream you want to query

# Interior boards 
# BO001 rel humidity = 432
# X07 rel humidity = 437
# X08 rel humidity = 442

idx = '432'
r = requests.get(url + '(' + idx +  ')' + "/Observations?$filter=phenomenonTime ge 2021-12-09T00:00:00Z&$select=result,phenomenonTime")
json_data = r.json()
print(json_data)