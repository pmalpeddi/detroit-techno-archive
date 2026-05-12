import boto3

session = boto3.Session(profile_name='techno-archive-dev', region_name='us-east-1')
dynamodb = session.resource('dynamodb')
table = dynamodb.Table('detroit-techno-artists')

BASE = 'https://detroit-techno-archive-media.s3.us-east-1.amazonaws.com'

artist_images = [
    ('artist_carl_craig',    f'{BASE}/artists/Carl_Craig.jpg'),
    ('artist_richie_hawtin', f'{BASE}/artists/Richie_Hawtin.jpg'),
    ('artist_jeff_mills',    f'{BASE}/artists/Jeff_Mills.jpg'),
    ('artist_robert_hood',   f'{BASE}/artists/Robert_Hood.jpg'),
    ('artist_mad_mike_banks',f'{BASE}/artists/Mike_Banks.jpg'),
]

def update():
    print("Updating artist image URLs...")
    for artist_id, url in artist_images:
        table.update_item(
            Key={'artist_id': artist_id},
            UpdateExpression='SET image_url = :url',
            ExpressionAttributeValues={':url': url}
        )
        print(f"  ✓ {artist_id}")
    print("\nDone!")

if __name__ == '__main__':
    update()