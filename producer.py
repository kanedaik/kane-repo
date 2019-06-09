import boto3
 
response = boto3.client('kinesis')

for i in range(100):
    response.put_record(
        StreamName = "api_gateway_stream",
        Data = "test",
        PartitionKey = "test",
    )

#print(StreamName, Data, PartitionKey)
