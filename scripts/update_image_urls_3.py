import boto3

session = boto3.Session(profile_name='techno-archive-dev', region_name='us-east-1')
dynamodb = session.resource('dynamodb')

BASE = 'https://detroit-techno-archive-media.s3.us-east-1.amazonaws.com'

# ─── Artists ───────────────────────────────────────────────────
artists_table = dynamodb.Table('detroit-techno-artists')

artist_images = [
    ('artist_drexciya',               f'{BASE}/artists/drexciya.jpg'),
    ('artist_dj_rolando',             f'{BASE}/artists/dj_rolando.jpg'),
    ('artist_suburban_knight',        f'{BASE}/artists/suburban_knight.jpg'),
    ('artist_octave_one',             f'{BASE}/artists/octave_one.jpg'),
    ('artist_anthony_shake_shakir',   f'{BASE}/artists/anthony_shakir.jpg'),
    ('artist_aux_88',                 f'{BASE}/artists/aux_88.jpg'),
]

for artist_id, url in artist_images:
    artists_table.update_item(
        Key={'artist_id': artist_id},
        UpdateExpression='SET image_url = :url',
        ExpressionAttributeValues={':url': url}
    )
    print(f"Updated artist image: {artist_id}")

# ─── Labels ────────────────────────────────────────────────────
labels_table = dynamodb.Table('detroit-techno-labels')

label_images = [
    ('label_430_west',    f'{BASE}/labels/430_west.jpg'),
    ('label_direct_beat', f'{BASE}/labels/direct_beat.jpg'),
]

for label_id, url in label_images:
    labels_table.update_item(
        Key={'label_id': label_id},
        UpdateExpression='SET image_url = :url',
        ExpressionAttributeValues={':url': url}
    )
    print(f"Updated label image: {label_id}")

# ─── Releases ──────────────────────────────────────────────────
releases_table = dynamodb.Table('detroit-techno-releases')

release_images = [
    ('release_robert_hood_minimal_nation',            f'{BASE}/releases/minimal_nation.jpg'),
    ('release_jeff_mills_waveform_transmission_vol1', f'{BASE}/releases/waveform_transmission_vol1.jpg'),
    ('release_ur_galaxy_2_galaxy',                    f'{BASE}/releases/galaxy_2_galaxy.jpg'),
    ('release_drexciya_unknown_aquatic_habitat',      f'{BASE}/releases/unknown_aquatic_habitat.jpg'),
    ('release_aztec_mystic_jaguar',                   f'{BASE}/releases/jaguar.jpg'),
    ('release_reese_just_want_another_chance',        f'{BASE}/releases/just_want_another_chance.jpg'),
    ('release_model_500_interference',                f'{BASE}/releases/interference.jpg'),
    ('release_paperclip_people_climax',               f'{BASE}/releases/the_climax.jpg'),
    ('release_suburban_knight_art_of_stalking',       f'{BASE}/releases/art_of_stalking.jpg'),
    ('release_aux_88_is_it_man_or_machine',           f'{BASE}/releases/is_it_man_or_machine.jpg'),
]

for release_id, url in release_images:
    releases_table.update_item(
        Key={'release_id': release_id},
        UpdateExpression='SET image_url = :url',
        ExpressionAttributeValues={':url': url}
    )
    print(f"Updated release image: {release_id}")

# ─── Events ────────────────────────────────────────────────────
events_table = dynamodb.Table('detroit-techno-events')

event_images = [
    ('event_movement_2026', f'{BASE}/events/movement_2026.jpg'),
]

for event_id, url in event_images:
    events_table.update_item(
        Key={'event_id': event_id},
        UpdateExpression='SET image_url = :url',
        ExpressionAttributeValues={':url': url}
    )
    print(f"Updated event image: {event_id}")

# ─── Gear ──────────────────────────────────────────────────────
gear_table = dynamodb.Table('detroit-techno-gear')

gear_images = [
    ('gear_sequential_prophet5', f'{BASE}/gear/sequential_prophet5.jpg'),
    ('gear_moog_source',         f'{BASE}/gear/moog_source.jpg'),
    ('gear_ensoniq_esq1',        f'{BASE}/gear/ensoniq_esq1.jpg'),
    ('gear_oberheim_matrix1000', f'{BASE}/gear/oberheim_matrix1000.jpg'),
]

for gear_id, url in gear_images:
    gear_table.update_item(
        Key={'gear_id': gear_id},
        UpdateExpression='SET image_url = :url',
        ExpressionAttributeValues={':url': url}
    )
    print(f"Updated gear image: {gear_id}")

print("\n✓ Wave 3 image URLs updated.")