import boto3
 
 
client = boto3.client('batch')
 
JOB_NAME = 'test-batch'
JOB_QUEUE = "arn:aws:batch:ap-southeast-1:723575221387:job-queue/batch-run-job-queue"
JOB_DEFINITION = "batch-run-job-definition:9"

response = client.submit_job(
	jobName = JOB_NAME,
	jobQueue = JOB_QUEUE,
	arrayProperties={
        'size': 3
    	},
	jobDefinition = JOB_DEFINITION
)
print(response)
