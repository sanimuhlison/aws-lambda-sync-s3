# aws-lambda-sync-s3

AWS Lambda function to sync object from `bucket source` to `bucket destination` once object successfully uploaded.

## Requirements
- **Set Lambda Triggers:** 
	- AWS S3 Bucket Source
- **Allow Lambda to Access:** 
	- s3:GetObject
	- ssm:GetParameter
	- kms:Decrypt
	- logs:PutLogEvents
	- logs:CreateLogStream
- **AWS SSM Parameters:**
```
/aws-lambda-sync-s3/AWS_ACCESS_KEY_ID
/aws-lambda-sync-s3/AWS_SECRET_ACCESS_KEY
```
- **AWS KEY**:
	- AWS_ACCESS_KEY_ID Destination
	- AWS_SECRET_ACCESS_KEY Destination
	- Then put those keys to AWS SSM Parameter above
