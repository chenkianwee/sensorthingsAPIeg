import requests
from requests.auth import HTTPBasicAuth

url = 'https://andlchaos300l.princeton.edu:8080/FROST-Server/v1.0/'
auth_user = ''
auth_pass = ''
#==========================================================================================================================================================
#Fill in the parameters, #The sensorthings API data model is used (https://developers.sensorup.com/docs/#introduction)
#==========================================================================================================================================================
#DATASTREAM PARAMETERS
#==========================================================================================================================================================
thing_id = 28
ds_name = 'Arg024_rel_humidity'
ds_desc = 'relative humidity reading from scd30'
obs_type = '"http://www.opengis.net/def/observationType/OGC-OM/2.0/OM_Measurement' 
#http://defs.opengis.net/elda-common/ogc-def/resource?uri=http://www.opengis.net/def/observationType/OGC-OM/2.0/&_format=html
ds_uom = {"name": "percentage",
          "symbol": "%",
          "definition": "relative humidity in percentage"}
#visit "http://www.qudt.org/qudt/owl/1.0.0/unit/Instances.html" to get the definition
#id of the observed property, go to  http://chaosbox.princeton.edu:8080/FROST-Server/v1.0/ObservedProperties to check the properties availabe and specify the @iot.id
#if properties are not available you will have to register a new property
ds_obs_prop_id = 3
#id of the sensor, go to http://chaosbox.princeton.edu:8080/FROST-Server/v1.0/Sensors to check the sensors availabe and specify the @iot.id
#if sensors are not available you will have to register a new property 
ds_sensor_id = 5
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
#Parameters that defines the datastream
datastream_data = {'name': ds_name,
                  'description': ds_desc,
                  'observationType': obs_type,
                  'unitOfMeasurement': ds_uom,
                  'Thing':{"@iot.id":thing_id},
                  'ObservedProperty':{'@iot.id':ds_obs_prop_id},
                  'Sensor':{'@iot.id':ds_sensor_id}
                  }

#==========================================================================================================================================================
#==========================================================================================================================================================
is_ds_reg = False
#check if this thing already exist on the database
filter_ds = "Datastreams?$filter=name eq '" + ds_name + "' and description eq '" + ds_desc + "'&$select=id"
find_ds = requests.get(url+filter_ds)
ds_content = find_ds.json()
ds_ls = ds_content['value']
nds = len(ds_ls)
if nds > 0:
    is_thing_reg = True
        
if is_ds_reg == False:
    r = requests.post(url+"Datastreams",auth=HTTPBasicAuth(auth_user,auth_pass),
                      json=datastream_data)
    print(r.headers)
    loc_str = r.headers['Location']
    ds_id = get_id_from_header(loc_str)
    

#==========================================================================================================================================================
print('===============================================================================')
print('Datastream ID:', ds_id)
print('Visit this page to look at the registered Device: \n',url+'Datastreams(' + str(ds_id) + ')')
print('Use this information to post observation in sensorthing_post_observation.py')
print('===============================================================================')