import boto3

session = boto3.Session(profile_name='techno-archive-dev', region_name='us-east-1')
dynamodb = session.resource('dynamodb')

# ─── Artists ───────────────────────────────────────────────────

artists_table = dynamodb.Table('detroit-techno-artists')

artists = [
    {
        "artist_id": "artist_moodymann",
        "name": "Moodymann",
        "birth_name": "Kenny Dixon Jr.",
        "born": "Unknown",
        "origin": "Detroit, MI",
        "active_years": "1996 - present",
        "genres": ["Detroit House", "Deep House", "Soul House"],
        "aliases": ["KDJ"],
        "associated_labels": ["label_mahogani_music"],
        "associated_acts": ["3 Chairs"],
        "biography": "Kenny Dixon Jr. — known as Moodymann — is the most singular figure in Detroit's deep house and soul movement, a producer who operates with fierce privacy and an aesthetic rooted as deeply in Marvin Gaye and Parliament-Funkadelic as in the city's techno tradition. He founded KDJ Records in the mid-1990s (later operating under the Mahogani Music name) and has released music entirely on his own terms — rarely giving interviews, performing behind curtains or in the dark, and insisting on African-American cultural ownership of Detroit's dance music at every opportunity. His productions are saturated with samples, spoken-word passages, and raw soul energy, building a body of work that sounds like no one else in electronic music. Where the first wave of Detroit Techno looked toward Europe and futurism, Moodymann looked inward — to Detroit's churches, its bars, its Black working-class culture — and made house music that was explicitly and uncompromisingly of that place.",
        "notable_tracks": ["Dem Young Sconies", "I Can't Kick This Feeling When It Hits", "Shades of Jae", "Don't Be Misled", "Sloppy Cosmic"],
        "gear": ["Roland TR-909", "Roland TR-808", "Akai MPC60"],
        "image_url": ""
    },
    {
        "artist_id": "artist_theo_parrish",
        "name": "Theo Parrish",
        "birth_name": "Theodore Parrish",
        "born": "1971",
        "origin": "Washington, D.C. / Detroit, MI",
        "active_years": "1996 - present",
        "genres": ["Detroit House", "Deep House", "Soul", "Jazz"],
        "aliases": [],
        "associated_labels": ["label_sound_signature"],
        "associated_acts": ["3 Chairs"],
        "biography": "Theo Parrish was born in Washington D.C. and studied at the American Conservatory of Music in Chicago before relocating to the Detroit area in the mid-1990s, where he founded Sound Signature Records and became one of the most uncompromising and intellectually serious figures in the international house and deep house underground. His productions are long, sprawling, and emotionally raw — drawing from jazz, soul, and African-American oral tradition to create music that refuses the commercial logic of dance formats without ever losing its grip on the floor. A fearsome live performer who treats turntables, drum machines, and mixers as simultaneous compositional instruments, Parrish is regarded by DJs and producers worldwide as one of the most technically demanding and musically honest artists the Detroit tradition has produced. His 3 Chairs collective alongside Moodymann, Rick Wilhite, and Marcellus Pittman became the defining statement of Detroit deep house in the 2000s.",
        "notable_tracks": ["Falling Up", "Yo Ya", "Black Dialogue", "The Rotating Assembly", "Synthetic Flemm"],
        "gear": ["Technics SL-1200", "Roland TR-909", "Roland TR-808"],
        "image_url": ""
    },
    {
        "artist_id": "artist_rick_wilhite",
        "name": "Rick Wilhite",
        "birth_name": "Rick Wilhite",
        "born": "Unknown",
        "origin": "Detroit, MI",
        "active_years": "1990s - present",
        "genres": ["Detroit House", "Deep House", "Soul"],
        "aliases": [],
        "associated_labels": [],
        "associated_acts": ["3 Chairs"],
        "biography": "Rick Wilhite is a Detroit DJ, producer, and selector who has operated quietly and consistently within the city's deep house underground for three decades, building a reputation as one of its most respected curators. He is a core member of 3 Chairs — the collaborative collective alongside Moodymann, Theo Parrish, and Marcellus Pittman that became the most important statement of Detroit deep house in the 2000s. His Vibes New & Old series, released across multiple volumes on Mahogani Music and other Detroit imprints, is an extended meditation on the relationship between soul, jazz, and house music that reflects the extraordinary depth and breadth of his record collection. Wilhite represents the quieter, less-heralded dimension of Detroit's music culture — knowledge keepers whose influence runs through generations of younger DJs.",
        "notable_tracks": ["Vibes New & Old", "Straight Up"],
        "gear": ["Technics SL-1200"],
        "image_url": ""
    },
    {
        "artist_id": "artist_marcellus_pittman",
        "name": "Marcellus Pittman",
        "birth_name": "Marcellus Pittman",
        "born": "Unknown",
        "origin": "Detroit, MI",
        "active_years": "1990s - present",
        "genres": ["Detroit House", "Deep House", "Soul"],
        "aliases": [],
        "associated_labels": ["label_unirhythm"],
        "associated_acts": ["3 Chairs"],
        "biography": "Marcellus Pittman is a Detroit DJ, producer, and label operator whose work has been central to the city's deep house underground since the 1990s. He founded Unirhythm Records — an imprint dedicated to the soulful, unprocessed end of the Detroit dance music spectrum — and co-founded the 3 Chairs collective with Moodymann, Theo Parrish, and Rick Wilhite. Pittman's productions and DJ sets are grounded in the African-American cultural continuum from soul and funk through house, and he is widely regarded as one of Detroit's most consistent and emotionally direct artists. His work is distributed through Submerge and sits within the same tradition of artist-controlled, community-rooted music-making that defines the Detroit underground at its best.",
        "notable_tracks": ["We Ghetto", "Unirhythm"],
        "gear": ["Technics SL-1200", "Roland TR-909"],
        "image_url": ""
    },
    {
        "artist_id": "artist_kai_alce",
        "name": "Kai Alcé",
        "birth_name": "Unknown",
        "born": "Unknown",
        "origin": "Detroit, MI / Atlanta, GA",
        "active_years": "2000s - present",
        "genres": ["Deep House", "Detroit House", "Soul"],
        "aliases": [],
        "associated_labels": ["label_ndatl_muzik"],
        "associated_acts": [],
        "biography": "Kai Alcé is a producer and label operator who bridges the Detroit and Atlanta deep house underground. He founded NDATL Muzik — the name abbreviates 'No Djays Allowed in the Lab' — as a platform for deep, soul-rooted electronic music that honors the Detroit tradition while operating from the Atlanta community. Alcé has collaborated extensively with Theo Parrish, Rick Wilhite, and Marcellus Pittman, and NDATL Muzik has become one of the most respected deep house imprints in the American underground, releasing records by both Detroit and Atlanta-rooted artists. His work demonstrates that the Detroit deep house tradition is not geographically fixed — it is a set of values, a relationship to African-American music history, that can be carried and practiced anywhere.",
        "notable_tracks": ["Phuture Thang", "Movin' On"],
        "gear": ["Technics SL-1200"],
        "image_url": ""
    },
    {
        "artist_id": "artist_delano_smith",
        "name": "Delano Smith",
        "birth_name": "Delano Smith",
        "born": "Unknown",
        "origin": "Detroit, MI",
        "active_years": "1990s - present",
        "genres": ["Detroit House", "Deep House", "Soul"],
        "aliases": [],
        "associated_labels": [],
        "associated_acts": [],
        "biography": "Delano Smith is one of Detroit's most enduring and consistently underestimated deep house figures — a DJ and producer whose career spans three decades of sustained output on labels including KMS Records, Mixmode, Vibraphone, and Rebirth. His productions are rooted in the soulful, jazz-inflected end of Detroit house, favoring warmth, feeling, and musical storytelling over the harder, more austere edge of the techno tradition. Smith has remained a fixture of the Detroit underground and has built a following among deep house listeners worldwide through a commitment to musicality that has never bent to trend or commercial pressure. He represents the wide, often invisible base of serious practitioners that makes Detroit's music culture genuinely deep rather than merely famous.",
        "notable_tracks": ["You Don't Know", "If Not for You", "The Love We Have"],
        "gear": ["Technics SL-1200", "Roland TR-909"],
        "image_url": ""
    },
    {
        "artist_id": "artist_dj_godfather",
        "name": "DJ Godfather",
        "birth_name": "Brian Jeffries",
        "born": "Unknown",
        "origin": "Detroit, MI",
        "active_years": "1990s - present",
        "genres": ["Ghettotech", "Booty Bass", "Electro"],
        "aliases": [],
        "associated_labels": ["label_databass_records"],
        "associated_acts": [],
        "biography": "Brian Jeffries — DJ Godfather — is one of the founding architects of ghettotech, the Detroit-specific synthesis of electro, booty bass, and hardcore that emerged from the city's east side in the mid-1990s. As founder of Databass Records, he built the label infrastructure around which Detroit's ghettotech movement organized, releasing dozens of records that carried the genre's raw energy, explicit content, and machine-precise production to a wider audience. His Crunk in the Trunk series — distributed through cassette, CD, and vinyl — became the definitive document of ghettotech's growth and remains a foundational reference for the genre. Godfather's productions are relentless and aggressive, rooted in the specific street culture and car-culture of Detroit's east side. Where the techno tradition pointed toward Europe and abstraction, ghettotech stayed on the block.",
        "notable_tracks": ["Crunk in the Trunk", "Bass Like Dat", "Get Up"],
        "gear": ["Roland TR-909", "Roland TR-808"],
        "image_url": ""
    },
    {
        "artist_id": "artist_dj_assault",
        "name": "DJ Assault",
        "birth_name": "Craig Adams",
        "born": "Unknown",
        "origin": "Detroit, MI",
        "active_years": "1994 - present",
        "genres": ["Ghettotech", "Booty Bass", "Electro"],
        "aliases": [],
        "associated_labels": ["label_electrofunk_records"],
        "associated_acts": [],
        "biography": "Craig Adams — DJ Assault — is ghettotech's most commercially visible and internationally known figure, and the artist most responsible for carrying the genre's explicit, raw energy beyond Detroit. His 1997 release Belle Isle Tech on Electrofunk Records introduced ghettotech's defining formula — stripped-down 909 drums, locked electro bass, and explicitly sexual lyrics delivered with total commitment — to a global underground audience. Tracks like 'Ass-N-Titties' and 'Sex on the Beach' became the genre's most recognized anthems, and the Jefferson Ave. series gave ghettotech a coherent aesthetic identity that has stuck. Assault has consistently maintained that the explicit content of ghettotech is inseparable from its cultural honesty — that the music says plainly what it means, which is itself a Detroit value. Sanitized versions exist; he has never endorsed them.",
        "notable_tracks": ["Ass-N-Titties", "Sex on the Beach", "Come On", "Belle Isle Tech", "Straight Up Detroit Shit"],
        "gear": ["Roland TR-909", "Roland TR-808"],
        "image_url": ""
    }
]

