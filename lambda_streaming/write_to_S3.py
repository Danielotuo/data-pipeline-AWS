from __future__ import print_function

import base64
import json
import boto3
from datetime import datetime

s3_client = boto3.client('s3')

# Converting datetime object to string
dateTimeObj = datetime.now()

# format the string
timestampStr = dateTimeObj.strftime("%d-%b-%Y-%H%M%S")

# this is the list for the records
kinesisRecords = []


def lambda_handler(event, context):
    """
    Processes Kinesis records, decodes them, and writes them to an S3 bucket.

    Parameters:
    - event (dict): Contains Kinesis records.
    - context (LambdaContext): Runtime information.

    Returns:
    - str: Success message with the number of processed records.
    """
    for record in event['Records']:
        payload = base64.b64decode(record['kinesis']['data'])
        kinesisRecords.append(payload)
        print("Decoded payload: " + payload)

    # Join all decoded payloads into a single string, separated by newlines
    ex_string = '\n'.join(kinesisRecords)

    # Generate the S3 object key using the current timestamp
    mykey = 'output-' + timestampStr + '.txt'

    # Write the combined string to the S3 bucket
    response = s3_client.put_object(
        Body=ex_string, Bucket='aws-de-project', Key=mykey)

    return 'Successfully processed {} records.'.format(len(event['Records']))
