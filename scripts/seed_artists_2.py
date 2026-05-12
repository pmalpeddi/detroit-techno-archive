import boto3

session = boto3.Session(profile_name='techno-archive-dev', region_name='us-east-1')
dynamodb = session.resource('dynamodb')
table = dynamodb.Table('detroit-techno-artists')

artists = [
    {
        "artist_id": "artist_carl_craig",
        "name": "Carl Craig",
        "birth_name": "Carl Craig",
        "born": "October 10, 1969",
        "origin": "Detroit, MI",
        "active_years": "1989 - present",
        "genres": ["Detroit Techno", "Deep Techno", "Electronic"],
        "aliases": ["69", "Paperclip People", "BFC", "Psyche", "Innerzone Orchestra"],
        "associated_labels": ["label_planet_e", "label_transmat"],
        "associated_acts": [],
        "biography": "A second-generation Detroit Techno architect who studied under Derrick May. Founded Planet E Communications in 1991. His productions under aliases like 69 and Paperclip People pushed Detroit Techno into deeper, more atmospheric territory. Responsible for bringing a jazz and soul sensibility to the genre's machine-driven foundation. One of the most globally respected figures in electronic music.",
        "notable_tracks": ["At Les", "Throw", "Science Fiction", "Desire", "Sandstorm"],
        "gear": ["Roland TR-909", "Korg M1", "Roland Juno-106", "Akai MPC60"],
        "image_url": ""
    },
    {
        "artist_id": "artist_richie_hawtin",
        "name": "Richie Hawtin",
        "birth_name": "Richard Hawtin",
        "born": "June 4, 1970",
        "origin": "Windsor, Ontario (Detroit border)",
        "active_years": "1989 - present",
        "genres": ["Detroit Techno", "Minimal Techno", "Acid Techno"],
        "aliases": ["Plastikman", "FUSE", "Circuit Breaker", "F.U.S.E."],
        "associated_labels": ["label_plus_8", "label_minus"],
        "associated_acts": ["John Acquaviva"],
        "biography": "Born in the UK and raised in Windsor, Ontario — directly across the river from Detroit. Co-founded Plus 8 Records with John Acquaviva in 1990, one of the most influential techno labels of the 90s. His Plastikman project defined minimal acid techno. A pioneer in DJ technology, developing the use of Final Scratch and later collaborating with Native Instruments on Traktor. Ran the legendary E in Detroit parties with Derrick May.",
        "notable_tracks": ["Spastik", "Acid Rain", "Plastique", "Consumed", "Motivator"],
        "gear": ["Roland TB-303", "Roland TR-909", "Roland TR-808", "Macintosh computer"],
        "image_url": ""
    },
    {
        "artist_id": "artist_jeff_mills",
        "name": "Jeff Mills",
        "birth_name": "Jeffrey Mills",
        "born": "August 18, 1963",
        "origin": "Detroit, MI",
        "active_years": "1985 - present",
        "genres": ["Detroit Techno", "Hardcore Techno", "Industrial"],
        "aliases": ["The Wizard"],
        "associated_labels": ["label_axis", "label_underground_resistance", "label_tresor"],
        "associated_acts": ["Underground Resistance", "Final Cut"],
        "biography": "Known as The Wizard from his early days as a DJ on Detroit radio station WJLB. Co-founded Underground Resistance with Mad Mike Banks. Founded Axis Records in 1992. Renowned for his superhuman three-turntable DJ technique — simultaneously operating the mixer, drum machine, and multiple decks. His sound is among the most demanding and uncompromising in Detroit Techno history.",
        "notable_tracks": ["The Bells", "Cycle 30", "Tomorrow Comes the Harvest", "Growth"],
        "gear": ["Roland TR-909", "Roland TR-808", "Technics 1200"],
        "image_url": ""
    },
    {
        "artist_id": "artist_robert_hood",
        "name": "Robert Hood",
        "birth_name": "Robert Hood",
        "born": "January 20, 1969",
        "origin": "Detroit, MI",
        "active_years": "1989 - present",
        "genres": ["Detroit Techno", "Minimal Techno", "Gospel"],
        "aliases": ["Floorplan", "Moveable Race"],
        "associated_labels": ["label_m_plant", "label_underground_resistance"],
        "associated_acts": ["Underground Resistance"],
        "biography": "A founding member of Underground Resistance alongside Mad Mike Banks and Jeff Mills. Left UR to pursue a stripped-back, minimal sound that became hugely influential on European techno. Founded M-Plant Records. His Floorplan alias bridges his deep Christian faith with deep house music — a combination that produced the gospel house anthem Never Grow Old. One of the most consistent and uncompromising figures in Detroit Techno.",
        "notable_tracks": ["Minus", "Moveable Parts", "Never Grow Old", "Baby Baby", "Ride"],
        "gear": ["Roland TR-909", "Roland TR-808", "Roland TB-303"],
        "image_url": ""
    },
    {
        "artist_id": "artist_mad_mike_banks",
        "name": "Mad Mike Banks",
        "birth_name": "Michael Banks",
        "born": "1966",
        "origin": "Detroit, MI",
        "active_years": "1989 - present",
        "genres": ["Detroit Techno", "Industrial Techno", "Electro"],
        "aliases": ["The Deacon", "X-101", "X-102", "UR"],
        "associated_labels": ["label_underground_resistance"],
        "associated_acts": ["Underground Resistance", "Final Cut"],
        "biography": "Co-founder of Underground Resistance with Jeff Mills and Robert Hood. The ideological backbone of UR — a fiercely independent, anti-corporate Detroit Techno collective that operates with military discipline and anonymity. Mad Mike has kept UR running for over three decades, releasing music on their own terms with no major label involvement. Underground Resistance is as much a political movement as a record label.",
        "notable_tracks": ["Jaguar", "X-102 Discovers the Rings of Saturn", "Electronic Warfare", "Frictional Nevada"],
        "gear": ["Roland TR-909", "Roland TR-808", "Oberheim Matrix-1000"],
        "image_url": ""
    }
]

def seed():
    print("Seeding artists...")
    for artist in artists:
        table.put_item(Item=artist)
        print(f"  ✓ {artist['name']}")
    print(f"\n{len(artists)} artists seeded.")

if __name__ == '__main__':
    seed()