for artist in artists:
    artists_table.put_item(Item=artist)
    print(f"Seeded artist: {artist['name']}")

# ─── Labels ───────────────────────────────────────────────────

labels_table = dynamodb.Table('detroit-techno-labels')

labels = [
    {
        "label_id": "label_mahogani_music",
        "name": "Mahogani Music",
        "variations": ["KDJ Records", "Mahogani"],
        "founded": 1996,
        "founder": "Moodymann",
        "origin": "Detroit, MI",
        "genres": ["Detroit House", "Deep House", "Soul House"],
        "associated_artists": ["artist_moodymann"],
        "description": "Mahogani Music — operating under the KDJ Records imprint — is Moodymann's artist-owned label and the vehicle for virtually all of his recorded output. It operates entirely outside the music industry's conventional structures, distributing through Submerge and select independent channels, with artwork and presentation that reflect the artist's insistence on Detroit's African-American cultural ownership of its own music.",
        "historical_significance": "Mahogani Music / KDJ Records is the institutional home of Moodymann's singular body of work and one of the most important artist-owned imprints in Detroit's deep house tradition. It embodies the belief — shared across the Detroit underground — that artists must control their own infrastructure to maintain creative and cultural integrity.",
        "image_url": ""
    },
    {
        "label_id": "label_sound_signature",
        "name": "Sound Signature",
        "variations": [],
        "founded": 1996,
        "founder": "Theo Parrish",
        "origin": "Detroit, MI",
        "genres": ["Detroit House", "Deep House", "Soul", "Jazz"],
        "associated_artists": ["artist_theo_parrish"],
        "description": "Sound Signature is Theo Parrish's Detroit-based imprint, founded in the mid-1990s and distributed through Submerge. Its releases are long, uncompromising, and deliberately resistant to radio or mainstream club formats — thick, warm records that reward patient listening and reflect Parrish's deep engagement with jazz, soul, and the full history of African-American music.",
        "historical_significance": "Sound Signature is one of the defining labels of Detroit's deep house movement — a body of work that places artistic vision and cultural rootedness above commercial accessibility, sustained across three decades without compromise. Along with FXHE and Mahogani, it forms the core of Detroit's second-generation artist-owned label ecosystem.",
        "image_url": ""
    },
    {
        "label_id": "label_unirhythm",
        "name": "Unirhythm",
        "variations": [],
        "founded": 1997,
        "founder": "Marcellus Pittman",
        "origin": "Detroit, MI",
        "genres": ["Detroit House", "Deep House", "Soul"],
        "associated_artists": ["artist_marcellus_pittman"],
        "description": "Unirhythm is Marcellus Pittman's Detroit imprint and the home for his most direct statements in Detroit deep house. Releases are distributed through the Submerge network and reflect Pittman's commitment to the soulful, unpolished end of the Detroit dance music spectrum.",
        "historical_significance": "Unirhythm is part of the network of artist-owned Detroit labels that sustained the city's deep house underground through the 2000s and 2010s, maintaining a consistent output of records grounded in the African-American soul tradition within the Submerge-distributed ecosystem.",
        "image_url": ""
    },
    {
        "label_id": "label_ndatl_muzik",
        "name": "NDATL Muzik",
        "variations": ["No Djays Allowed in the Lab"],
        "founded": 2006,
        "founder": "Kai Alcé",
        "origin": "Atlanta, GA",
        "genres": ["Deep House", "Soul", "Detroit House"],
        "associated_artists": ["artist_kai_alce"],
        "description": "NDATL Muzik — the name abbreviates 'No Djays Allowed in the Lab' — is Kai Alcé's Atlanta-based imprint and the primary vehicle for the deep, soul-rooted house music community that bridges Detroit and Atlanta. The label has released records by Detroit-rooted artists including Rick Wilhite and Marcellus Pittman alongside Atlanta producers, operating as connective tissue between the two cities' underground scenes.",
        "historical_significance": "NDATL Muzik extended the reach of Detroit's deep house tradition to the Atlanta community and built one of the few American underground house labels of the 2000s to sustain output consistent with the values and aesthetics of the original Detroit deep house movement.",
        "image_url": ""
    },
    {
        "label_id": "label_databass_records",
        "name": "Databass Records",
        "variations": ["Databass"],
        "founded": 1994,
        "founder": "DJ Godfather",
        "origin": "Detroit, MI",
        "genres": ["Ghettotech", "Booty Bass", "Electro"],
        "associated_artists": ["artist_dj_godfather"],
        "description": "Databass Records is DJ Godfather's Detroit imprint and the primary institutional home of ghettotech — the hard, explicit, electro-driven genre that emerged from Detroit's east side in the mid-1990s. The label has released hundreds of records documenting the full range of the ghettotech sound, from Godfather's own productions to releases by other Detroit booty bass artists.",
        "historical_significance": "Databass Records is the infrastructure that made ghettotech a genre rather than a local phenomenon. By providing a consistent release platform and distribution channel, it allowed ghettotech to reach audiences beyond Detroit and established the label as the definitive institutional home of Detroit's most explicitly street-rooted dance music.",
        "image_url": ""
    },
    {
        "label_id": "label_electrofunk_records",
        "name": "Electrofunk Records",
        "variations": ["Jefferson Ave.", "Electrofunk"],
        "founded": 1996,
        "founder": "DJ Assault",
        "origin": "Detroit, MI",
        "genres": ["Ghettotech", "Booty Bass", "Electro"],
        "associated_artists": ["artist_dj_assault"],
        "description": "Electrofunk Records is DJ Assault's Detroit imprint, founded in the mid-1990s and home to Belle Isle Tech (1997) — the release widely credited with introducing ghettotech to an international audience. The 'Jefferson Ave.' branding — drawn from the Detroit avenue running through the city's east side — became associated with the label's compilation series and gave the wider ghettotech aesthetic its most recognizable identity.",
        "historical_significance": "Electrofunk Records was ghettotech's primary vehicle for international visibility. Belle Isle Tech (1997) is considered the genre's defining document, and the Jefferson Ave. compilation series gave ghettotech a coherent identity and distribution pathway that reached DJs and collectors worldwide.",
        "image_url": ""
    }
]

