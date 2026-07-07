import json
import boto3
import os
import re

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(os.environ['DYNAMODB_TABLE_GEAR'])

REQUIRED_FIELDS = ['name']

def slugify(text):
    slug = text.lower().strip()
    slug = re.sub(r'[^a-z0-9]+', '_', slug)
    return slug.strip('_')

def lambda_handler(event, context):
    try:
        body = json.loads(event.get('body') or '{}')

        missing = [f for f in REQUIRED_FIELDS if not body.get(f)]
        if missing:
            return {
                'statusCode': 400,
                'headers': {'Content-Type': 'application/json'},
                'body': json.dumps({'error': f'Missing required fields: {", ".join(missing)}'})
            }

        gear_id = body.get('gear_id') or f"gear_{slugify(body['name'])}"

        existing = table.get_item(Key={'gear_id': gear_id})
        if existing.get('Item'):
            return {
                'statusCode': 409,
                'headers': {'Content-Type': 'application/json'},
                'body': json.dumps({'error': f'Gear item {gear_id} already exists'})
            }

        gear_item = {
            'gear_id': gear_id,
            'name': body['name'],
            'type': body.get('type', ''),
            'manufacturer': body.get('manufacturer', ''),
            'released_year': body.get('released_year', 0),
            'description': body.get('description', ''),
            'role_in_detroit_techno': body.get('role_in_detroit_techno', ''),
            'associated_artists': body.get('associated_artists', []),
            'image_url': body.get('image_url', '')
        }

        table.put_item(Item=gear_item)

        return {
            'statusCode': 201,
            'headers': {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*'
            },
            'body': json.dumps(gear_item)
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'headers': {'Content-Type': 'application/json'},
            'body': json.dumps({'error': str(e)})
        }