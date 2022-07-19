import requests
from requests.auth import HTTPBasicAuth

url = 'http://chaosbox.princeton.edu:8080/FROST-Server/v1.0/'
auth_user = ''
auth_pass = ''

#========================================================================
#thing + location
#========================================================================
# foi = {
#         "name": "UofC CCIT",
#         "description": "University of Calgary, CCIT building",
#         "encodingType": "application/vnd.geo+json",
#         "location": {"type": "MultiPoint",
#                      "coordinates": []}
#       }

foi = {"name": "Princeton University",
        "description": "PrincetonUni, projection EPSG:26918",
        "encodingType": "application/vnd.geo+json",
        "location": {"type": "Point",
                    "coordinates": [0, 0, 0]
                    }
        }

'''=============================================================='''
'''for multidatastream with many data in an observation'''
# for i in range(10000):
#     foi['location']['coordinates'].append([-114.133, 51.08, 20+i])
'''=============================================================='''
    
thingloc_data = {"name": "Raspberry Pi",
                  "description": "A Raspberry Pi Gateway",
                  "properties": {"Deployment Condition": "Setup in DormX "},
                  "Locations": [foi]
                  }

# print(foi)
r = requests.post(url+"Things", auth=HTTPBasicAuth(auth_user, auth_pass), 
                  json=thingloc_data, verify=False)
print(r.headers['location'])
# #========================================================================
#observed property
#========================================================================
observed_prop1 = {"name": "Temperature",
                 "description": "The temperature at the position",
                 "definition": "https://en.wikipedia.org/wiki/Celsius"
                 }

observed_prop2 = {"name": "Illuminance",
                 "description": "The illuminance at the position",
                 "definition": "https://en.wikipedia.org/wiki/Illuminance"
                 }


# r1 = requests.post(url+"ObservedProperties", 
#                   auth=HTTPBasicAuth(auth_user, auth_pass), 
#                   json=observed_prop1)

# print(r1)
# r2 = requests.post(url+"ObservedProperties", 
#                   auth=HTTPBasicAuth(auth_user, auth_pass), 
#                   json=observed_prop2)
# print(r2)

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

# r1 = requests.post(url+"Sensors", 
#                   auth=HTTPBasicAuth(auth_user, auth_pass), 
#                   json=sensor_data1)
# print(r1)

# r2 = requests.post(url+"Sensors", 
#                   auth=HTTPBasicAuth(auth_user, auth_pass), 
#                   json=sensor_data2)
# print(r2)

#========================================================================
#datastream
#========================================================================
datastream_data1 = {"name": "Temperature",
                   "description": "Datastream for Temperature@Dorm X",
                   "observationType": "degrees celsius",
                   "unitOfMeasurement": {"name": "Degrees Celsius",
                                         "symbol": "C",
                                         "definition": "https://en.wikipedia.org/wiki/celsius"
                                         },
                   "Thing":{"@iot.id":1},
                   "ObservedProperty":{"@iot.id":1},
                   "Sensor":{"@iot.id":1}
                   }

datastream_data2 = {"name": "Lighting",
                   "description": "Datastream for Lighting@Dorm X",
                   "observationType": "https://en.wikipedia.org/wiki/Illuminance",
                   "unitOfMeasurement": {"name": "Illuminance",
                                         "symbol": "lux",
                                         "definition": "https://en.wikipedia.org/wiki/Solar_irradiance"
                                         },
                   "Thing":{"@iot.id":1},
                   "ObservedProperty":{"@iot.id":2},
                   "Sensor":{"@iot.id":2}
                   }

# r1 = requests.post(url+"Datastreams", 
#                   auth=HTTPBasicAuth(auth_user, auth_pass), 
#                   json=datastream_data1)
# print(r1)

# r2 = requests.post(url+"Datastreams", 
#                   auth=HTTPBasicAuth(auth_user, auth_pass), 
#                   json=datastream_data2)
# print(r2)

#========================================================================
#observations
#========================================================================
import datetime
import time

# temp = 20
# light = 300
# for cnt in range(5):  
#     utc_dt = datetime.datetime.now(datetime.timezone.utc) # UTC time
#     dt = utc_dt.astimezone() # local time
#     dtstr = dt.strftime('%Y-%m-%dT%H:%M:%S%z')
#     print(dtstr)

#     obs_data1 = {"phenomenonTime": dtstr,
#                 "resultTime" : dtstr,
#                 "result" : temp+cnt,
#                 "Datastream":{"@iot.id":1}
#                 }
    
#     r1 = requests.post(url+"Observations", 
#                       auth=HTTPBasicAuth(auth_user, auth_pass), 
#                       json=obs_data1)
    
#     obs_data2 = {"phenomenonTime": dtstr,
#                 "resultTime" : dtstr,
#                 "result" : light+cnt,
#                 "Datastream":{"@iot.id":2}
#                 }
    
#     r2 = requests.post(url+"Observations", 
#                       auth=HTTPBasicAuth(auth_user, auth_pass), 
#                       json=obs_data2)
    
#     print(r1)
#     print(r2)
#     time.sleep(5)

#========================================================================
#Mdatastream
#========================================================================
uom = {"name": "Watts per Square Meter",
        "symbol": "w/m2",
        "definition": "https://en.wikipedia.org/wiki/Solar_irradiance"}


mdatastream_data = {"name": "Irradiation and Illumination",
                    "description": "MultiDatastream for recording irradiation and illumination.",
                    "observationType": "http://www.opengis.net/def/observationType/OGC-OM/2.0/OM_ComplexObservation",
                    "multiObservationDataTypes":[],
                    "unitOfMeasurements": [],
                    "Thing":{"@iot.id":53506},
                    "ObservedProperties":[],
                    "Sensor":{"@iot.id":1}
                    }
# obstype_ls = []
# uom_ls = []
# obs_prop_ls = []
# for _ in range(10000):
#     obstype_ls.append("http://www.opengis.net/def/observationType/OGC-OM/2.0/OM_Measurement")
#     uom_ls.append(uom)
#     obs_prop_ls.append({"@iot.id":1})
    
# mdatastream_data['multiObservationDataTypes'] = obstype_ls
# mdatastream_data['unitOfMeasurements'] = uom_ls
# mdatastream_data['ObservedProperties'] = obs_prop_ls
    
# r = requests.post(url+"MultiDatastreams", 
#                   auth=HTTPBasicAuth(auth_user, auth_pass), 
#                   json=mdatastream_data)
# print(r)

#========================================================================
#observations for multidatastream
#========================================================================
# arrayobs = [{
#             "components": ["phenomenonTime","resultTime","result"],
#             "dataArray": [["2020-05-25T17:01:00.000Z",
#                             "2020-05-25T17:01:00.000Z"]],
            
#             "dataArray@iot.count": 1,
#             "MultiDatastream": {"@iot.id": 5},
#             }]

# res_list = []
# for i in range(10000):
#     res_list.append(i)

# arrayobs[0]['dataArray'][0].append(res_list)

# r = requests.post(url+"CreateObservations", 
#                   auth=HTTPBasicAuth(auth_user, auth_pass), 
#                   json=arrayobs)
# print(r.text)

