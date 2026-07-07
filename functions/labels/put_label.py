import json
import boto3
import os

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(os.environ['DYNAMODB_TABLE_LABELS'])

UPDATABLE_FIELDS = [
    'name', 'founded', 'origin', 'profile', 'founder', 'parent_label',
    'sublabels', 'distribution', 'contact', 'genres', 'notable_artists',
    'notable_releases', 'variations', 'links', 'image_url'
]

def lambda_handler(event, context):
    try:
        label_id = event['pathParameters']['label_id']
        body = json.loads(event.get('body') or '{}')

        existing = table.get_item(Key={'label_id': label_id})
        if not existing.get('Item'):
            return {
                'statusCode': 404,
                'headers': {'Content-Type': 'application/json'},
                'body': json.dumps({'error': 'Label not found'})
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
            Key={'label_id': label_id},
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