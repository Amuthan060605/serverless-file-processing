import json
import boto3

sns = boto3.client('sns')

SNS_TOPIC_ARN = "YOUR_SNS_TOPIC_ARN"


def lambda_handler(event, context):

    print("Received S3 event:")
    print(json.dumps(event))

    bucket_name = event['Records'][0]['s3']['bucket']['name']
    file_name = event['Records'][0]['s3']['object']['key']

    print("Bucket:", bucket_name)
    print("File:", file_name)

    message = f"""
File uploaded successfully!

Bucket: {bucket_name}
File: {file_name}

Lambda processed the uploaded file.
"""

    sns.publish(
        TopicArn=SNS_TOPIC_ARN,
        Subject="S3 File Processing Notification",
        Message=message
    )

    print("SNS notification sent.")

    return {
        'statusCode': 200,
        'body': json.dumps('File processed successfully!')
    }
