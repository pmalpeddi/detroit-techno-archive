import boto3

session = boto3.Session(profile_name='techno-archive-dev', region_name='us-east-1')
dynamodb = session.resource('dynamodb')

# ─── Venues ───────────────────────────────────────────────────

venues_table = dynamodb.Table('detroit-techno-venues')

venues = [
    {
        "venue_id": "venue_spot_lite",
        "name": "Spot Lite",
        "status": "closed",
        "opened": 2021,
        "closed": 2026,
        "address": "2905 Beaufait St, Detroit, MI",
        "neighborhood": "Islandview",
        "city": "Detroit, MI",
        "capacity": None,
        "type": "bar / gallery / club",
        "genres": ["Detroit Techno", "House", "Electronic"],
        "historical_significance": "Opened in 2021 by Roula David and Jesse Cory, Spot Lite occupied a 7,900 sq ft repurposed Beyster Lumber warehouse in Detroit's Islandview neighborhood on the east side — well outside the traditional techno circuit of Midtown and downtown. The space operated simultaneously as a bar, art gallery, record store, coworking space, and dance floor, and was home to Cairo Coffee. Spot Lite was notable for stacking serious DJ lineups in a setting that refused to be just a club, blurring the lines between nightlife, visual art, and community gathering in ways that echoed the hybrid ambitions of Detroit's best underground spaces. It closed June 28, 2026 after a five-year run; owners cited stepping away from nightlife after building something genuinely original on the east side.",
        "notable_events": [],
        "notable_artists_performed": [],
        "image_url": ""
    },
    {
        "venue_id": "venue_ufo_bar",
        "name": "UFO Bar",
        "status": "closed",
        "opened": 2024,
        "closed": 2026,
        "address": "2110 Trumbull St, Detroit, MI",
        "neighborhood": "Corktown",
        "city": "Detroit, MI",
        "capacity": None,
        "type": "bar / club",
        "genres": ["Detroit Techno", "House", "Electronic", "Indie"],
        "historical_significance": "The building at 2110 Trumbull in Corktown had a long life as UFO Factory, a beloved indie and underground music venue. In 2024, Roula David — who also co-founded Spot Lite — purchased the space and reopened it as UFO Bar, preserving much of its original character while bringing the DJ-forward programming she had developed on the east side. The venue closed June 30, 2026; the space will reopen under new ownership as Detroit Vinyl Bar, a record store and cocktail bar, continuing the building's identity as a music-rooted gathering place in Corktown.",
        "notable_events": [],
        "notable_artists_performed": [],
        "image_url": ""
    }
]

for venue in venues:
    venues_table.put_item(Item=venue)
    print(f"Seeded venue: {venue['name']}")

print("\n✓ Wave 5 seed complete.")
print(f"  Venues:   {len(venues)}")
print(f"  Total:    {len(venues)} new entries")
