import requests
from requests.auth import HTTPBasicAuth

# url = 'http://chaosbox.princeton.edu:8080/FROST-Server/v1.0/'
url = 'http://192.168.1.243:8080/FROST-Server/v1.0/'
auth_user = ''
auth_pass = ''
#==========================================================================================================================================================
#Fill in the parameters, #The sensorthings API data model is used (https://developers.sensorup.com/docs/#introduction)
#==========================================================================================================================================================
#THING PARAMETERS
#==========================================================================================================================================================
thing_name = 'test2'
thingDesc = 'describe the thing 1'#describe the deployment
pins = ''#describe the pins connection on the particle device
#==========================================================================================================================================================
#LOCATION PARAMETERS
#==========================================================================================================================================================
locName = 'myhome'
locDesc = 'on the table'
loc_encoding_type = 'application/vnd.geo+json'
#Define the geometry of the location. Geometry types from geojson is accepted. Refer to https://tools.ietf.org/html/rfc7946 for geometry types.
loc_type = 'Point'
coordinates = [0,0,0] #0,0,0 lon/kat/alt is the coordinates of null island, this is just a place holder
#==========================================================================================================================================================
#DATASTREAM PARAMETERS
#==========================================================================================================================================================
ds_name = 'some number'
ds_desc = 'random numbers'
obs_type = 'random generated'
#http://defs.opengis.net/elda-common/ogc-def/resource?uri=http://www.opengis.net/def/observationType/OGC-OM/2.0/&_format=html
ds_uom = {"name": "unitless",
          "symbol": "nil",
          "definition": "define"}
#visit "http://www.qudt.org/qudt/owl/1.0.0/unit/Instances.html" to get the definition

#id of the observed property, go to  http://chaosbox.princeton.edu:8080/FROST-Server/v1.0/ObservedProperties to check the properties availabe and specify the @iot.id
#if properties are not available you will have to register a new property
ds_obs_prop_id = 1
#id of the sensor, go to http://chaosbox.princeton.edu:8080/FROST-Server/v1.0/Sensors to check the sensors availabe and specify the @iot.id
#if sensors are not available you will have to register a new property 
ds_sensor_id = 1

#==========================================================================================================================================================
#FUNCTIONS
#==========================================================================================================================================================
def get_id_from_header(location_str):
    split = location_str.split('/')
    thing = split[-1]
    idx1 = thing.index('(')
    idx2 = thing.index(')')
    thing_id = int(thing[idx1+1:idx2])
    return thing_id

#==========================================================================================================================================================
#THE JSON OBJECTS TO BE POST
#==========================================================================================================================================================
#Parameters that defines the location of the thing    
loc_data = {'name': locName,
            'description': locDesc,
            'encodingType': loc_encoding_type,
            'location': {'type': loc_type,
                         'coordinates': coordinates}}

#Parameters that defines the thing
thingloc_data = {'name': thing_name,
                 'description': thingDesc,
                 'properties': {'pins': pins},
                 'Locations': [loc_data]}

#Parameters that defines the datastream
datastream_data = {'name': ds_name,
              'description': ds_desc,
              'observationType': obs_type,
              'unitOfMeasurement': ds_uom,
              'Thing':{},
              'ObservedProperty':{'@iot.id':ds_obs_prop_id},
              'Sensor':{'@iot.id':ds_sensor_id}
              }
#==========================================================================================================================================================
#==========================================================================================================================================================
is_thing_reg = False
#check if this thing already exist on the database
filter_thing = "Things?$filter=name eq '" + thing_name + "'&$expand=Locations($select=name),Datastreams($select=id),Multidatastreams($select=id)&$select=id"
find_thing = requests.get(url+filter_thing)
thing_content = find_thing.json()
thing_ls = thing_content['value']
print(thing_content)
nthings = len(thing_ls)
if nthings > 0:
    loc_name_val = thing_ls[0]['Locations'][0]['name']
    if loc_name_val == locName:
        is_thing_reg = True
        
if is_thing_reg == False:
    r = requests.post(url+"Things",auth=HTTPBasicAuth(auth_user,auth_pass),
                      json=thingloc_data)
    print(r.text)
    loc_str = r.headers['Location']
    thing_id = get_id_from_header(loc_str)
    
else:
    thing_id = thing_ls[0]['@iot.id']

if len(thing_ls) == 0:
    nmds = 0
    nds = 0
else:
    nmds = len(thing_ls[0]['MultiDatastreams'])
    nds = len(thing_ls[0]['Datastreams'])

if nds == 0:
    datastream_data['Thing'] = {"@iot.id":thing_id}
    dr = requests.post(url+"Datastreams", 
                      auth=HTTPBasicAuth(auth_user,auth_pass),
                      json=datastream_data)
    print('datastream', dr.text)
    ds_loc_str = dr.headers['Location'] 
    ds_id = get_id_from_header(ds_loc_str )
else:
    ds_id = thing_ls[0]['Datastreams'][0]['@iot.id']
    
#==========================================================================================================================================================
print('===============================================================================')
print('Thing ID:', thing_id)
print('Visit this page to look at the registered Device: \n',url+'Things(' + str(thing_id) + ')')
print('Datastream ID:', ds_id)
print('Use this information to post observation in sensorthing_post_observation.py')
print('===============================================================================')