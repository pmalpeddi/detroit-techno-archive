import boto3

session = boto3.Session(profile_name='techno-archive-dev', region_name='us-east-1')
dynamodb = session.resource('dynamodb')

BASE = 'https://detroit-techno-archive-media.s3.us-east-1.amazonaws.com'

# ─── Artists ────────────────────────────────────────────────────
artists_table = dynamodb.Table('detroit-techno-artists')

artist_images = [
    ('artist_moodymann',         f'{BASE}/artists/moodymann.jpg'),
    ('artist_theo_parrish',      f'{BASE}/artists/theo_parrish.jpg'),
    ('artist_rick_wilhite',      f'{BASE}/artists/rick_wilhite.jpg'),
    ('artist_marcellus_pittman', f'{BASE}/artists/marcellus_pittman.jpg'),
    ('artist_kai_alce',          f'{BASE}/artists/kai_alce.jpg'),
    ('artist_delano_smith',      f'{BASE}/artists/delano_smith.jpg'),
    ('artist_dj_godfather',      f'{BASE}/artists/dj_godfather.jpg'),
    ('artist_dj_assault',        f'{BASE}/artists/dj_assault.jpg'),
]

# ─── Labels ─────────────────────────────────────────────────────
labels_table = dynamodb.Table('detroit-techno-labels')

label_images = [
    ('label_mahogani_music',      f'{BASE}/labels/mahogani_music.jpg'),
    ('label_sound_signature',     f'{BASE}/labels/sound_signature.jpg'),
    ('label_unirhythm',           f'{BASE}/labels/unirhythm.jpg'),
    ('label_ndatl_muzik',         f'{BASE}/labels/ndatl_muzik.jpg'),
    ('label_databass_records',    f'{BASE}/labels/databass_records.jpg'),
    ('label_electrofunk_records', f'{BASE}/labels/electrofunk_records.jpg'),
]

# ─── Releases ───────────────────────────────────────────────────
releases_table = dynamodb.Table('detroit-techno-releases')

release_images = [
    ('release_moodymann_i_cant_kick_this_feeling',   f'{BASE}/releases/moodymann_i_cant_kick_this_feeling.jpg'),
    ('release_moodymann_forevernevermore',            f'{BASE}/releases/moodymann_forevernevermore.jpg'),
    ('release_theo_parrish_american_intelligence',   f'{BASE}/releases/theo_parrish_american_intelligence.jpg'),
    ('release_dj_assault_belle_isle_tech',           f'{BASE}/releases/dj_assault_belle_isle_tech.jpg'),
    ('release_dj_assault_jefferson_ave_7_mile',      f'{BASE}/releases/dj_assault_jefferson_ave_7_mile.jpg'),
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
    update_images(labels_table,   label_images,   'label_id',   'Labels')
    update_images(releases_table, release_images, 'release_id', 'Releases')
    print('\n✓ Wave 6 image URLs updated.')
