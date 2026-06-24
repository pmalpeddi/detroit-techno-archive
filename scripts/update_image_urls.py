import boto3

session = boto3.Session(profile_name='techno-archive-dev', region_name='us-east-1')
dynamodb = session.resource('dynamodb')

BASE = 'https://detroit-techno-archive-media.s3.us-east-1.amazonaws.com'

# ─── Artists ───────────────────────────────────────────────────
artists_table = dynamodb.Table('detroit-techno-artists')

artist_images = [
    ('artist_kevin_saunderson', f'{BASE}/artists/Kevin_Saunderson.jpg'),
    ('artist_juan_atkins',      f'{BASE}/artists/Juan_Atkins.jpg'),
    ('artist_derrick_may',      f'{BASE}/artists/Derrick_May.jpg'),
    ('artist_eddie_fowlkes',    f'{BASE}/artists/Eddie_Fowlkes.jpg'),
    ('artist_blake_baxter',     f'{BASE}/artists/Blake_Baxter.jpg'),
]

# ─── Gear ──────────────────────────────────────────────────────
gear_table = dynamodb.Table('detroit-techno-gear')

gear_images = [
    ('gear_roland_tr909',   f'{BASE}/gear/Roland_TR-909.jpg'),
    ('gear_roland_tr808',   f'{BASE}/gear/Roland_TR-808.jpg'),
    ('gear_roland_tb303',   f'{BASE}/gear/Roland_TB-303.jpg'),
    ('gear_roland_juno106', f'{BASE}/gear/Roland_Juno-106.jpg'),
]

# ─── Labels ────────────────────────────────────────────────────
labels_table = dynamodb.Table('detroit-techno-labels')

label_images = [
    ('label_kms_records', f'{BASE}/labels/KMS.jpg'),
    ('label_transmat',    f'{BASE}/labels/Transmat.jpg'),
    ('label_metroplex',   f'{BASE}/labels/Metroplex.jpg'),
]

# ─── Releases ──────────────────────────────────────────────────
releases_table = dynamodb.Table('detroit-techno-releases')

release_images = [
    ('release_inner_city_big_fun',                    f'{BASE}/releases/BigFun.jpg'),
    ('release_model_500_no_ufos',                     f'{BASE}/releases/NoUFO\'S.jpg'),
    ('release_rhythim_is_rhythim_strings_of_life',    f'{BASE}/releases/StringsofLife.jpg'),
]

# ─── Venues ────────────────────────────────────────────────────
venues_table = dynamodb.Table('detroit-techno-venues')

venue_images = [
    ('venue_music_institute', f'{BASE}/venues/TheMusicInstitute.jpg'),
    ('venue_hart_plaza',      f'{BASE}/venues/HartPlaza.jpg'),
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
    update_images(artists_table,  artist_images,  'artist_id',  'Artists')
    update_images(gear_table,     gear_images,    'gear_id',    'Gear')
    update_images(labels_table,   label_images,   'label_id',   'Labels')
    update_images(releases_table, release_images, 'release_id', 'Releases')
    update_images(venues_table,   venue_images,   'venue_id',   'Venues')
    print('\nAll image URLs updated!')