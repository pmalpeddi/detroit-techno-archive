import boto3

session = boto3.Session(profile_name='techno-archive-dev', region_name='us-east-1')
dynamodb = session.resource('dynamodb')

# ─── Artists ───────────────────────────────────────────────────

artists_table = dynamodb.Table('detroit-techno-artists')

artists = [
    {
        "artist_id": "artist_drexciya",
        "name": "Drexciya",
        "birth_name": "Gerald Donald & James Stinson",
        "born": "Unknown",
        "origin": "Detroit, MI",
        "active_years": "1989 - 2002",
        "genres": ["Detroit Techno", "Electro", "Electronica"],
        "aliases": ["Heinrich Mueller", "Elecktroids", "Dopplereffekt"],
        "associated_labels": ["label_underground_resistance", "label_tresor"],
        "associated_acts": ["Underground Resistance"],
        "biography": "Drexciya was the mythological and musical project of Gerald Donald and James Stinson, two of Detroit's most enigmatic artists. Operating under near-total anonymity, they built an elaborate Afrofuturist mythology around an underwater civilization descended from enslaved Africans thrown overboard during the Middle Passage. Their music was ferocious, propulsive electro-techno — machine music with emotional depth few could match. James Stinson passed away in 2002 shortly after Drexciya's final interview, leaving the project's mythology intact and unresolved.",
        "notable_tracks": ["The Unknown Aquatic Habitat", "Aquatic Invasion", "Sea Quake", "Bubble Metropolis", "Wavejumper"],
        "gear": ["Roland TR-808", "Roland TR-909", "Roland SH-101", "Korg MS-20"],
        "image_url": ""
    },
    {
        "artist_id": "artist_dj_rolando",
        "name": "DJ Rolando",
        "birth_name": "Rolando Rocha",
        "born": "1974",
        "origin": "Detroit, MI",
        "active_years": "1994 - present",
        "genres": ["Detroit Techno", "Techno", "House"],
        "aliases": ["Aztec Mystic"],
        "associated_labels": ["label_underground_resistance", "label_tresor"],
        "associated_acts": ["Underground Resistance"],
        "biography": "Rolando Rocha is a Detroit DJ and producer who rose to prominence as a member of the Underground Resistance collective. His 1999 release Jaguar, issued under the alias Aztec Mystic, became one of the most recognizable and beloved tracks in techno history — a soaring, melodic anthem built from orchestral stabs and driving percussion that captured the spiritual dimension of Detroit Techno at its peak. He remains an active DJ with a global following.",
        "notable_tracks": ["Jaguar", "Knights of the Jaguar", "Los Niños", "Strings of Life (UR Edit)"],
        "gear": ["Roland TR-909", "Roland TR-808", "Korg M1"],
        "image_url": ""
    },
    {
        "artist_id": "artist_suburban_knight",
        "name": "Suburban Knight",
        "birth_name": "James Pennington",
        "born": "1963",
        "origin": "Detroit, MI",
        "active_years": "1987 - present",
        "genres": ["Detroit Techno", "House", "Dark Techno"],
        "aliases": ["Suburban Knight", "The Mentalist"],
        "associated_labels": ["label_transmat", "label_underground_resistance"],
        "associated_acts": [],
        "biography": "James Pennington is one of the original Detroit Techno producers, a close associate of Derrick May who released some of the darkest and most atmospheric records on Transmat Records. His 1990 EP The Art of Stalking is considered a cornerstone of early Detroit Techno — shadowy, paranoid machine music that pushed the sound toward its more industrial and minimal possibilities. He has remained active through decades of techno's evolution.",
        "notable_tracks": ["The Art of Stalking", "Nocturbulous Behavior", "My Sol Dark Funk", "Vanguard"],
        "gear": ["Roland TR-909", "Roland Juno-106", "Roland TR-808"],
        "image_url": ""
    },
    {
        "artist_id": "artist_octave_one",
        "name": "Octave One",
        "birth_name": "Lenny Burden & Lawrence Burden",
        "born": "Unknown",
        "origin": "Detroit, MI",
        "active_years": "1989 - present",
        "genres": ["Detroit Techno", "Techno", "House"],
        "aliases": ["Random Noise Generation", "Dusoul"],
        "associated_labels": ["label_430_west", "label_tresor"],
        "associated_acts": [],
        "biography": "Brothers Lenny and Lawrence Burden formed Octave One in Detroit in the late 1980s, becoming one of the most consistent and beloved acts in the Detroit Techno tradition. They founded their own label 430 West Records to maintain creative control, releasing a catalog of deep, functional techno with strong emotional undercurrents. Their 2000 track Blackwater became an unlikely anthem — raw, ragged, and rooted in Detroit soul.",
        "notable_tracks": ["Blackwater", "I Believe", "Life Story", "Open Your Eyes", "The X-Files"],
        "gear": ["Roland TR-909", "Akai MPC60", "E-mu SP-1200", "Korg M1"],
        "image_url": ""
    },
    {
        "artist_id": "artist_anthony_shake_shakir",
        "name": "Anthony \"Shake\" Shakir",
        "birth_name": "Anthony Shakir",
        "born": "1966",
        "origin": "Detroit, MI",
        "active_years": "1987 - present",
        "genres": ["Detroit Techno", "House", "Electro"],
        "aliases": ["Shake"],
        "associated_labels": ["label_metroplex", "label_plus_8"],
        "associated_acts": [],
        "biography": "Anthony Shakir is one of Detroit's most respected and prolific producers, a behind-the-scenes architect of the early Detroit Techno sound who worked closely with Juan Atkins and the Metroplex circle. Known for his meticulous ear and mentoring of younger Detroit talent, Shakir has released records across several decades without ever chasing trends. His work is prized by collectors and DJs for its depth, warmth, and technical precision.",
        "notable_tracks": ["Frictionalism", "The Groove That Won't Stop", "Rogue State", "Detroit 2 Frankfurt"],
        "gear": ["Roland TR-909", "Roland TB-303", "Korg MS-20", "Ensoniq ESQ-1"],
        "image_url": ""
    },
    {
        "artist_id": "artist_aux_88",
        "name": "Aux 88",
        "birth_name": "Tommy Hamilton & Keith Tucker",
        "born": "Unknown",
        "origin": "Detroit, MI",
        "active_years": "1992 - present",
        "genres": ["Detroit Techno", "Electro", "Detroit Electro"],
        "aliases": ["Bass Agenda", "X-Ray"],
        "associated_labels": ["label_direct_beat"],
        "associated_acts": [],
        "biography": "Tommy Hamilton and Keith Tucker are the duo behind Aux 88, the most important act in Detroit Electro's revival. Operating on the Direct Beat label they co-run with DJ Stingray, Aux 88 kept Detroit's electro tradition alive through the 1990s and 2000s when techno had largely moved on. Their robotic vocoder vocals, punishing 808 kicks, and science-fiction aesthetics made them cult figures globally and laid the groundwork for electro's international resurgence in the 2010s.",
        "notable_tracks": ["Is It Man or Machine?", "Made in Detroit", "Electro Invasion", "Bass Magnetic", "Tokyo"],
        "gear": ["Roland TR-808", "Roland SH-101", "Korg MS-20", "Sequential Circuits Prophet-5"],
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
        "label_id": "label_430_west",
        "name": "430 West Records",
        "variations": ["430 West"],
        "founded": 1992,
        "founder": "Lenny Burden, Lawrence Burden",
        "origin": "Detroit, MI",
        "genres": ["Detroit Techno", "Techno", "House"],
        "associated_artists": ["artist_octave_one"],
        "description": "430 West Records is the independent Detroit Techno label founded by brothers Lenny and Lawrence Burden of Octave One. The label gave the duo full creative and commercial control over their output and became a reliable imprint for deep, honest Detroit Techno through the 1990s and 2000s. It stands as an example of the Detroit tradition of artist-owned labels.",
        "historical_significance": "One of several artist-owned Detroit Techno labels that kept the scene independent and self-sustaining through the commercial EDM boom of the late 1990s and 2000s.",
        "image_url": ""
    },
    {
        "label_id": "label_direct_beat",
        "name": "Direct Beat",
        "variations": ["Direct Beat Crew"],
        "founded": 1992,
        "founder": "Tommy Hamilton, Keith Tucker, DJ Stingray",
        "origin": "Detroit, MI",
        "genres": ["Detroit Techno", "Electro", "Detroit Electro"],
        "associated_artists": ["artist_aux_88"],
        "description": "Direct Beat is the Detroit Electro label co-founded by Aux 88 and DJ Stingray. It became the primary home of Detroit Electro through the 1990s and beyond, releasing records that kept the Roland TR-808 and SH-101 tradition alive long after techno had moved toward minimalism and abstraction.",
        "historical_significance": "The central label of Detroit Electro — a distinct strand of Detroit electronic music rooted in the electro tradition of Afrika Bambaataa and the early Roland drum machine sound. Direct Beat kept this tradition alive and influential for over three decades.",
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
        "release_id": "release_robert_hood_minimal_nation",
        "title": "Minimal Nation",
        "artist": "Robert Hood",
        "aliases_used": "Robert Hood",
        "label_id": "label_axis",
        "catalog_number": "AX-001",
        "year": 1994,
        "format": "LP",
        "genres": ["Detroit Techno", "Minimal Techno"],
        "tracklist": ["Home", "Minus", "Protein Valve", "Moveable Parts", "Internal Empire", "Pace"],
        "description": "Robert Hood's debut long-player on his own Axis label, Minimal Nation is the founding document of minimal techno. Recorded in Detroit with stripped-back drum machine patterns, bass tones, and near-total absence of melody, it proved that techno's power came from rhythm and negative space, not complexity.",
        "historical_significance": "The record that defined minimal techno as a genre. Hood's reduction of Detroit Techno to its barest functional elements — kick, bass, hi-hat, space — became the template for an entire strand of electronic music that dominated clubs globally through the late 1990s and 2000s.",
        "image_url": ""
    },
    {
        "release_id": "release_jeff_mills_waveform_transmission_vol1",
        "title": "Waveform Transmission Vol. 1",
        "artist": "Jeff Mills",
        "aliases_used": "Jeff Mills",
        "label_id": "label_tresor",
        "catalog_number": "TRESOR 19",
        "year": 1992,
        "format": "LP",
        "genres": ["Detroit Techno", "Techno"],
        "tracklist": ["Waveform Transmission Vol. 1", "The Bells (Original)", "X-102", "Gamma Player", "The Cane"],
        "description": "Jeff Mills' first full-length release on Berlin's Tresor label, recorded in Detroit and capturing his most ferocious early productions. Hard, relentless, and technically precise — a blueprint for the industrial-influenced techno he would become synonymous with.",
        "historical_significance": "One of the key early releases connecting Detroit Techno to the Berlin techno scene via Tresor Records. Established Jeff Mills as an international figure and demonstrated how Detroit's sound could translate into European club culture.",
        "image_url": ""
    },
    {
        "release_id": "release_ur_galaxy_2_galaxy",
        "title": "Galaxy 2 Galaxy",
        "artist": "Underground Resistance",
        "aliases_used": "Underground Resistance",
        "label_id": "label_underground_resistance",
        "catalog_number": "UR-038",
        "year": 1993,
        "format": "12\"",
        "genres": ["Detroit Techno", "Techno", "Jazz"],
        "tracklist": ["Hi-Tech Jazz", "Galaxy 2 Galaxy", "Transition", "Wavejumper"],
        "description": "Underground Resistance's jazz-infused techno statement, blending the futurism of Detroit Techno with the improvisational spirit of jazz. A record that pointed toward the music's African-American roots while pushing it into new territory.",
        "historical_significance": "Demonstrated that Detroit Techno had intellectual and cultural depth beyond the dancefloor — that it was connected to jazz, funk, and the broader African-American musical tradition. Remains one of UR's most celebrated releases.",
        "image_url": ""
    },
    {
        "release_id": "release_drexciya_unknown_aquatic_habitat",
        "title": "The Unknown Aquatic Habitat",
        "artist": "Drexciya",
        "aliases_used": "Drexciya",
        "label_id": "label_underground_resistance",
        "catalog_number": "UR-035",
        "year": 1994,
        "format": "12\"",
        "genres": ["Detroit Techno", "Electro"],
        "tracklist": ["The Unknown Aquatic Habitat", "Positronic Soun Dellay", "Sea Quake", "Journey Home"],
        "description": "One of Drexciya's earliest and most important releases, establishing the core elements of their mythology and sound — turbocharged electro, submarine pressure, machine funk stripped to its skeleton. Released through the Underground Resistance network.",
        "historical_significance": "The release that introduced Drexciya's underwater mythology to a wider audience and established the template for Detroit Electro's most sustained and visionary artistic project.",
        "image_url": ""
    },
    {
        "release_id": "release_aztec_mystic_jaguar",
        "title": "Jaguar",
        "artist": "DJ Rolando",
        "aliases_used": "Aztec Mystic",
        "label_id": "label_underground_resistance",
        "catalog_number": "UR-053",
        "year": 1999,
        "format": "12\"",
        "genres": ["Detroit Techno", "Techno"],
        "tracklist": ["Jaguar", "Knights of the Jaguar"],
        "description": "Released under the alias Aztec Mystic, Jaguar is one of the most iconic techno records ever made — an orchestral, melodic anthem built on rising string stabs, a driving 909 kick, and an irresistible emotional arc. Underground Resistance at its most euphoric.",
        "historical_significance": "One of the best-selling Underground Resistance releases and a touchstone of melodic techno. Jaguar reached audiences far beyond the techno underground and remains a staple of DJ sets two decades later.",
        "image_url": ""
    },
    {
        "release_id": "release_reese_just_want_another_chance",
        "title": "Just Want Another Chance",
        "artist": "Kevin Saunderson",
        "aliases_used": "Reese",
        "label_id": "label_network_records",
        "catalog_number": "NET 005",
        "year": 1988,
        "format": "12\"",
        "genres": ["Detroit Techno", "House", "Acid House"],
        "tracklist": ["Just Want Another Chance", "Just Want Another Chance (Dub)"],
        "description": "Released under the Reese alias, this record contained the bass line that would define jungle, drum and bass, and countless genres to come. The deep, distorted, sliding sub-bass — produced on a Roland Juno-106 — became known simply as the Reese bass and remains one of electronic music's most sampled sounds.",
        "historical_significance": "The origin of the Reese Bassline — one of the most influential bass sounds in electronic music history. Its impact on jungle and drum and bass in the UK in the early 1990s was immense. A single bass line that spawned a genre.",
        "image_url": ""
    },
    {
        "release_id": "release_model_500_interference",
        "title": "Interference",
        "artist": "Juan Atkins",
        "aliases_used": "Model 500",
        "label_id": "label_metroplex",
        "catalog_number": "MX-009",
        "year": 1990,
        "format": "12\"",
        "genres": ["Detroit Techno", "Electro"],
        "tracklist": ["Interference", "Interference (Remix)", "Sonic Destroyer"],
        "description": "A later Metroplex release from Juan Atkins under the Model 500 alias, Interference showcases his ability to evolve the core Detroit Techno sound while remaining rooted in the cold, futuristic aesthetic he had established in the mid-1980s.",
        "historical_significance": "Part of the essential Model 500 catalog that defined the Metroplex sound and demonstrated Detroit Techno's longevity and adaptability into the early 1990s.",
        "image_url": ""
    },
    {
        "release_id": "release_paperclip_people_climax",
        "title": "The Climax",
        "artist": "Carl Craig",
        "aliases_used": "Paperclip People",
        "label_id": "label_planet_e",
        "catalog_number": "PE-03",
        "year": 1994,
        "format": "12\"",
        "genres": ["Detroit Techno", "Techno", "House"],
        "tracklist": ["The Climax", "Throw", "Just Another"],
        "description": "Released under the Paperclip People alias on his own Planet E label, The Climax shows Carl Craig at his most playful and house-influenced — looser and warmer than his more abstract releases, yet still unmistakably Detroit in its production values.",
        "historical_significance": "Demonstrated Carl Craig's versatility and his label Planet E's role as a home for Detroit Techno that could bridge the gap between pure techno and the dancefloor accessibility of house.",
        "image_url": ""
    },
    {
        "release_id": "release_suburban_knight_art_of_stalking",
        "title": "The Art of Stalking",
        "artist": "Suburban Knight",
        "aliases_used": "Suburban Knight",
        "label_id": "label_transmat",
        "catalog_number": "TM-011",
        "year": 1990,
        "format": "12\"",
        "genres": ["Detroit Techno", "Dark Techno"],
        "tracklist": ["The Art of Stalking", "Nocturbulous Behavior", "My Sol Dark Funk"],
        "description": "James Pennington's defining release on Transmat, The Art of Stalking is among the darkest and most atmospheric records in the early Detroit Techno canon. Where much of Detroit Techno looked outward to the cosmos, Pennington turned inward — paranoid, shadowy, relentless.",
        "historical_significance": "One of the earliest examples of dark techno as a distinct aesthetic within the Detroit sound, prefiguring the industrial-influenced techno that would emerge from Berlin in the early 1990s.",
        "image_url": ""
    },
    {
        "release_id": "release_aux_88_is_it_man_or_machine",
        "title": "Is It Man or Machine?",
        "artist": "Aux 88",
        "aliases_used": "Aux 88",
        "label_id": "label_direct_beat",
        "catalog_number": "DB-001",
        "year": 1995,
        "format": "LP",
        "genres": ["Detroit Techno", "Electro", "Detroit Electro"],
        "tracklist": ["Is It Man or Machine?", "Made in Detroit", "Bass Magnetic", "Electro Invasion", "Tokyo", "Back to the Basics"],
        "description": "Aux 88's debut album on Direct Beat, Is It Man or Machine? is the flagship release of Detroit Electro — robotic vocoder vocals, punishing 808 kicks, and sci-fi aesthetics that drew a straight line from Afrika Bambaataa through Juan Atkins to the duo's own machine-obsessed sound.",
        "historical_significance": "The definitive statement of Detroit Electro as its own genre separate from but deeply connected to Detroit Techno. Aux 88's commitment to the TR-808 and electro tradition in an era when techno had moved away from it proved prescient — electro would enjoy a global revival two decades later.",
        "image_url": ""
    }
]

