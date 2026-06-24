import boto3

dynamodb = boto3.resource('dynamodb', region_name='us-east-1')

# ─── Artists ───────────────────────────────────────────────────

artists_table = dynamodb.Table('detroit-techno-artists')

artists = [
    {
        "artist_id": "artist_kevin_saunderson",
        "name": "Kevin Saunderson",
        "birth_name": "Kevin Maurice Saunderson",
        "born": "September 5, 1964",
        "origin": "Brooklyn, NY (raised in Belleville, MI)",
        "active_years": "1984 - present",
        "genres": ["Detroit Techno", "House", "Acid House", "Dance-Pop"],
        "aliases": ["Reese", "Reese Project", "Tronikhouse", "Kreem", "Essaray"],
        "associated_labels": ["label_kms_records", "label_metroplex"],
        "associated_acts": ["Inner City", "E-Dancer", "The Belleville Three"],
        "biography": "One third of the legendary Belleville Three alongside Juan Atkins and Derrick May. Known as The Elevator for bringing Detroit Techno to the mainstream. Founded KMS Records in 1987. His Inner City project with vocalist Paris Grey achieved six million combined sales and nine UK top 40 hits. His Reese Bassline became foundational to jungle and drum and bass.",
        "notable_tracks": ["Big Fun", "Good Life", "Just Want Another Chance", "Velocity Funk", "Pump The Move"],
        "gear": ["Roland TR-909", "Roland TR-808", "Roland TR-727", "Yamaha DX100", "Casio CZ-1000"],
        "image_url": ""
    },
    {
        "artist_id": "artist_juan_atkins",
        "name": "Juan Atkins",
        "birth_name": "Juan Atkins",
        "born": "September 12, 1962",
        "origin": "Detroit, MI",
        "active_years": "1980 - present",
        "genres": ["Detroit Techno", "Electro"],
        "aliases": ["Model 500", "Infiniti", "Codename: Overlord"],
        "associated_labels": ["label_metroplex", "label_network_records"],
        "associated_acts": ["The Belleville Three", "Cybotron"],
        "biography": "Widely credited as the originator of Detroit Techno. Co-founded Cybotron with Rick Davis in 1980 before launching Metroplex Records in 1985 — one of the first independent techno labels. His Model 500 releases defined the cold, futuristic sound of Detroit Techno. Heavily influenced by Alvin Toffler's The Third Wave and Parliament-Funkadelic.",
        "notable_tracks": ["No UFOs", "Night Drive", "Berlin", "The Chase", "Off To Battle"],
        "gear": ["Roland TR-808", "Roland Juno-106", "Korg MS-20", "Roland SH-101"],
        "image_url": ""
    },
    {
        "artist_id": "artist_derrick_may",
        "name": "Derrick May",
        "birth_name": "Derrick Bernard May",
        "born": "April 6, 1963",
        "origin": "Detroit, MI",
        "active_years": "1984 - present",
        "genres": ["Detroit Techno", "House"],
        "aliases": ["Rhythim Is Rhythim", "Mayday"],
        "associated_labels": ["label_transmat", "label_kms_records"],
        "associated_acts": ["The Belleville Three"],
        "biography": "One third of the Belleville Three. Founded Transmat Records in 1986. His track Strings of Life is widely regarded as one of the greatest electronic records ever made — a piano-driven euphoric anthem that bridged techno and house. Brought Detroit Techno to Europe through key connections with the UK and Belgian rave scenes.",
        "notable_tracks": ["Strings of Life", "Nude Photo", "It Is What It Is", "Kao-tic Harmony", "Beyond the Dance"],
        "gear": ["Roland TR-909", "Oberheim Xpander", "Roland Juno-106", "E-mu Emulator II"],
        "image_url": ""
    },
    {
        "artist_id": "artist_eddie_fowlkes",
        "name": "Eddie Fowlkes",
        "birth_name": "Eddie Fowlkes",
        "born": "December 15, 1963",
        "origin": "Detroit, MI",
        "active_years": "1984 - present",
        "genres": ["Detroit Techno", "House", "Deep House"],
        "aliases": ["Eddy F"],
        "associated_labels": ["label_metroplex", "label_transmat"],
        "associated_acts": ["The Belleville Three"],
        "biography": "A founding member of the Detroit Techno scene and close friend of the Belleville Three. His 1984 track Goodbye Kiss was one of the first Detroit Techno records released on Metroplex. Known as a bridge between Detroit Techno and Chicago House, and a key early resident at The Music Institute.",
        "notable_tracks": ["Goodbye Kiss", "Fun With Machines", "Let's Get Together"],
        "gear": ["Roland TR-909", "Roland TR-808"],
        "image_url": ""
    },
    {
        "artist_id": "artist_blake_baxter",
        "name": "Blake Baxter",
        "birth_name": "Blake Baxter",
        "born": "1964",
        "origin": "Detroit, MI",
        "active_years": "1986 - present",
        "genres": ["Detroit Techno", "House", "Acid House"],
        "aliases": ["The Prince of Techno"],
        "associated_labels": ["label_kms_records", "label_metroplex"],
        "associated_acts": [],
        "biography": "One of the early Detroit Techno artists to cross over to European audiences. Known for his raw, sexually charged lyrics and stripped-back industrial techno sound. A regular at The Music Institute and an early KMS Records artist. Became a beloved fixture of the Berlin underground scene.",
        "notable_tracks": ["When We Used To Play", "Sexuality", "Dream Sequence One"],
        "gear": ["Roland TR-909", "Roland TB-303"],
        "image_url": ""
    }
]

