import json
import boto3
import os
def lambda_handler(event, context):
    DYNAMODB_ENDPOINT_URL = 'http://%s:4566' % os.environ['LOCALSTACK_HOSTNAME']
    
    client = boto3.resource("dynamodb",
    aws_access_key_id="test",
    aws_secret_access_key="test",
    endpoint_url=DYNAMODB_ENDPOINT_URL,
    region_name="us-east-1")

    table = client.Table("example")
    item = json.loads(event["body"])
    todo = item["ToDo"]
    done = item["Done"]
    #print(item)
    table.put_item(TableName="example", Item= {'ToDo': todo, 'Done': done})

    return {
        "isBase64Encoded": False,
        "statusCode": 200,
        "headers": {
            "Content-Type":"application/json",
            "Access-Control-Allow-Origin": "*"
        },
        "body": json.dumps({
            "success": True,
            "message": event
        }), 
    }