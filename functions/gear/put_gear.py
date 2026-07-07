import json
import boto3
import os

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(os.environ['DYNAMODB_TABLE_GEAR'])

UPDATABLE_FIELDS = [
    'name', 'type', 'manufacturer', 'released_year', 'description',
    'role_in_detroit_techno', 'associated_artists', 'image_url'
]

def lambda_handler(event, context):
    try:
        gear_id = event['pathParameters']['gear_id']
        body = json.loads(event.get('body') or '{}')

        existing = table.get_item(Key={'gear_id': gear_id})
        if not existing.get('Item'):
            return {
                'statusCode': 404,
                'headers': {'Content-Type': 'application/json'},
                'body': json.dumps({'error': 'Gear item not found'})
            }

        updates = {k: v for k, v in body.items() if k in UPDATABLE_FIELDS}
        if not updates:
            return {
                'statusCode': 400,
                'headers': {'Content-Type': 'application/json'},
                'body': json.dumps({'error': 'No valid fields to update'})
            }

        update_expr = 'SET ' + ', '.join(f'#{k} = :{k}' for k in updates)
        expr_names = {f'#{k}': k for k in updates}
        expr_values = {f':{k}': v for k, v in updates.items()}

        response = table.update_item(
            Key={'gear_id': gear_id},
            UpdateExpression=update_expr,
            ExpressionAttributeNames=expr_names,
            ExpressionAttributeValues=expr_values,
            ReturnValues='ALL_NEW'
        )

        return {
            'statusCode': 200,
            'headers': {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*'
            },
            'body': json.dumps(response['Attributes'])
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'headers': {'Content-Type': 'application/json'},
            'body': json.dumps({'error': str(e)})
        }