# ─── Labels ────────────────────────────────────────────────────

labels_table = dynamodb.Table('detroit-techno-labels')

labels = [
    {
        "label_id": "label_metroplex",
        "name": "Metroplex",
        "variations": ["Metroplex Records"],
        "founded": 1985,
        "founder": ["Juan Atkins"],
        "origin": "Detroit, MI",
        "contact": "",
        "parent_label": "",
        "sublabels": [],
        "distribution": "Submerge",
        "genres": ["Detroit Techno", "Electro"],
        "profile": "The first dedicated Detroit Techno label, founded by Juan Atkins in 1985. Metroplex was ground zero for the Detroit Techno sound, releasing early records by Model 500, Eddie Fowlkes, and Derrick May before he launched Transmat.",
        "notable_artists": ["Juan Atkins", "Eddie Fowlkes", "Derrick May", "Blake Baxter"],
        "notable_releases": [],
        "links": {},
        "image_url": ""
    },
    {
        "label_id": "label_transmat",
        "name": "Transmat",
        "variations": ["Transmat Records"],
        "founded": 1986,
        "founder": ["Derrick May"],
        "origin": "Detroit, MI",
        "contact": "",
        "parent_label": "",
        "sublabels": [],
        "distribution": "Submerge",
        "genres": ["Detroit Techno", "House"],
        "profile": "Founded by Derrick May in 1986, Transmat became one of the most influential labels in Detroit Techno history. Home to Strings of Life and a key conduit for bringing Detroit Techno to European audiences through licensing deals with Kool Kat and other UK labels.",
        "notable_artists": ["Derrick May", "Stacey Pullen", "Bug in the Bass Bin"],
        "notable_releases": [],
        "links": {},
        "image_url": ""
    },
    {
        "label_id": "label_kms_records",
        "name": "KMS Records",
        "variations": ["KMS", "K.M.S. Records"],
        "founded": 1987,
        "founder": ["Kevin Saunderson"],
        "origin": "Ypsilanti, MI (later Detroit, MI)",
        "contact": "KMS Productions LLC, 1249 Washington Blvd, Suite 650, Detroit, Michigan 48226, USA",
        "parent_label": "Armada Music B.V.",
        "sublabels": ["KMS 25th Anniversary Classics"],
        "distribution": "Submerge (original), Above Board Distribution (2012 - present)",
        "genres": ["Detroit Techno", "House", "Deep House"],
        "profile": "Founded in 1987 by Kevin Saunderson. KMS stands for Kevin Maurice Saunderson. Released Inner City's Big Fun and Good Life, which brought Detroit Techno to mainstream global audiences. Relaunched on its 25th anniversary in 2012.",
        "notable_artists": ["Kevin Saunderson", "Blake Baxter", "MK", "Chez Damier", "Dantiez Saunderson"],
        "notable_releases": [],
        "links": {
            "website": "kmsrecordsus.com",
            "facebook": "facebook.com/kmsrecordsus",
            "soundcloud": "soundcloud.com/kmsrecords"
        },
        "image_url": ""
    }
]

