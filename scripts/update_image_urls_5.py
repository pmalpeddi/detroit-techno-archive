import boto3

session = boto3.Session(profile_name='techno-archive-dev', region_name='us-east-1')
dynamodb = session.resource('dynamodb')

BASE = 'https://detroit-techno-archive-media.s3.us-east-1.amazonaws.com'

# ─── Venues ────────────────────────────────────────────────────
venues_table = dynamodb.Table('detroit-techno-venues')

venue_images = [
    ('venue_spot_lite', f'{BASE}/venues/spot_lite.jpg'),
    ('venue_ufo_bar',   f'{BASE}/venues/ufo_bar.jpg'),
]

# ─── Runner ────────────────────────────────────────────────────
def update_images(table, items, pk_field, label):
    print(f'\nUpdating {label}...')
    for pk, url in items:
        table.update_item(
            Key={pk_field: pk},
            UpdateExpression='SET image_url = :url',
            ExpressionAttributeValues={':url': url}
        )
        print(f'  ✓ {pk}')

if __name__ == '__main__':
    update_images(venues_table, venue_images, 'venue_id', 'Venues')
    print('\n✓ Wave 5 image URLs updated.')
