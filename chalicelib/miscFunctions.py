import os
import json
import boto3

APP_NAME = os.getenv('APP_NAME')
ENV_NAME = os.environ["ENV_NAME"]
EMAIL_QUEUE_URL = os.environ["EMAIL_QUEUE_URL"]

ERROR_LOGS_ENABLE = False
ERROR_EMAIL_ENABLE = True

def processError(errorType,errorMsg,msgBody):
    if ERROR_LOGS_ENABLE:
        print(errorType)
        print(errorMsg)
        print(msgBody)

    if ERROR_EMAIL_ENABLE:
        emailSubject = 'Error - {} - {} - Severity High' .format(APP_NAME,ENV_NAME)
        emailBody = '{}\n{}\n{}' .format(errorType,errorMsg,msgBody)
        senderEmailAddress = 'no-reply-diagnostics@spintly.com'
        recipientEmailAddresses = "malcolm@spintly.com"
        SendEmail(senderEmailAddress,recipientEmailAddresses,emailSubject,emailBody)

def SendEmail(senderEmailAddress,recipientEmailAddresses,emailSubject,emailBody):
    emailMessage = {
        "version": 1,
        "messageType": "sendEmail",
        "messageData": {
            "senderEmailAddress": senderEmailAddress,
            "recipientEmailAddresses": recipientEmailAddresses,
            "emailSubject": emailSubject,
            "emailBody": emailBody
        }
    }

    sqsClient = boto3.client('sqs')
    sqsClient.send_message(QueueUrl=EMAIL_QUEUE_URL,DelaySeconds=1,MessageBody=json.dumps(emailMessage))


