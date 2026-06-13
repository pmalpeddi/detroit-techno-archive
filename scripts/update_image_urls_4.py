import boto3

session = boto3.Session(profile_name='techno-archive-dev', region_name='us-east-1')
dynamodb = session.resource('dynamodb')

BASE = 'https://detroit-techno-archive-media.s3.us-east-1.amazonaws.com'

# ─── Artists ───────────────────────────────────────────────────
artists_table = dynamodb.Table('detroit-techno-artists')

artist_images = [
    ('artist_kenny_larkin',    f'{BASE}/artists/kenny_larkin.jpg'),
    ('artist_dj_minx',         f'{BASE}/artists/dj_minx.jpg'),
    ('artist_omar_s',          f'{BASE}/artists/omar_s.jpg'),
    ('artist_dopplereffekt',   f'{BASE}/artists/dopplereffekt.jpg'),
    ('artist_terrence_dixon',  f'{BASE}/artists/terrence_dixon.jpg'),
]

# ─── Labels ────────────────────────────────────────────────────
labels_table = dynamodb.Table('detroit-techno-labels')

label_images = [
    ('label_fxhe',           f'{BASE}/labels/fxhe.jpg'),
    ('label_women_on_wax',   f'{BASE}/labels/women_on_wax.jpg'),
    ('label_population_one', f'{BASE}/labels/population_one.jpg'),
]

# ─── Releases ──────────────────────────────────────────────────
releases_table = dynamodb.Table('detroit-techno-releases')

release_images = [
    ('release_carl_craig_landcruising',    f'{BASE}/releases/landcruising.jpg'),
    ('release_model_500_night_drive',      f'{BASE}/releases/night_drive.jpg'),
    ('release_ur_interstellar_fugitives',  f'{BASE}/releases/interstellar_fugitives.jpg'),
    ('release_eddie_fowlkes_goodbye_kiss', f'{BASE}/releases/goodbye_kiss.jpg'),
    ('release_omar_s_thank_you',           f'{BASE}/releases/thank_you.jpg'),
]

# ─── Events ────────────────────────────────────────────────────
events_table = dynamodb.Table('detroit-techno-events')

event_images = [
    ('event_demf_2000', f'{BASE}/events/demf_2000.jpg'),
]

# ─── Venues ────────────────────────────────────────────────────
venues_table = dynamodb.Table('detroit-techno-venues')

venue_images = [
    ('venue_st_andrews_hall', f'{BASE}/venues/st_andrews_hall.jpg'),
    ('venue_bookies_club',    f'{BASE}/venues/bookies_club.jpg'),
    ('venue_marble_bar',      f'{BASE}/venues/marble_bar.jpg'),
]

# ─── Gear ──────────────────────────────────────────────────────
gear_table = dynamodb.Table('detroit-techno-gear')

gear_images = [
    ('gear_roland_jupiter8',       f'{BASE}/gear/roland_jupiter8.jpg'),
    ('gear_akai_s950',             f'{BASE}/gear/akai_s950.jpg'),
    ('gear_sequential_six_trak',   f'{BASE}/gear/sequential_six_trak.jpg'),
    ('gear_roland_mc202',          f'{BASE}/gear/roland_mc202.jpg'),
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
    update_images(events_table,   event_images,   'event_id',   'Events')
    update_images(venues_table,   venue_images,   'venue_id',   'Venues')
    update_images(gear_table,     gear_images,    'gear_id',    'Gear')
    print('\n✓ Wave 4 image URLs updated.')
