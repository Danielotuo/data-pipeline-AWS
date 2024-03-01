import json
import boto3

# Entry point for AWS Lambda


def lambda_handler(event, context):
    """
    Handles HTTP GET and POST requests in an AWS Lambda function.

    Parameters:
    - event (dict): Contains request data.
    - context (LambdaContext): Runtime information.

    Returns:
    - dict: Response data based on the request method.
    """

    # Print the event for debugging purposes
    print("MyEvent:")
    print(event)

    # Determine the HTTP method of the request
    method = event['context']['http-method']

    if method == "GET":
        # Initialize DynamoDB client
        dynamo_client = boto3.client('dynamodb')

        # Extract query parameters from the request
        im_InvoiceNo = event['params']['querystring']['InvoiceNo']
        im_StockCode = event['params']['querystring']['StockCode']

        # Construct the primary key for DynamoDB
        primary_key = dict()
        primary_key.update({'InvoiceNo': {"S": im_InvoiceNo}})
        primary_key.update({'StockCode': {"S": im_StockCode}})

        # Retrieve the item from DynamoDB
        response = dynamo_client.get_item(
            TableName='test-invoice', Key=primary_key)
        print(response['Item'])

        # Return the retrieved item in the response
        return {
            'statusCode': 200,
            'body': json.dumps(response['Item'])
        }

    elif method == "POST":
        # Process the request body
        p_record = event['body-json']
        recordstring = json.dumps(p_record)

        # Initialize Kinesis client
        client = boto3.client('kinesis')
        # Send the record to the Kinesis stream
        response = client.put_record(
            StreamName='API-Data-Stream', Data=recordstring, PartitionKey='string')

        # Return the original data in the response
        return {
            'statusCode': 200,
            'body': json.dumps(p_record)
        }

    else:
        # Return a 501 status code for unsupported methods
        return {
            'statusCode': 501,
            'body': json.dumps("Server Error")
        }
