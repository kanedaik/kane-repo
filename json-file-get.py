import json
import boto3
import decimal
from datetime import datetime

s3 = boto3.resource('s3')
client = s3.meta.client

response = client.get_object(Bucket='json-file-get', Key='annotation.json')
body = response['Body'].read()
print(body.decode('utf-8'))

current_time = datetime.now().strftime("%Y%m%d %H:%M:%S")

json_dict = json.loads(body, parse_float = decimal.Decimal)
frame_id = json_dict['frame_id']
bounding_box = json_dict['bounding_box']

print(current_time, frame_id, bounding_box)

dynamodb = boto3.resource('dynamodb', region_name='ap-southeast-1')
table = dynamodb.Table('Image_Annotation_DB')

query_response = table.put_item(
	Item={
		'Current_time': current_time,
		'Frame_id': frame_id,
		'Boundign_box': bounding_box
	}
)

print(query_response)
	
