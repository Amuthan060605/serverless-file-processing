# Serverless File Processing Pipeline

## 📌 Project Overview

This project implements an event-driven serverless file-processing pipeline using AWS services.

When a file is uploaded to an Amazon S3 bucket, an S3 event automatically triggers an AWS Lambda function. The Lambda function processes the uploaded file information and sends an email notification using Amazon SNS.

Amazon CloudWatch is used to monitor Lambda execution logs and detect errors using alarms.

## 🏗️ Architecture

```text
User
  |
  | Upload File
  v
Amazon S3
  |
  | S3 Event
  v
AWS Lambda (Python)
  |
  | Publish Notification
  v
Amazon SNS
  |
  v
Email Notification

AWS CloudWatch
  |
  +-- Lambda Logs
  |
  +-- Error Alarm
```

## ☁️ AWS Services Used

* Amazon S3
* AWS Lambda
* Amazon SNS
* Amazon CloudWatch
* AWS IAM

## ⚙️ How It Works

1. User uploads a file to the S3 bucket.
2. Amazon S3 generates an object-created event.
3. The event automatically triggers the Lambda function.
4. Lambda reads the S3 bucket and file information.
5. Lambda publishes a message to the SNS topic.
6. SNS sends an email notification.
7. CloudWatch records Lambda execution logs.
8. CloudWatch alarm monitors Lambda errors.

## 🐍 Lambda Function

The Lambda function is written in Python using the AWS SDK for Python (Boto3).

The function extracts:

* S3 bucket name
* Uploaded file name
* S3 event information

It then publishes a notification through SNS.

## 📊 Monitoring

Amazon CloudWatch is used for:

* Lambda execution logs
* Error monitoring
* Alarm configuration
* Debugging

## 🧪 Testing

The project was tested by uploading files such as:

```text
test.txt
document.pdf
```

After uploading a file:

```text
S3 → Lambda → SNS → Email
```

The Lambda execution can also be verified through CloudWatch Logs.

## 📸 Project Screenshots

### S3 Bucket

![S3 Bucket](screenshots/s3-bucket.png)

### Lambda Function

![Lambda Function](screenshots/lambda-function.png)

### Lambda Trigger

![Lambda Trigger](screenshots/lambda-trigger.png)

### SNS Topic

![SNS Topic](screenshots/sns-topic.png)

### Email Notification

![Email Notification](screenshots/email-notification.png)

### CloudWatch Logs

![CloudWatch Logs](screenshots/cloudwatch-logs.png)

### CloudWatch Alarm

![CloudWatch Alarm](screenshots/cloudwatch-alarm.png)

## 🎯 Skills Demonstrated

* AWS Serverless Architecture
* Amazon S3
* AWS Lambda
* Python
* Amazon SNS
* Amazon CloudWatch
* IAM
* Event-driven Architecture
* Monitoring and Debugging

## 👨‍💻 Author

Amuthan
