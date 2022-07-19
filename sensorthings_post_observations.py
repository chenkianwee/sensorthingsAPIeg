import datetime
import time
import random 

import requests
from requests.auth import HTTPBasicAuth

url = 'http://192.168.1.243:8080/FROST-Server/v1.0/'
auth_user = ''
auth_pass = ''

#==========================================================================================================================================================
#DATASTREAMS ID
#==========================================================================================================================================================
#if you do not have the datastream IDs, run the sensorthings_register.py script to obtain the necessary ids for running this script.
ds_id = 2
mds_id = 21
#==========================================================================================================================================================
#==========================================================================================================================================================
loop = True
obs_data = {'phenomenonTime': '',
            'resultTime': '',
            'result': '',
            'Datastream':{'@iot.id':ds_id}
            }

arrayobs = [{
            'components': ['phenomenonTime','resultTime','result'],
            'dataArray': [['','',[]]],
            'dataArray@iot.count': 1,
            'MultiDatastream': {'@iot.id': mds_id},
            }]

cnt = 0
while loop == True:
    #get the current time
    utc_dt = datetime.datetime.now(datetime.timezone.utc) # UTC time
    dt = utc_dt.astimezone() # local time
    dtstr = dt.strftime('%Y-%m-%dT%H:%M:%S%z')
    print(dtstr)
    
    #post the datastream
    obs_data['phenomenonTime'] = dtstr
    obs_data['resultTime'] = dtstr
    obs_data['result'] = 'hello world'
    
    r1 = requests.post(url+"Observations", 
                      auth=HTTPBasicAuth(auth_user, auth_pass), 
                      json=obs_data)
    print(r1.text)
    # #post the multiobservation
    # res2 = random.random()
    # res3 = random.random()
    # arrayobs[0]['dataArray'][0][0] = dtstr
    # arrayobs[0]['dataArray'][0][1] = dtstr
    # arrayobs[0]['dataArray'][0][2] = [res2, res3]
    
    # # r2 = requests.post(url+"CreateObservations", 
    # #               auth=HTTPBasicAuth(auth_user, auth_pass), 
    # #               json=arrayobs)
    # print(r1.headers)
    # # print(r1.headers['location'])
    # print(r2.text)
    # #make a post every 5s
    time.sleep(5)
    # cnt+=1
    # #to make an infinity loop just remove this line
    # if cnt == 5:
    #     loop = False