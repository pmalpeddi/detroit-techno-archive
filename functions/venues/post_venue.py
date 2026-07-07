import json
import boto3
import os
import re

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(os.environ['DYNAMODB_TABLE_VENUES'])

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

        venue_id = body.get('venue_id') or f"venue_{slugify(body['name'])}"

        existing = table.get_item(Key={'venue_id': venue_id})
        if existing.get('Item'):
            return {
                'statusCode': 409,
                'headers': {'Content-Type': 'application/json'},
                'body': json.dumps({'error': f'Venue {venue_id} already exists'})
            }

        venue = {
            'venue_id': venue_id,
            'name': body['name'],
            'type': body.get('type', ''),
            'status': body.get('status', ''),
            'address': body.get('address', ''),
            'neighborhood': body.get('neighborhood', ''),
            'city': body.get('city', ''),
            'opened': body.get('opened', 0),
            'closed': body.get('closed', 0),
            'capacity': body.get('capacity', None),
            'genres': body.get('genres', []),
            'notable_artists_performed': body.get('notable_artists_performed', []),
            'notable_events': body.get('notable_events', []),
            'historical_significance': body.get('historical_significance', ''),
            'image_url': body.get('image_url', '')
        }

        table.put_item(Item=venue)

        return {
            'statusCode': 201,
            'headers': {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*'
            },
            'body': json.dumps(venue)
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'headers': {'Content-Type': 'application/json'},
            'body': json.dumps({'error': str(e)})
        }