for label in labels:
    labels_table.put_item(Item=label)
    print(f"Seeded label: {label['name']}")

# ─── Releases ───────────────────────────────────────────────────

releases_table = dynamodb.Table('detroit-techno-releases')

releases = [
    {
        "release_id": "release_moodymann_i_cant_kick_this_feeling",
        "title": "I Can't Kick This Feeling When It Hits",
        "artist": "Moodymann",
        "aliases_used": "Moodymann",
        "label_id": "label_mahogani_music",
        "catalog_number": "KDJ-001",
        "year": 1996,
        "format": "12\"",
        "genres": ["Detroit House", "Deep House", "Soul House"],
        "tracklist": ["I Can't Kick This Feeling When It Hits", "Shades of Jae"],
        "description": "KDJ Records' debut release introduced Moodymann's aesthetic in fully-formed terms — a raw, sampled, deeply soulful house record that bore almost no resemblance to the European techno flooding dance floors at the same moment. 'I Can't Kick This Feeling When It Hits' is built from Detroit R&B and gospel DNA, its drums loose and live-feeling, its emotion unguarded. It announced that house music's African-American roots were not background to be acknowledged but the entire point.",
        "historical_significance": "KDJ-001 is the opening statement of one of Detroit electronic music's most important bodies of work. It established the aesthetic framework — soulful, politically conscious, explicitly Black — that Moodymann would sustain across three decades, and marked the beginning of Detroit's second-generation deep house movement.",
        "image_url": ""
    },
    {
        "release_id": "release_moodymann_forevernevermore",
        "title": "Forevernevermore",
        "artist": "Moodymann",
        "aliases_used": "Moodymann",
        "label_id": "label_mahogani_music",
        "catalog_number": "KDJ-013",
        "year": 2000,
        "format": "2xLP",
        "genres": ["Detroit House", "Deep House", "Soul House"],
        "tracklist": ["Dem Young Sconies", "Don't Be Misled", "I'd Rather Be Lonely", "Let's Get It On (Not the Marvin Gaye Song)", "Andover"],
        "description": "Moodymann's debut full-length is a double LP that spreads across soul, funk, gospel, and raw Detroit house with complete disregard for genre boundaries. Layered with samples, spoken-word passages, and the sound of actual Detroit life, it sounds more like a living document of the city's African-American music culture than a conventional electronic album — dense, emotional, and impossible to fully map on first listen.",
        "historical_significance": "Forevernevermore established Moodymann as more than a 12-inch producer — as an artist capable of sustaining a statement across album length, one whose work demands to be understood in the tradition of Marvin Gaye and George Clinton as much as Juan Atkins. It remains one of the most personally and culturally ambitious releases in the history of Detroit electronic music.",
        "image_url": ""
    },
    {
        "release_id": "release_theo_parrish_american_intelligence",
        "title": "American Intelligence",
        "artist": "Theo Parrish",
        "aliases_used": "Theo Parrish",
        "label_id": "label_sound_signature",
        "catalog_number": "SS-016",
        "year": 2001,
        "format": "2xLP",
        "genres": ["Detroit House", "Deep House", "Soul", "Jazz"],
        "tracklist": ["Falling Up", "Yo Ya", "Black Dialogue", "Synthetic Flemm", "Cass Corridor"],
        "description": "Theo Parrish's debut full-length on Sound Signature is a sprawling, uncompromising document of his approach to house music — long tracks that breathe and develop over extended running time, layered with jazz textures, soul samples, and percussion that feels live even when machine-generated. American Intelligence refuses the efficiency of club-formatted house and demands to be experienced as a complete work. 'Cass Corridor' takes its name from the Detroit neighborhood that was the city's bohemian heart before gentrification.",
        "historical_significance": "American Intelligence announced Theo Parrish as one of the most intellectually and musically serious figures in global house music and established Sound Signature as the home of Detroit's most uncompromising deep house vision. It remains a foundational text for the international deep house underground and a benchmark for what a house music album can demand of its listener.",
        "image_url": ""
    },
    {
        "release_id": "release_dj_assault_belle_isle_tech",
        "title": "Belle Isle Tech",
        "artist": "DJ Assault",
        "aliases_used": "DJ Assault",
        "label_id": "label_electrofunk_records",
        "catalog_number": "EF-001",
        "year": 1997,
        "format": "12\"",
        "genres": ["Ghettotech", "Booty Bass", "Electro"],
        "tracklist": ["Ass-N-Titties", "Sex on the Beach", "Come On", "Belle Isle Tech"],
        "description": "The release that defined ghettotech as a genre — fast, stripped-down 909 drums, locked electro bass, and explicit lyrical content delivered with total commitment. The title references Belle Isle, the Detroit island park in the Detroit River. 'Ass-N-Titties' became the genre's most recognized anthem and a global signifier of Detroit's most raw and unfiltered underground dance music. The explicit titles are not provocation for its own sake: they are the literal content of the genre, which has always said plainly what it means.",
        "historical_significance": "Belle Isle Tech introduced ghettotech to an international audience and established the genre's formal conventions: hard 909 patterns, minimal electro bass, and explicit content treated as a musical and cultural statement. It is the single most important document in ghettotech history and remains the entry point for anyone approaching the genre from outside Detroit.",
        "image_url": ""
    },
    {
        "release_id": "release_dj_assault_jefferson_ave_7_mile",
        "title": "Jefferson Ave. & 7 Mile",
        "artist": "DJ Assault",
        "aliases_used": "DJ Assault",
        "label_id": "label_electrofunk_records",
        "catalog_number": "EF-007",
        "year": 2001,
        "format": "2xLP",
        "genres": ["Ghettotech", "Booty Bass", "Electro"],
        "tracklist": ["Straight Up Detroit Shit", "Let Me See You Get Low", "Pop That Coochie", "Detroit Allstars"],
        "description": "Named for the east side Detroit geography — Jefferson Avenue running along the riverfront, 7 Mile Road crossing the city — Jefferson Ave. & 7 Mile is a sprawling statement of ghettotech at the peak of its first wave of international circulation. The album functions simultaneously as a DJ toolkit, a scene document, and a geographic statement: this music belongs to a specific place and a specific community, and it sounds like neither would ask you to pretend otherwise.",
        "historical_significance": "Jefferson Ave. & 7 Mile consolidated ghettotech's international identity and gave the genre a title and aesthetic statement that has become its most widely referenced document outside Detroit. The 'Jefferson Ave.' branding became synonymous with the hardest, most stripped-down end of the Detroit underground.",
        "image_url": ""
    },
]

for release in releases:
    releases_table.put_item(Item=release)
    print(f"Seeded release: {release['title']} by {release['artist']}")

print("\n✓ Wave 6 seed complete.")
print(f"  Artists:  {len(artists)}")
print(f"  Labels:   {len(labels)}")
print(f"  Releases: {len(releases)}")
print(f"  Total:    {len(artists) + len(labels) + len(releases)} new entries")
