from __future__ import print_function
import boto3
import json
import argparse
import random
import time
import datetime
import logging

_TOPIC = "connectedcar/topic"
_WAIT = 5

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

#----------------------------------------------------------
def argCheck():
    logging.info("start argCheck")
    argDict = {}
#    parser.add_argument("--device_name", required = True,
#            help = "[MUST] --device_name [dummy device name]")
    parser.add_argument("--region", required = True,
            help = "[MUST] --region (e.g.:us-west-2")

    args = parser.parse_args()
#    argDict['device_name'] = args.device_name
    argDict['region'] = args.region

    return argDict
#----------------------------------------------------------
def dummyData():
    logging.info("start dummyData")
    try:
#        now = datetime.datetime.now().strftime('%Y-%m-%dT%H:%M:%S')
#        val = random.randint(0, 100)

        resJson = {
		"vin": "VUORU37MWGQ211111",
		"trip_id": "1cc1258c-de1a-4c69-8fa9-5f1994311111",
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

        return resJson
    except Exception as e:
        logging.error("Error on dummyData()")
        raise e
#----------------------------------------------------------
if __name__ == '__main__':
    logging.info("start main")
    try:
        parser = argparse.ArgumentParser()
        argDict = argCheck()

#        devicename = argDict['device_name']
        topic = _TOPIC

        IoT = boto3.client('iot-data', region_name = argDict['region'])
        while True:
            jsonPayload = dummyData()
            print(jsonPayload)
            logging.debug("send data:{}".format(json.dumps(jsonPayload)))
            IoT.publish(
                topic = topic,
                qos = 1,
                payload = json.dumps(jsonPayload)
            )
            time.sleep(_WAIT)

    except Exception as e:
        logging.error("Error on main()")
        logging.error(e.message)
