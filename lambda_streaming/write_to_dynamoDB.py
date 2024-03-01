# Import necessary modules
import json
import base64
import boto3

# Entry point for AWS Lambda


def lambda_handler(event, context):
    """
    Processes Kinesis records, decodes them, and writes them to DynamoDB.

    Parameters:
    - event (dict): Contains Kinesis records.
    - context (LambdaContext): Runtime information.

    Returns:
    - str: Success message with the number of processed records.
    """

    client = boto3.client('dynamodb')

    # Iterate over each record in the event
    for record in event['Records']:
        # Decode the base64 encoded Kinesis data
        t_record = base64.b64decode(record['kinesis']['data'])
        # Convert bytes to string
        str_record = str(t_record, 'utf-8')
        # Parse JSON string into a dictionary
        dict_record = json.loads(str_record)

        # Prepare data for Customer Row in DynamoDB
        customer_key = dict()
        customer_key.update(
            {'CustomerID': {"S": str(dict_record['CustomerID'])}})
        customer_key.update(
            {'InvoiceNo': {"S": str(dict_record['InvoiceNo'])}})

        attributes_customer = dict()
        attributes_customer.update(
            {'StockCode': {'Value': {"S": str(dict_record['StockCode'])}, "Action": "PUT"}})
        attributes_customer.update(
            {'Description': {'Value': {"S": str(dict_record['Description'])}, "Action": "PUT"}})
        attributes_customer.update(
            {'Quantity': {'Value': {"N": str(dict_record['Quantity'])}, "Action": "PUT"}})
        attributes_customer.update(
            {'InvoiceDate': {'Value': {"S": str(dict_record['InvoiceDate'])}, "Action": "PUT"}})
        attributes_customer.update(
            {'UnitPrice': {'Value': {"N": str(dict_record['UnitPrice'])}, "Action": "PUT"}})
        attributes_customer.update(
            {'Country': {'Value': {"S": str(dict_record['Country'])}, "Action": "PUT"}})

        # Write Customer Row to DynamoDB
        response = client.update_item(
            TableName='test-customer', Key=customer_key, AttributeUpdates=attributes_customer)

        # Prepare data for Invoice Row in DynamoDB
        invoice_key = dict()
        invoice_key.update({'InvoiceNo': {"S": str(dict_record['InvoiceNo'])}})
        invoice_key.update({'StockCode': {"S": str(dict_record['StockCode'])}})

        attributes_invoice = dict()
        attributes_invoice.update(
            {'Description': {'Value': {"S": str(dict_record['Description'])}, "Action": "PUT"}})
        attributes_invoice.update(
            {'Quantity': {'Value': {"N": str(dict_record['Quantity'])}, "Action": "PUT"}})
        attributes_invoice.update(
            {'InvoiceDate': {'Value': {"S": str(dict_record['InvoiceDate'])}, "Action": "PUT"}})
        attributes_invoice.update(
            {'UnitPrice': {'Value': {"N": str(dict_record['UnitPrice'])}, "Action": "PUT"}})
        attributes_invoice.update(
            {'Country': {'Value': {"S": str(dict_record['Country'])}, "Action": "PUT"}})

        # Write Invoice Row to DynamoDB
        response = client.update_item(
            TableName='test-invoice', Key=invoice_key, AttributeUpdates=attributes_invoice)

    # Return success message
    return 'Successfully processed {} records.'.format(len(event['Records']))