# ─── Releases ──────────────────────────────────────────────────

releases_table = dynamodb.Table('detroit-techno-releases')

releases = [
    {
        "release_id": "release_rhythim_is_rhythim_strings_of_life",
        "title": "Strings of Life",
        "artist": "Derrick May",
        "aliases_used": "Rhythim Is Rhythim",
        "label_id": "label_transmat",
        "catalog_number": "TM-002",
        "year": 1987,
        "format": "12\"",
        "genres": ["Detroit Techno", "House"],
        "tracklist": ["Strings of Life", "Strings of Life (Instrumental)"],
        "description": "Recorded in 1987 with piano performed by musician Michael James. The piano lines were originally a placeholder that Derrick May intended to replace — he never did, and it became the record's defining element.",
        "historical_significance": "Widely considered one of the greatest electronic music records ever made. A euphoric, piano-driven anthem that bridged the gap between Detroit Techno and Chicago House, and became a cornerstone of the UK rave and acid house explosion.",
        "image_url": ""
    },
    {
        "release_id": "release_model_500_no_ufos",
        "title": "No UFOs",
        "artist": "Juan Atkins",
        "aliases_used": "Model 500",
        "label_id": "label_metroplex",
        "catalog_number": "MX-001",
        "year": 1985,
        "format": "12\"",
        "genres": ["Detroit Techno", "Electro"],
        "tracklist": ["No UFOs", "No UFOs (Version)"],
        "description": "The debut release on Metroplex Records and one of the earliest Detroit Techno records ever pressed. Cold, minimal, and machine-driven — a direct product of Juan Atkins' vision of music as technology.",
        "historical_significance": "Catalog number MX-001 on the first Detroit Techno label. Established the template for the Detroit Techno aesthetic: futurist, sparse, mechanical, and deeply funky.",
        "image_url": ""
    },
    {
        "release_id": "release_inner_city_big_fun",
        "title": "Big Fun",
        "artist": "Inner City",
        "aliases_used": None,
        "label_id": "label_kms_records",
        "catalog_number": "",
        "year": 1988,
        "format": "Single",
        "genres": ["Detroit Techno", "House", "Dance-Pop"],
        "tracklist": ["Big Fun", "Big Fun (Instrumental)"],
        "description": "Accidentally created when Kevin Saunderson recorded a backing track and brought in Chicago vocalist Paris Grey. Became a worldwide hit after appearing on the Virgin Records compilation Techno - The New Dance Sound of Detroit.",
        "historical_significance": "One of the defining releases that brought Detroit Techno to mainstream global audiences. Inner City went on to achieve six million combined sales and nine UK top 40 hits.",
        "image_url": ""
    }
]

# ─── Venues ────────────────────────────────────────────────────

venues_table = dynamodb.Table('detroit-techno-venues')

venues = [
    {
        "venue_id": "venue_music_institute",
        "name": "The Music Institute",
        "status": "closed",
        "opened": 1988,
        "closed": 1990,
        "address": "1315 Broadway, Detroit, MI",
        "neighborhood": "Downtown",
        "city": "Detroit, MI",
        "capacity": None,
        "type": "club",
        "genres": ["Detroit Techno", "House", "Acid House"],
        "historical_significance": "The first dedicated techno club in Detroit. No alcohol served — purely music focused. Open midnight to 8-9am. Owned by Chez Damier, Alton Miller, and George Baker. United a previously scattered scene into a tightly-knit underground family and served as the incubator of the Detroit Techno movement.",
        "notable_events": [],
        "notable_artists_performed": ["Derrick May", "Juan Atkins", "Kevin Saunderson", "Eddie Fowlkes", "Blake Baxter"],
        "image_url": ""
    },
    {
        "venue_id": "venue_hart_plaza",
        "name": "Hart Plaza",
        "status": "active",
        "opened": 1975,
        "closed": None,
        "address": "One Hart Plaza, Detroit, MI 48226",
        "neighborhood": "Downtown / Riverfront",
        "city": "Detroit, MI",
        "capacity": 50000,
        "type": "outdoor",
        "genres": ["Detroit Techno", "House", "Electronic"],
        "historical_significance": "A 14-acre public plaza on the Detroit Riverfront and home of the Movement Electronic Music Festival since 2000. The festival — originally the Detroit Electronic Music Festival — drew 1 million attendees in its first year with free admission. Now one of the most important annual techno events in the world.",
        "notable_events": ["Movement Electronic Music Festival"],
        "notable_artists_performed": ["Kevin Saunderson", "Juan Atkins", "Derrick May", "Richie Hawtin", "Carl Craig"],
        "image_url": ""
    }
]

