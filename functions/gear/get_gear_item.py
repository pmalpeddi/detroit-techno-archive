import json, boto3, os
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(os.environ['DYNAMODB_TABLE_GEAR'])

def lambda_handler(event, context):
    try:
        gear_id = event['pathParameters']['gear_id']
        response = table.get_item(Key={'gear_id': gear_id})
        item = response.get('Item')
        if not item:
            return {'statusCode': 404, 'headers': {'Content-Type': 'application/json'}, 'body': json.dumps({'error': 'Gear not found'})}
        return {'statusCode': 200, 'headers': {'Content-Type': 'application/json', 'Access-Control-Allow-Origin': '*'}, 'body': json.dumps(item)}
    except Exception as e:
        return {'statusCode': 500, 'headers': {'Content-Type': 'application/json'}, 'body': json.dumps({'error': str(e)})}