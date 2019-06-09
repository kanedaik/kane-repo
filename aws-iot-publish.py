# coding: utf-8

import json
import boto3

iot = boto3.client('iot-data')
    
topic = 'connectedcar/trip'
payload = {
	"vin": "VUORU37MWGQ222222",
	"trip_id": "1cc1258c-de1a-4c69-8fa9-5f1994322222",
	"accelerator_pedal_position_mean": "12.163340271375452",
	"brake_mean": "11.953352769679302",
	"brake_pedal_status": "false",
	"engine_speed_mean": "3087.098346153109",
	"fuel_consumed_since_restart": "0.1562595469735892",
	"fuel_level": "99.67757825756603",
	"high_acceleration_event": "7",
	"high_braking_event": "0",
	"high_speed_duration": "138450",
	"idle_duration": "2760329",
	"ignition_status": "off",
	"latitude": "38.954946",
	"longitude": "-77.384727",
	"name": "aggregated_telemetrics",
	"odometer": "15.094381874211349",
	"oil_temp_mean": "203.76931245431606",
	"start_time": "2018-10-05T06:20:33.243Z",
	"timestamp": "2018-10-05 07:13:34.775000000"
}
    
try:
    iot.publish(
        topic=topic,
        qos=0,
        payload=json.dumps(payload)
    )

    print("Succeeeded.")
    
except Exception as e:
    print(e)
    print("Failed.")
