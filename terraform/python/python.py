import json
def lambda_handler(event, context):
   message = json.loads('Hello {} !'.format(event['key1']))
   print(message)
   return {
        "statusCode": 200,
        "headers": {'Content-Type': 'application/json'},
        "body": json.dumps(message)
   }