import json
import boto3
import os
import re

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(os.environ['DYNAMODB_TABLE_EVENTS'])

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

        event_id = body.get('event_id') or f"event_{slugify(body['name'])}"

        existing = table.get_item(Key={'event_id': event_id})
        if existing.get('Item'):
            return {
                'statusCode': 409,
                'headers': {'Content-Type': 'application/json'},
                'body': json.dumps({'error': f'Event {event_id} already exists'})
            }

        new_event = {
            'event_id': event_id,
            'name': body['name'],
            'type': body.get('type', ''),
            'status': body.get('status', ''),
            'date': body.get('date', ''),
            'year': body.get('year', 0),
            'venue_id': body.get('venue_id', ''),
            'description': body.get('description', ''),
            'historical_significance': body.get('historical_significance', ''),
            'lineup': body.get('lineup', []),
            'image_url': body.get('image_url', '')
        }

        table.put_item(Item=new_event)

        return {
            'statusCode': 201,
            'headers': {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*'
            },
            'body': json.dumps(new_event)
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'headers': {'Content-Type': 'application/json'},
            'body': json.dumps({'error': str(e)})
        }