import boto3

session = boto3.Session(profile_name='techno-archive-dev', region_name='us-east-1')
dynamodb = session.resource('dynamodb')

BASE = 'https://detroit-techno-archive-media.s3.us-east-1.amazonaws.com'

# ─── Artists ───────────────────────────────────────────────────
artists_table = dynamodb.Table('detroit-techno-artists')

artist_images = [
    ('artist_stacey_pullen',          f'{BASE}/artists/Stacey_Pullen.jpg'),
    ('artist_chez_damier',            f'{BASE}/artists/Chez_Damier.jpg'),
    ('artist_alan_oldham',            f'{BASE}/artists/Alan_Oldham.jpg'),
    ('artist_claude_young',           f'{BASE}/artists/Claude_Young.jpg'),
    ('artist_cybotron',               f'{BASE}/artists/Cybotron.jpg'),
    ('artist_underground_resistance', f'{BASE}/artists/Underground_Resistance.jpg'),
]

# ─── Gear ──────────────────────────────────────────────────────
gear_table = dynamodb.Table('detroit-techno-gear')

gear_images = [
    ('gear_korg_ms20',       f'{BASE}/gear/Korg_MS-20.jpg'),
    ('gear_roland_sh101',    f'{BASE}/gear/Roland_SH-101.jpg'),
    ('gear_oberheim_dmx',    f'{BASE}/gear/Oberheim_DMX.jpg'),
    ('gear_akai_mpc60',      f'{BASE}/gear/Akai_MPC60.jpg'),
    ('gear_korg_m1',         f'{BASE}/gear/Korg_M1.jpg'),
    ('gear_emu_sp1200',      f'{BASE}/gear/EMU_SP-1200.jpg'),
    ('gear_yamaha_dx7',      f'{BASE}/gear/Yamaha_DX7.jpg'),
    ('gear_technics_sl1200', f'{BASE}/gear/Technics_SL-1200.jpg'),
]

# ─── Labels ────────────────────────────────────────────────────
labels_table = dynamodb.Table('detroit-techno-labels')

label_images = [
    ('label_network_records',       f'{BASE}/labels/Network_Records.jpg'),
    ('label_planet_e',              f'{BASE}/labels/Planet_E.jpg'),
    ('label_plus_8',                f'{BASE}/labels/Plus_8.jpg'),
    ('label_minus',                 f'{BASE}/labels/Minus.jpg'),
    ('label_axis',                  f'{BASE}/labels/Axis.jpg'),
    ('label_underground_resistance',f'{BASE}/labels/Underground_Resistance.jpg'),
    ('label_m_plant',               f'{BASE}/labels/M-Plant.jpg'),
    ('label_tresor',                f'{BASE}/labels/Tresor.jpg'),
]

# ─── Releases ──────────────────────────────────────────────────
releases_table = dynamodb.Table('detroit-techno-releases')

release_images = [
    ('release_cybotron_alleys_of_your_mind', f'{BASE}/releases/AlleysOfYourMind.jpg'),
    ('release_cybotron_clear',               f'{BASE}/releases/Clear.jpg'),
    ('release_ur_electronic_warfare',        f'{BASE}/releases/ElectronicWarfare.jpg'),
    ('release_plastikman_spastik',           f'{BASE}/releases/Spastik.jpg'),
    ('release_jeff_mills_the_bells',         f'{BASE}/releases/TheBells.jpg'),
    ('release_69_at_les',                    f'{BASE}/releases/AtLes.jpg'),
]

# ─── Venues ────────────────────────────────────────────────────
venues_table = dynamodb.Table('detroit-techno-venues')

venue_images = [
    ('venue_the_shelter',   f'{BASE}/venues/TheShelter.jpg'),
    ('venue_packard_plant', f'{BASE}/venues/PackardPlant.jpg'),
    ('venue_elektricity',   f'{BASE}/venues/Elektricity.jpg'),
    ('venue_submerge',      f'{BASE}/venues/Submerge.jpg'),
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