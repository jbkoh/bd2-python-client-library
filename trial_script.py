#/usr/bin/python
import pdb
import arrow
from building_depot import DataService, BDError

cse_dataservice_url = 'YOUR_ENDPOINT'
bd_username = 'YOUR_USERNAME'
bd_api_key = 'YOUR_APIKEY'

#Connect with BuildingDepot
ds = DataService(cse_dataservice_url, bd_api_key, bd_username)

query = {
    'room': 'rm-2150', # There are other rooms
    'template': 'Zone Temperature', # There are other template
}
resp = ds.list_sensors(query)
sensors = resp['sensors']
PT = 'US/Pacific'
start_time = arrow.get(2019, 1, 1, tzinfo=PT)
end_time = arrow.get(2019, 1, 6, tzinfo=PT)

for sensor in sensors:
    sensor_srcid = sensor['source_identifier'] # ID used inside BACnet
    sensor_uuid = sensor['uuid'] # ID used in BD
    data = ds.get_timeseries_datapoints(sensor_uuid,
                                        'PresentValue',
                                        str(start_time),
                                        str(end_time),
                                        )
    print(sensor)
    print(data)
