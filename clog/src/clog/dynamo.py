import uuid
from datetime import datetime
import boto3
from botocore.exceptions import ClientError


def is_table_created(engine, table_name):
    try:
        response = engine.describe_table(TableName=table_name)
        return True
    except ClientError as ce:
        if ce.response['Error']['Code'] == 'ResourceNotFoundException':
            return False
        return False


def create_table(engine, table_name, table_schema=None):
    if not table_schema:
        table_schema = {
            'KeySchema': [
                {
                    'AttributeName': 'item_id',
                    'KeyType': 'HASH'
                },
            ],
            "AttributeDefinitions": [
                {
                    'AttributeName': 'item_id',
                    'AttributeType': 'S'
                },
            ],
            "ProvisionedThroughput": {
                'ReadCapacityUnits': 1,
                'WriteCapacityUnits': 1
            }
        }

    """
    This function creates a table in dynamodb
    Returns
    -------
    String
        table creation status string
    """
    try:
        table = engine.create_table(
            TableName=table_name,
            KeySchema=table_schema['KeySchema'],
            AttributeDefinitions=table_schema['AttributeDefinitions'],
            ProvisionedThroughput=table_schema['ProvisionedThroughput']
        )
        table.meta.client.get_waiter('table_exists').wait(TableName=table_name)
        return table.table_status
    except Exception as err:
        print(err)


def put(table, data):
    item = {
        'item_id': str(uuid.uuid4()),
        'text': data,
        'created_at': datetime.now().isoformat(),
    }
    response = table.put_item(Item=item)

    return {'status': response['ResponseMetadata']['HTTPStatusCode'], 'item_id': item['item_id']}


def get_data(table, id):
    response = table.get_item(
        Item={
            'item_id': id
        }
    )
    return response['Item']


def get_all(table):
    # fetch all todos from the database
    result = table.scan()
    # return result['Items']
    return [(x['item_id'], x['text']) for x in result['Items']]


def delete_data(table, id):
    response = table.delete_item(
        Item={
            'username': 'aastha@gmail.com',
            'password': 'password'
        }
    )
    return response['Item']


def update_data(table, data):
    response = table.update_item(
        Key={
            'username': 'aastha@gmail.com',
            'password': 'password'
        },
        UpdateExpression='SET fname = :values',
        ExpressionAttributeValues={
            ':values': 'Aastha Gupta'
        }
    )
    return response['Item']


if __name__ == '__main__':
    table_name = 'backups'
    dynamodb = boto3.resource('dynamodb')

    # result = create_table(dynamodb, table_name)
    table = dynamodb.Table(table_name)
    # result = put(table, 'This is a test')
    # result2 = put(table, 'This is a second test')
    # result3 = put(table, 'This is a third test')