for release in releases:
    releases_table.put_item(Item=release)
    print(f"Seeded release: {release['title']} by {release['artist']}")

# ─── Events ───────────────────────────────────────────────────

events_table = dynamodb.Table('detroit-techno-events')

events = [
    {
        "event_id": "event_movement_2026",
        "name": "Movement Music Festival 2026",
        "type": "festival",
        "venue_id": "venue_hart_plaza",
        "date": "May 23-25, 2026",
        "year": 2026,
        "status": "historical",
        "lineup": [
            "Carl Cox", "Sara Landry", "Dom Dolla", "Juan Atkins",
            "Richie Hawtin", "Carl Craig b2b Cajmere", "E-Dancer (Kevin Saunderson & Dantiez)",
            "Boys Noize b2b MCR-T", "Danny Brown", "The Dare",
            "Nia Archives", "Blawan", "Courtesy", "Dax J",
            "Delano Smith", "Detroit Techno Militia", "DJ Godfather",
            "DJ Harvey", "Claude VonStroke", "Octo Octa",
            "Barry Can't Swim", "Mochakk", "999999999",
            "Collabs3000 (Chris Liebing & Speedy J)", "Audion"
        ],
        "description": "The 20th anniversary edition of Movement Music Festival, held at Hart Plaza on the Detroit Riverfront over Memorial Day Weekend. Over 115 acts performed across six stages across three days. Headlined by Carl Cox, Sara Landry, and Dom Dolla, with strong representation from Detroit legends including Juan Atkins, Richie Hawtin, Carl Craig, and Kevin Saunderson. The KMS Records showcase anchored the Detroit legacy programming.",
        "historical_significance": "The 20th anniversary edition of Paxahau's stewardship of the festival, which began as the Detroit Electronic Music Festival (DEMF) in 2000. Movement 2026 brought together three generations of electronic music — from Detroit Techno originators to contemporary global talent — on the riverfront where the genre was born.",
        "image_url": ""
    }
]

