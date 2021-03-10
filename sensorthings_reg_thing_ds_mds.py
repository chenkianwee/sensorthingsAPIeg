import requests
from requests.auth import HTTPBasicAuth

url = 'https://andlchaos300l.princeton.edu:8080/FROST-Server/v1.0/'
auth_user = ''
auth_pass = ''
#==========================================================================================================================================================
#Fill in the parameters, #The sensorthings API data model is used (https://developers.sensorup.com/docs/#introduction)
#==========================================================================================================================================================
#THING PARAMETERS
#==========================================================================================================================================================
thing_name = 'python test5'
thingDesc = 'Describe the thing'#describe the deployment
pins = 'A0-Manifold Return, A1-Manifold Supply'#describe the pins connection on the particle device
#==========================================================================================================================================================
#LOCATION PARAMETERS
#==========================================================================================================================================================
locName = 'Name of location'
locDesc = 'Describe the location'
loc_encoding_type = 'application/vnd.geo+json'
#Define the geometry of the location. Geometry types from geojson is accepted. Refer to https://tools.ietf.org/html/rfc7946 for geometry types.
loc_type = 'Point'
coordinates = [0,0,0] #0,0,0 is the coordinates of null island, this is just a place holder
#==========================================================================================================================================================
#DATASTREAM PARAMETERS
#==========================================================================================================================================================
ds_name = 'python_ds_name'
ds_desc = 'python_ds_description'
obs_type = 'a string to describe the observation the datastream is making' 
#http://defs.opengis.net/elda-common/ogc-def/resource?uri=http://www.opengis.net/def/observationType/OGC-OM/2.0/&_format=html
ds_uom = {"name": "name of Unit of measurement",
          "symbol": "the symbol",
          "definition": "definition of the uom"}
#visit "http://www.qudt.org/qudt/owl/1.0.0/unit/Instances.html" to get the definition
#id of the observed property, go to  http://chaosbox.princeton.edu:8080/FROST-Server/v1.0/ObservedProperties to check the properties availabe and specify the @iot.id
#if properties are not available you will have to register a new property
ds_obs_prop_id = 1
#id of the sensor, go to http://chaosbox.princeton.edu:8080/FROST-Server/v1.0/Sensors to check the sensors availabe and specify the @iot.id
#if sensors are not available you will have to register a new property 
ds_sensor_id = 1 
#==========================================================================================================================================================
#MULTIDATASTREAM PARAMETERS
#==========================================================================================================================================================
mds_name = 'python_mds_name'
mds_desc = 'python mds description'
uom_ls = [{"name": "name of unit of measurement1",
           "symbol": "x1",
           "definition": "definition of the unit of measurement1"},
          {"name": "name of unit of measurement2",
           "symbol": "x2",
           "definition": "definition of the unit of measurement2"}
          ]
#id of the observed property, go to  http://chaosbox.princeton.edu:8080/FROST-Server/v1.0/ObservedProperties to check the properties availabe and specify the @iot.id
#if properties are not available you will have to register a new property
mds_obs_properties_id = [{'@iot.id':1}, {'@iot.id':1}]
#id of the sensor, go to http://chaosbox.princeton.edu:8080/FROST-Server/v1.0/Sensors to check the sensors availabe and specify the @iot.id
#if sensors are not available you will have to register a new property
mds_sensor_id = 1
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

#parameters for the multidatastream
mdatastream_data = {'name': mds_name,
                    'description': mds_desc,
                    'observationType': 'http://www.opengis.net/def/observationType/OGC-OM/2.0/OM_ComplexObservation',
                    'multiObservationDataTypes':['http://www.opengis.net/def/observationType/OGC-OM/2.0/OM_Measurement', 
                                                 'http://www.opengis.net/def/observationType/OGC-OM/2.0/OM_Measurement'],
                    'unitOfMeasurements': uom_ls,
                    'Thing':{},
                    'ObservedProperties':mds_obs_properties_id,
                    'Sensor':{"@iot.id":mds_sensor_id}
                    }
#==========================================================================================================================================================
#==========================================================================================================================================================
is_thing_reg = False
#check if this thing already exist on the database
filter_thing = "Things?$filter=name eq '" + thing_name + "' and description eq '" + thingDesc + "'&$expand=Locations($select=name),Datastreams($select=id),Multidatastreams($select=id)&$select=id"
find_thing = requests.get(url+filter_thing)
thing_content = find_thing.json()
thing_ls = thing_content['value']
nthings = len(thing_ls)
if nthings > 0:
    loc_name_val = thing_ls[0]['Locations'][0]['name']
    if loc_name_val == locName:
        is_thing_reg = True
        
if is_thing_reg == False:
    r = requests.post(url+"Things",auth=HTTPBasicAuth(auth_user,auth_pass),
                      json=thingloc_data)
    
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
    ds_loc_str = dr.headers['Location'] 
    ds_id = get_id_from_header(ds_loc_str )
else:
    ds_id = thing_ls[0]['Datastreams'][0]['@iot.id']

if nmds == 0:
    mdatastream_data['Thing'] = {"@iot.id":thing_id}
    mr = requests.post(url+"MultiDatastreams", 
                      auth=HTTPBasicAuth(auth_user,auth_pass),
                      json=mdatastream_data)
    
    mds_loc_str = mr.headers['Location'] 
    mds_id = get_id_from_header(mds_loc_str )
else:
    mds_id = thing_ls[0]['MultiDatastreams'][0]['@iot.id']
    
#==========================================================================================================================================================
print('===============================================================================')
print('Thing ID:', thing_id)
print('Visit this page to look at the registered Device: \n',url+'Things(' + str(thing_id) + ')')
print('Datastream ID:', ds_id)
print('MultiDatastream ID:', mds_id)
print('Use this information to post observation in sensorthing_post_observation.py')
print('===============================================================================')