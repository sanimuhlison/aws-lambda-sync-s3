import boto3
import logging

logger = logging.Logger('catch_all')
ssm = boto3.client('ssm')


def lambda_handler(event, context):
	s3_source = boto3.client('s3')
	s3_destination = boto3.client(
		's3',
		aws_access_key_id=get_ssm_value('/aws-lambda-sync-s3/AWS_ACCESS_KEY_ID'),
		aws_secret_access_key=get_ssm_value('/aws-lambda-sync-s3/AWS_SECRET_ACCESS_KEY')
	)
	
	bucket_source = event['Records'][0]['s3']['bucket']['name']
	bucket_dest = 'your_destination_bucket_name'
	object_key = event['Records'][0]['s3']['object']['key']

	try:
		print("[START] Sync FROM '"+ bucket_source +"' TO '"+ bucket_dest)
		
		aws_response = s3_source.get_object(
			Bucket=bucket_source,
			Key=object_key
		)

		s3_destination.upload_fileobj(
			aws_response['Body'],
			bucket_dest,
			object_key,
		)
		
		print("[DONE] Sync '"+ object_key +"' Succeeded")
	except Exception as e:
		logger.error("[ERROR] Copy '"+ object_key + "' Failed. Error Messages: "+ str(e))
		
def get_ssm_value(key):
	response = ssm.get_parameter(
    	Name=key,
    	WithDecryption=True
	)
	return response.get("Parameter").get("Value")