for event in events:
    events_table.put_item(Item=event)
    print(f"Seeded event: {event['name']}")

# ─── Gear ───────────────────────────────────────────────────

gear_table = dynamodb.Table('detroit-techno-gear')

gear = [
    {
        "gear_id": "gear_sequential_prophet5",
        "name": "Sequential Circuits Prophet-5",
        "manufacturer": "Sequential Circuits",
        "type": "synthesizer",
        "released_year": 1978,
        "description": "The world's first fully programmable polyphonic synthesizer — five voices, fully analog signal path, and onboard memory for 120 patches. The Prophet-5's warm, lush sound became a defining texture of late 1970s and 1980s pop, jazz, and electronic music. In Detroit, it provided the chord stabs and pad textures that gave early Detroit Techno its sense of space.",
        "notable_users": ["Juan Atkins", "Derrick May", "Giorgio Moroder"],
        "historical_significance": "The Prophet-5 set the standard for analog polyphonic synthesizers and remains one of the most influential instruments in electronic music history. Its programmability was revolutionary — for the first time, a synthesizer could reliably recall a sound.",
        "image_url": ""
    },
    {
        "gear_id": "gear_moog_source",
        "name": "Moog Source",
        "manufacturer": "Moog Music",
        "type": "synthesizer",
        "released_year": 1981,
        "description": "A monophonic analog synthesizer from Moog featuring a membrane touch panel instead of traditional knobs — an unusual design choice that made it less intuitive to program but deeply expressive to play. The Source has a characteristically aggressive, cutting tone, particularly in the bass and lead registers, that became prized in underground electronic music.",
        "notable_users": ["Underground Resistance", "Mad Mike Banks"],
        "historical_significance": "Used within the Underground Resistance circle for its aggressive tone and raw character. The Moog Source contributed to the harder, more confrontational sound of UR's most militant releases.",
        "image_url": ""
    },
    {
        "gear_id": "gear_ensoniq_esq1",
        "name": "Ensoniq ESQ-1",
        "manufacturer": "Ensoniq",
        "type": "synthesizer",
        "released_year": 1986,
        "description": "A hybrid digital/analog synthesizer that combined digital oscillators with analog filters — giving it a sound somewhere between the warmth of analog and the precision of digital synthesis. The ESQ-1 was affordable at launch and became widely used in Detroit studios. Its built-in sequencer made it particularly useful for writing patterns.",
        "notable_users": ["Derrick May", "Anthony Shakir", "Kevin Saunderson"],
        "historical_significance": "One of the workhorses of Detroit Techno's second wave. The ESQ-1's affordability opened synthesis to a wider range of Detroit producers and its built-in sequencer was used to develop the interlocking patterns that defined the Detroit sound.",
        "image_url": ""
    },
    {
        "gear_id": "gear_oberheim_matrix1000",
        "name": "Oberheim Matrix-1000",
        "manufacturer": "Oberheim",
        "type": "synthesizer",
        "released_year": 1987,
        "description": "A rack-mounted analog synthesizer with 1000 preset patches and no front-panel programming — a synthesis engine in a box, intended for studio use as a preset expander. Despite its limitations, the Matrix-1000 contains the Oberheim Matrix-6 sound engine, giving it the lush, warm character associated with the Oberheim name at a fraction of the cost.",
        "notable_users": ["Carl Craig", "Richie Hawtin"],
        "historical_significance": "The Matrix-1000 made the Oberheim analog sound accessible to producers who couldn't afford the larger Matrix-6 or Matrix-12. Its warm pad and bass tones appeared across countless Detroit and Chicago productions in the late 1980s and early 1990s.",
        "image_url": ""
    }
]

for item in gear:
    gear_table.put_item(Item=item)
    print(f"Seeded gear: {item['name']}")

print("\n✓ Wave 3 seed complete.")
print(f"  Artists:  {len(artists)}")
print(f"  Labels:   {len(labels)}")
print(f"  Releases: {len(releases)}")
print(f"  Events:   {len(events)}")
print(f"  Gear:     {len(gear)}")
print(f"  Total:    {len(artists) + len(labels) + len(releases) + len(events) + len(gear)} new entries")