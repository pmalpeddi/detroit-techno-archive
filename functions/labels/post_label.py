import json
import boto3
import os
import re

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(os.environ['DYNAMODB_TABLE_LABELS'])

REQUIRED_FIELDS = ['name']

def slugify(name):
    slug = name.lower().strip()
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

        label_id = f"label_{slugify(body['name'])}"

        existing = table.get_item(Key={'label_id': label_id})
        if existing.get('Item'):
            return {
                'statusCode': 409,
                'headers': {'Content-Type': 'application/json'},
                'body': json.dumps({'error': f'Label {label_id} already exists'})
            }

        label = {
            'label_id': label_id,
            'name': body['name'],
            'founded': body.get('founded', 0),
            'origin': body.get('origin', ''),
            'profile': body.get('profile', ''),
            'founder': body.get('founder', []),
            'parent_label': body.get('parent_label', ''),
            'sublabels': body.get('sublabels', []),
            'distribution': body.get('distribution', ''),
            'contact': body.get('contact', ''),
            'genres': body.get('genres', []),
            'notable_artists': body.get('notable_artists', []),
            'notable_releases': body.get('notable_releases', []),
            'variations': body.get('variations', []),
            'links': body.get('links', {}),
            'image_url': body.get('image_url', '')
        }

        table.put_item(Item=label)

        return {
            'statusCode': 201,
            'headers': {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*'
            },
            'body': json.dumps(label)
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'headers': {'Content-Type': 'application/json'},
            'body': json.dumps({'error': str(e)})
        }