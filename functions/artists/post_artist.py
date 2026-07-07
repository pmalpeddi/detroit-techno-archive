import json
import boto3
import os
import re

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(os.environ['DYNAMODB_TABLE_ARTISTS'])

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

        artist_id = f"artist_{slugify(body['name'])}"

        existing = table.get_item(Key={'artist_id': artist_id})
        if existing.get('Item'):
            return {
                'statusCode': 409,
                'headers': {'Content-Type': 'application/json'},
                'body': json.dumps({'error': f'Artist {artist_id} already exists'})
            }

        artist = {
            'artist_id': artist_id,
            'name': body['name'],
            'birth_name': body.get('birth_name', ''),
            'born': body.get('born', ''),
            'origin': body.get('origin', ''),
            'active_years': body.get('active_years', ''),
            'biography': body.get('biography', ''),
            'aliases': body.get('aliases', []),
            'associated_acts': body.get('associated_acts', []),
            'associated_labels': body.get('associated_labels', []),
            'genres': body.get('genres', []),
            'gear': body.get('gear', []),
            'notable_tracks': body.get('notable_tracks', []),
            'image_url': body.get('image_url', '')
        }

        table.put_item(Item=artist)

        return {
            'statusCode': 201,
            'headers': {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*'
            },
            'body': json.dumps(artist)
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'headers': {'Content-Type': 'application/json'},
            'body': json.dumps({'error': str(e)})
        }