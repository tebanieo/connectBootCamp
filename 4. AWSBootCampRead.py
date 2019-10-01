from __future__ import print_function
import boto3
import base64
import json
import os
import urllib
import logging
from botocore.exceptions import ClientError
import os
import datetime
from datetime import datetime
import time



#logger = logging.getLogger()
#logger.setLevel(logging.Error)
from urllib import request, parse

from botocore.exceptions import ClientError


def lambda_handler(event, context):
    """Read file from s3 on trigger."""
    s3 = boto3.client("s3")
    if event:
        file_obj = event["Records"][0]
        bucketname = str(file_obj['s3']['bucket']['name'])
        print (bucketname)
        filename = str(file_obj['s3']['object']['key'])
        print (filename)
        contactId = filename [0:36]
        print (contactId)
        object = s3.get_object(Bucket = bucketname,Key = filename)
        print (object)
        data = object['Body'].read().decode("utf-8")
        print(data)
        data = json.loads(data)
        transcript = data['results']['transcripts'][0]['transcript']
        print(transcript)

        table = boto3.resource('dynamodb').Table('awsbootcampcontactDetails')
        table.update_item(
            Key={
                'contactId': contactId
            },
            UpdateExpression="SET transcript = :var",
            ExpressionAttributeValues={
                ':var': transcript
            }
        )
            
    
   
    return "Status 200 OK"

    
 