# ─── Gear ──────────────────────────────────────────────────────

gear_table = dynamodb.Table('detroit-techno-gear')

gear = [
    {
        "gear_id": "gear_roland_tr909",
        "name": "Roland TR-909 Rhythm Composer",
        "manufacturer": "Roland Corporation",
        "type": "drum machine",
        "released_year": 1983,
        "description": "Analog/digital hybrid drum machine with MIDI. Distinctive open hi-hats, punchy kicks, and snappy snares. Originally a commercial failure, it was sold cheaply second-hand and ended up in the hands of almost every Detroit Techno and Chicago House producer.",
        "associated_artists": ["Kevin Saunderson", "Juan Atkins", "Derrick May", "Richie Hawtin", "Eddie Fowlkes"],
        "role_in_detroit_techno": "The defining drum machine of Detroit Techno and House music. Its open hi-hat became the rhythmic signature of the genre. Virtually every classic Detroit Techno record was built on a 909.",
        "image_url": ""
    },
    {
        "gear_id": "gear_roland_tr808",
        "name": "Roland TR-808 Rhythm Composer",
        "manufacturer": "Roland Corporation",
        "type": "drum machine",
        "released_year": 1980,
        "description": "All-analog drum machine with a distinctive booming kick drum, sharp snare, and cowbell. Like the 909, it was discontinued and sold cheaply before becoming ubiquitous in electronic music.",
        "associated_artists": ["Juan Atkins", "Kevin Saunderson", "Derrick May"],
        "role_in_detroit_techno": "Predates the 909 in the Detroit scene. Juan Atkins and Cybotron used the 808 extensively in early electro records that directly led to Detroit Techno. Its sub-bass kick became a signature of early Detroit productions.",
        "image_url": ""
    },
    {
        "gear_id": "gear_roland_tb303",
        "name": "Roland TB-303 Bass Line",
        "manufacturer": "Roland Corporation",
        "type": "synthesizer",
        "released_year": 1981,
        "description": "A bass synthesizer originally designed to simulate bass guitar for solo practice. Its distinctive squelching, acidic sound when knobs are tweaked during playback became the defining sound of Acid House.",
        "associated_artists": ["Blake Baxter", "Richie Hawtin", "Larry Heard"],
        "role_in_detroit_techno": "A key piece of gear bridging Detroit Techno and Chicago Acid House. Blake Baxter and later Richie Hawtin used the 303 heavily. Its acid squelch became a staple of harder Detroit Techno productions.",
        "image_url": ""
    },
    {
        "gear_id": "gear_roland_juno106",
        "name": "Roland Juno-106",
        "manufacturer": "Roland Corporation",
        "type": "synthesizer",
        "released_year": 1984,
        "description": "Six-voice polyphonic analog synthesizer with a built-in chorus effect and MIDI. Affordable, reliable, and capable of lush pads and piercing leads. One of the most widely used synths in electronic music history.",
        "associated_artists": ["Juan Atkins", "Derrick May", "Kevin Saunderson"],
        "role_in_detroit_techno": "The Juno-106's pads and chord stabs appear throughout early Detroit Techno records. Its combination of affordability and MIDI made it accessible to the Belleville Three and their peers working on tight budgets.",
        "image_url": ""
    }
]

# ─── Seed Runner ───────────────────────────────────────────────

def seed_table(table, items, label):
    print(f"\nSeeding {label}...")
    for item in items:
        table.put_item(Item=item)
        print(f"  ✓ {item.get('name') or item.get('title') or list(item.values())[0]}")
    print(f"  {len(items)} {label} seeded.")

if __name__ == '__main__':
    seed_table(artists_table, artists, "Artists")
    seed_table(labels_table, labels, "Labels")
    seed_table(releases_table, releases, "Releases")
    seed_table(venues_table, venues, "Venues")
    seed_table(gear_table, gear, "Gear")
    print("\nAll done! 🎛️")