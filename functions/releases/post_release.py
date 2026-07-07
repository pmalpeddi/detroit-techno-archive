import json
import boto3
import os
import re

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(os.environ['DYNAMODB_TABLE_RELEASES'])

REQUIRED_FIELDS = ['title', 'artist']

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

        if body.get('release_id'):
            release_id = body['release_id']
        else:
            artist_slug = slugify(body.get('aliases_used') or body['artist'])
            title_slug = slugify(body['title'])
            release_id = f"release_{artist_slug}_{title_slug}"

        existing = table.get_item(Key={'release_id': release_id})
        if existing.get('Item'):
            return {
                'statusCode': 409,
                'headers': {'Content-Type': 'application/json'},
                'body': json.dumps({'error': f'Release {release_id} already exists'})
            }

        release = {
            'release_id': release_id,
            'title': body['title'],
            'artist': body['artist'],
            'aliases_used': body.get('aliases_used', ''),
            'label_id': body.get('label_id', ''),
            'catalog_number': body.get('catalog_number', ''),
            'year': body.get('year', 0),
            'format': body.get('format', ''),
            'genres': body.get('genres', []),
            'tracklist': body.get('tracklist', []),
            'description': body.get('description', ''),
            'historical_significance': body.get('historical_significance', ''),
            'image_url': body.get('image_url', '')
        }

        table.put_item(Item=release)

        return {
            'statusCode': 201,
            'headers': {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*'
            },
            'body': json.dumps(release)
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'headers': {'Content-Type': 'application/json'},
            'body': json.dumps({'error': str(e)})
        }