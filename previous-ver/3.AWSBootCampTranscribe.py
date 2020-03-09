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
        filename = str(file_obj['s3']['object']['key'])
        print("Filename: ", filename)
        newFilename = filename.replace("%3A", ":")
        print("newFilename: ", newFilename)
        newFilename2 = newFilename [11:100]
        print("newFilename2:", newFilename2)
        contactId = filename[11:47]
        print("contactId: ", contactId)
        bucket = "awsbootcamptranscribe24"
        prefix = "https://awsbootcamptranscribe24.s3-ap-southeast-2.amazonaws.com/recordings/"
        job_uri = prefix + newFilename2

        print("link: ", job_uri)

            
    transcribe = boto3.client('transcribe')

    job_name = contactId
    #job_uri = "s3://vmdemo9900991/recordings/385035bb-8e3e-4053-b3e6-19d37f097894_2019-08-26T01:55:35Z.wav"

    transcribe.start_transcription_job(
        TranscriptionJobName=job_name,
        Media={'MediaFileUri': job_uri},
        MediaFormat='wav',
        LanguageCode='en-AU',
        OutputBucketName = 'awsbootcamp24',
        Settings={'VocabularyName': 'vocab1'}    
    )

    while True:
        status = transcribe.get_transcription_job(TranscriptionJobName=job_name)
        if status['TranscriptionJob']['TranscriptionJobStatus'] in ['COMPLETED', 'FAILED']:
            break
        print("Not ready yet...")
        time.sleep(5)
    print(status)
   
    return "Status 200 OK"

    
 