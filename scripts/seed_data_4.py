import boto3

session = boto3.Session(profile_name='techno-archive-dev', region_name='us-east-1')
dynamodb = session.resource('dynamodb')

# ─── Artists ───────────────────────────────────────────────────

artists_table = dynamodb.Table('detroit-techno-artists')

artists = [
    {
        "artist_id": "artist_kenny_larkin",
        "name": "Kenny Larkin",
        "birth_name": "Kenny Larkin",
        "born": "1967",
        "origin": "Detroit, MI",
        "active_years": "1991 - present",
        "genres": ["Detroit Techno", "Techno", "Electro"],
        "aliases": ["Dark Comedy"],
        "associated_labels": ["label_plus_8"],
        "associated_acts": [],
        "biography": "Kenny Larkin is a Detroit-born producer who came up in the city's second wave of techno talent, studying music at Wayne State University and developing under the influence of Juan Atkins and the Metroplex circle. Where many of his contemporaries pursued austerity, Larkin developed a warmer, more melodic approach to Detroit Techno — one that preserved the music's emotional depth while opening it toward funk and soul. His debut album Azimuth (1994, R&S Records) announced him as a major figure, and his series of Plus 8 releases placed him in the international club circuit early in his career. His alias Dark Comedy reflected a dry wit that ran beneath his technically immaculate productions.",
        "notable_tracks": ["Yoyo", "Dance of Life", "Tedra", "Dark Comedy", "Azimuth"],
        "gear": ["Roland TR-909", "Roland Juno-106", "Sequential Circuits Prophet-5"],
        "image_url": ""
    },
    {
        "artist_id": "artist_dj_minx",
        "name": "DJ Minx",
        "birth_name": "Jennifer Witcher",
        "born": "1969",
        "origin": "Detroit, MI",
        "active_years": "1988 - present",
        "genres": ["Detroit Techno", "House", "Deep House"],
        "aliases": ["Minx"],
        "associated_labels": ["label_women_on_wax"],
        "associated_acts": [],
        "biography": "Jennifer Witcher — known as DJ Minx — is one of Detroit's most important underground DJs and a foundational figure in the city's music community. She began DJing in the late 1980s at a time when few women were visible in Detroit's techno and house scene, and went on to become a resident at key underground spaces including venues within the Submerge network. In the mid-1990s she founded Women on Wax Recordings, a Detroit imprint dedicated to platforming female and femme-identifying producers in a genre long dominated by men. She has remained a tireless advocate for Detroit's underground dance culture across four decades.",
        "notable_tracks": ["After Hours", "What Goes On", "Voices from the Shadows", "Come Into My World"],
        "gear": ["Technics SL-1200", "Roland TR-909"],
        "image_url": ""
    },
    {
        "artist_id": "artist_omar_s",
        "name": "Omar S",
        "birth_name": "Alex Omar Smith",
        "born": "1977",
        "origin": "Detroit, MI",
        "active_years": "2002 - present",
        "genres": ["Detroit Techno", "House", "Deep House"],
        "aliases": [],
        "associated_labels": ["label_fxhe"],
        "associated_acts": [],
        "biography": "Alex Omar Smith — known universally as Omar S — is one of Detroit's most prolific and beloved underground producers. Operating through his own FXHE Records imprint, he has released dozens of records in a raw, deliberately unpolished aesthetic that rejects the slick production values of commercial electronic music. His output is deeply rooted in the Detroit tradition — emotional, groove-driven, and irreverent — with house, funk, and soul woven through a characteristically abrasive but soulful sound. His motto, 'For Those That Knoe,' signals a commitment to an underground of in-the-know listeners rather than mainstream approval.",
        "notable_tracks": ["Thank U 4 Letting Me Be Myself", "Here's What I Know You Want", "The Shit (U Should Know by Now)", "New Day"],
        "gear": ["Roland TR-909", "Roland TR-808", "Akai MPC60"],
        "image_url": ""
    },
    {
        "artist_id": "artist_dopplereffekt",
        "name": "Dopplereffekt",
        "birth_name": "Gerald Donald",
        "born": "Unknown",
        "origin": "Detroit, MI",
        "active_years": "1994 - present",
        "genres": ["Detroit Techno", "Electro", "Electronic Body Music", "Industrial"],
        "aliases": ["Heinrich Mueller", "Japanese Telecom", "Arpanet"],
        "associated_labels": ["label_underground_resistance"],
        "associated_acts": ["Drexciya", "Underground Resistance"],
        "biography": "Dopplereffekt is the principal project of Gerald Donald — one half of Drexciya — operating under the alias Heinrich Mueller. More austere and conceptually rigorous than Drexciya, Dopplereffekt draws on German Electronic Body Music, industrial electronics, and the cold precision of scientific language to build machine music of extraordinary density. The project's visual and conceptual identity is deliberately clinical — drawing on Kraftwerk's aesthetics while remaining rooted in the African-American Detroit tradition. Their 1994 debut Gesamtkunstwerk is one of the most singular recordings to emerge from the Detroit underground, predating the wider international interest in cold, EBM-influenced techno by years.",
        "notable_tracks": ["Sterilization", "Infophysix", "Pornoviewer", "Superior Race", "Cellular Automata"],
        "gear": ["Roland TR-808", "Korg MS-20"],
        "image_url": ""
    },
    {
        "artist_id": "artist_terrence_dixon",
        "name": "Terrence Dixon",
        "birth_name": "Terrence Dixon",
        "born": "1974",
        "origin": "Detroit, MI",
        "active_years": "1997 - present",
        "genres": ["Detroit Techno", "Minimal Techno", "Techno"],
        "aliases": ["Population One", "T. Dixon"],
        "associated_labels": ["label_population_one", "label_tresor"],
        "associated_acts": [],
        "biography": "Terrence Dixon is a Detroit producer whose work sits at the intersection of Detroit Techno's emotional depth and the austerity of minimal production. Operating through his Population One imprint, he has built a catalog of deeply introspective techno that explores isolation, spirituality, and inner life through rhythm and texture. His From the Far Future series — records that sound genuinely alien while remaining rooted in the Detroit tradition — are among the most critically admired productions to emerge from the city in the 2000s, influencing a generation of producers drawn to the overlap between sound and inner experience.",
        "notable_tracks": ["From the Far Future", "Collapse", "Your Mind is a Temple", "Blank Expressions", "Cosmic Abstract"],
        "gear": ["Roland TR-909", "Roland TR-808", "Ensoniq ESQ-1"],
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
        "label_id": "label_fxhe",
        "name": "FXHE Records",
        "variations": ["For Those That Knoe"],
        "founded": 2002,
        "founder": "Omar S",
        "origin": "Detroit, MI",
        "genres": ["Detroit Techno", "House", "Deep House"],
        "associated_artists": ["artist_omar_s"],
        "description": "FXHE Records — the name abbreviates 'For Those That Knoe' — is Omar S's self-owned Detroit imprint and one of the most respected underground electronic labels in the world. Its releases are characterized by deliberately lo-fi aesthetics: handwritten labels, rough sleeve artwork, and an uncompromising sonic identity that prizes rawness over polish. FXHE operates entirely outside the mainstream music industry, distributing records directly to DJs and independent record stores.",
        "historical_significance": "FXHE embodies the Detroit tradition of artist-owned, community-rooted label operations at its most uncompromising. It demonstrated that raw, unpolished production is a strength — influencing a generation of producers who pushed back against the trend toward clean, overproduced electronic music in the 2000s.",
        "image_url": ""
    },
    {
        "label_id": "label_women_on_wax",
        "name": "Women on Wax",
        "variations": ["Women on Wax Recordings"],
        "founded": 1996,
        "founder": "DJ Minx",
        "origin": "Detroit, MI",
        "genres": ["Detroit Techno", "House", "Deep House"],
        "associated_artists": ["artist_dj_minx"],
        "description": "Women on Wax is the Detroit label founded by DJ Minx in the mid-1990s to create visibility for female and femme-identifying producers in electronic music. The label has released house and techno across several decades, maintaining its grassroots Detroit identity while advocating for a more inclusive underground.",
        "historical_significance": "One of the first DJ- and producer-led imprints in Detroit dedicated explicitly to gender equity in electronic music. Women on Wax filled a visible gap in the city's scene and has been a consistent presence for nearly three decades.",
        "image_url": ""
    },
    {
        "label_id": "label_population_one",
        "name": "Population One",
        "variations": [],
        "founded": 1997,
        "founder": "Terrence Dixon",
        "origin": "Detroit, MI",
        "genres": ["Detroit Techno", "Minimal Techno"],
        "associated_artists": ["artist_terrence_dixon"],
        "description": "Population One is Terrence Dixon's self-owned imprint and the name he uses as a primary artist alias. The label reflects Dixon's deeply personal and introspective approach to Detroit Techno — stripped-back, spiritual, and emotionally austere. Releases are distributed through the Submerge network.",
        "historical_significance": "Population One is part of the tradition of Detroit producers creating their own infrastructure to release music independently of major labels or mainstream distribution. It has been the vehicle for some of Detroit Techno's most thoughtful and emotionally complex work of the 2000s.",
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
        "release_id": "release_carl_craig_landcruising",
        "title": "Landcruising",
        "artist": "Carl Craig",
        "aliases_used": "Carl Craig",
        "label_id": "label_planet_e",
        "catalog_number": "PE-005",
        "year": 1995,
        "format": "LP",
        "genres": ["Detroit Techno", "Techno", "House", "Electronic"],
        "tracklist": ["Science Fiction", "La Ferme des Animaux", "At Les", "Throw", "Frustration", "Darkness"],
        "description": "Carl Craig's landmark studio album on his own Planet E label, Landcruising moves across the full spectrum of Detroit electronic music — from hard, functional techno to jazz-influenced abstraction to raw house grooves. Recorded under his own name rather than any of his many aliases, it announced Craig as a fully realized artist capable of sustaining a statement across LP format.",
        "historical_significance": "One of the definitive Detroit Techno albums of the 1990s. Landcruising demonstrated that the genre's ambitions could extend beyond the 12-inch format and placed Carl Craig alongside Juan Atkins and Derrick May as one of the central figures of the entire movement.",
        "image_url": ""
    },
    {
        "release_id": "release_model_500_night_drive",
        "title": "Night Drive (Thru-Babylon)",
        "artist": "Juan Atkins",
        "aliases_used": "Model 500",
        "label_id": "label_metroplex",
        "catalog_number": "MX-002",
        "year": 1985,
        "format": "12\"",
        "genres": ["Detroit Techno", "Electro"],
        "tracklist": ["Night Drive (Thru-Babylon)", "Night Drive (Thru-Babylon) (Dub)"],
        "description": "One of the earliest Model 500 releases on Metroplex, Night Drive (Thru-Babylon) is a cold, hypnotic slice of early Detroit electronic music — urban, cinematic, and machine-precise. Its imagery of driving through an alienated cityscape captures the Metroplex aesthetic in miniature and the profound influence of Alvin Toffler's The Third Wave on Juan Atkins's thinking about technology and society.",
        "historical_significance": "Among the earliest documents of what would become Detroit Techno, Night Drive captures the genre at its very beginning — synthesizer-driven, future-facing, rooted in the alienated machine music of Kraftwerk and the electro of Afrika Bambaataa but unmistakably shaped by the specific landscape of post-industrial Detroit.",
        "image_url": ""
    },
    {
        "release_id": "release_ur_interstellar_fugitives",
        "title": "Interstellar Fugitives",
        "artist": "Underground Resistance",
        "aliases_used": "Various UR artists",
        "label_id": "label_underground_resistance",
        "catalog_number": "UR-045",
        "year": 1998,
        "format": "LP",
        "genres": ["Detroit Techno", "Electro", "House", "Jazz"],
        "tracklist": ["Interstellar Fugitives", "Hi-Tech Jazz", "Punisher", "Elimination", "Combat Stance", "Riot", "From the Banks of the Nile"],
        "description": "Underground Resistance's sprawling compilation documenting the full range of their collective and its associated aliases. Spanning techno, electro, house, and jazz-influenced abstraction, Interstellar Fugitives presents the UR universe as a cohesive artistic statement — the work of a genuine underground movement with a consistent philosophy, not a loose collection of one-off releases.",
        "historical_significance": "The most comprehensive document of the Underground Resistance collective's reach and depth. Interstellar Fugitives introduced many listeners to the full scope of UR's operations and cemented the collective's reputation as the most important organizational force in Detroit Techno.",
        "image_url": ""
    },
    {
        "release_id": "release_eddie_fowlkes_goodbye_kiss",
        "title": "Goodbye Kiss",
        "artist": "Eddie Fowlkes",
        "aliases_used": "Eddie Fowlkes",
        "label_id": "label_metroplex",
        "catalog_number": "MX-005",
        "year": 1986,
        "format": "12\"",
        "genres": ["Detroit Techno", "House", "Electronic"],
        "tracklist": ["Goodbye Kiss", "Goodbye Kiss (Instrumental)"],
        "description": "One of Eddie Fowlkes's earliest releases and among the first Metroplex records not credited to Juan Atkins himself. Goodbye Kiss is soulful and minimal — a record that sits at the seam between Chicago House and the emerging Detroit Techno sound, reflecting Fowlkes's role as a connector between the two cities.",
        "historical_significance": "Eddie Fowlkes is one of the original Detroit DJs — a peer of Juan Atkins, Derrick May, and Kevin Saunderson from their shared time at Belleville High School. Goodbye Kiss places him in the Metroplex founding generation and documents the Detroit-Chicago cross-pollination that shaped both scenes in their earliest years.",
        "image_url": ""
    },
    {
        "release_id": "release_omar_s_thank_you",
        "title": "Thank U 4 Letting Me Be Myself",
        "artist": "Omar S",
        "aliases_used": "Omar S",
        "label_id": "label_fxhe",
        "catalog_number": "FXHE-005",
        "year": 2007,
        "format": "12\"",
        "genres": ["Detroit Techno", "House"],
        "tracklist": ["Thank U 4 Letting Me Be Myself", "New Day"],
        "description": "One of Omar S's most celebrated releases on FXHE, Thank U 4 Letting Me Be Myself captures his characteristic blend of raw production, emotional directness, and deep groove. The title's irreverent spelling reflects his refusal to package Detroit music for mainstream consumption — authenticity over marketability, every time.",
        "historical_significance": "A key release in the revival of interest in raw, unpolished Detroit electronic music during the mid-2000s. Omar S and FXHE became reference points for a generation of producers reacting against the trend toward cleaner, more commercial sounds in global club culture.",
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
        "event_id": "event_demf_2000",
        "name": "Detroit Electronic Music Festival 2000",
        "type": "festival",
        "venue_id": "venue_hart_plaza",
        "date": "May 27-29, 2000",
        "year": 2000,
        "status": "historical",
        "lineup": [
            "Juan Atkins", "Derrick May", "Kevin Saunderson",
            "Richie Hawtin", "Carl Craig", "Jeff Mills",
            "Underground Resistance", "Blake Baxter", "Stacey Pullen",
            "DJ Rolando", "Claude Young", "Robert Hood",
            "Octave One", "Aux 88", "DJ Minx"
        ],
        "description": "The inaugural Detroit Electronic Music Festival — the largest free electronic music festival in history at the time. Organized by Carol Marvin and produced with Carl Craig, DEMF 2000 was held over Memorial Day Weekend at Hart Plaza on the Detroit Riverfront and drew an estimated 1 million attendees. For the first time, virtually the entire Detroit Techno canon performed together in their home city at a scale that matched the global significance of the music they had created.",
        "historical_significance": "DEMF 2000 was a watershed moment for Detroit Techno — a public recognition of the genre's cultural and historical importance in the city where it was born. The event established Hart Plaza as the permanent home of Detroit's annual electronic music celebration and laid the groundwork for what would become the Movement Electronic Music Festival.",
        "image_url": ""
    }
]

for event in events:
    events_table.put_item(Item=event)
    print(f"Seeded event: {event['name']}")

# ─── Venues ───────────────────────────────────────────────────

venues_table = dynamodb.Table('detroit-techno-venues')

venues = [
    {
        "venue_id": "venue_st_andrews_hall",
        "name": "St. Andrew's Hall",
        "status": "active",
        "opened": 1907,
        "closed": None,
        "address": "431 E Congress St, Detroit, MI 48226",
        "neighborhood": "Downtown",
        "city": "Detroit, MI",
        "capacity": 1000,
        "type": "concert hall / club",
        "genres": ["Detroit Techno", "Electronic", "Alternative", "Rock"],
        "historical_significance": "A historic multi-room venue in Downtown Detroit that has hosted underground music of every kind since the early 20th century. The main hall hosted techno and electronic music events through the 1990s and 2000s, while the downstairs Shelter (a separate venue in the same building) became one of Detroit's most important underground dance spaces. Together the two rooms formed one of Detroit's most significant live music buildings.",
        "notable_events": [],
        "notable_artists_performed": ["Jeff Mills", "Richie Hawtin", "Derrick May", "Juan Atkins", "Carl Craig"],
        "image_url": ""
    },
    {
        "venue_id": "venue_bookies_club",
        "name": "Bookies Club 870",
        "status": "closed",
        "opened": 1978,
        "closed": 1982,
        "address": "870 Michigan Ave, Detroit, MI",
        "neighborhood": "Corktown",
        "city": "Detroit, MI",
        "capacity": None,
        "type": "club",
        "genres": ["Punk", "New Wave", "Post-Punk", "Electronic"],
        "historical_significance": "Detroit's seminal punk and new wave club of the late 1970s, Bookies Club 870 was the crucible from which the city's experimental music scene emerged. Many of the teenagers who attended Bookies — exposed to synthesizer-driven European post-punk and the early electro of Afrika Bambaataa — went on to create Detroit Techno. A generation of Detroit artists trace their musical consciousness directly to this venue.",
        "notable_events": [],
        "notable_artists_performed": ["Various punk, new wave, and electronic acts from the late 1970s"],
        "image_url": ""
    },
    {
        "venue_id": "venue_marble_bar",
        "name": "Marble Bar",
        "status": "closed",
        "opened": 1978,
        "closed": 1988,
        "address": "1501 Michigan Ave, Detroit, MI",
        "neighborhood": "Corktown",
        "city": "Detroit, MI",
        "capacity": None,
        "type": "bar / club",
        "genres": ["Punk", "New Wave", "Electronic", "Alternative"],
        "historical_significance": "The Marble Bar was Detroit's foremost alternative underground venue through the early 1980s, hosting punk, new wave, and experimental electronic music events that introduced the next generation of Detroit producers to synthesizer-driven music from Germany, the UK, and New York. Like Bookies Club, it is considered part of the cultural pre-history of Detroit Techno — a space where the musical influences that produced the genre were first absorbed by future artists.",
        "notable_events": [],
        "notable_artists_performed": ["Various underground acts from the Detroit punk and new wave era"],
        "image_url": ""
    }
]

for venue in venues:
    venues_table.put_item(Item=venue)
    print(f"Seeded venue: {venue['name']}")

# ─── Gear ───────────────────────────────────────────────────

gear_table = dynamodb.Table('detroit-techno-gear')

gear = [
    {
        "gear_id": "gear_roland_jupiter8",
        "name": "Roland Jupiter-8",
        "manufacturer": "Roland Corporation",
        "type": "synthesizer",
        "released_year": 1981,
        "description": "An eight-voice polyphonic analog synthesizer with dual oscillators per voice, a resonant four-pole low-pass filter, and a distinctive warm, wide character. The Jupiter-8's lush pads and expressive arpeggiated sequences made it one of the defining synthesizers of the 1980s. It was expensive at launch but found its way into Detroit studios through the used-gear market.",
        "notable_users": ["Juan Atkins", "Derrick May", "Kevin Saunderson"],
        "historical_significance": "The Jupiter-8 contributed the wide, warm polyphonic textures that gave early Detroit Techno its sense of cosmic scale — its pads and arpeggios fill the space between drums and bass in many classic records. It served as the emotional counterpart to the colder, more digital DX7 and the more functional Juno-106.",
        "image_url": ""
    },
    {
        "gear_id": "gear_akai_s950",
        "name": "Akai S950",
        "manufacturer": "Akai Professional",
        "type": "sampler",
        "released_year": 1988,
        "description": "A 12-bit stereo sampler offering up to 2.25 MB of sample memory and eight-voice polyphony. The S950 was a streamlined, more affordable successor to the S900, capable of sampling at up to 40kHz. Its 12-bit converters introduced a characteristic warmth and slight grit that made it a preferred tool for Detroit and Chicago producers who valued the character that digital sampling's imperfections could bring to otherwise machine-driven music.",
        "notable_users": ["Carl Craig", "Richie Hawtin", "Octave One"],
        "historical_significance": "The Akai S-series samplers were central to second-wave Detroit Techno in the late 1980s and early 1990s, allowing producers to incorporate live sounds, found audio, and jazz samples into their machine-driven productions. This capacity for human warmth and organic texture is one reason Detroit Techno retained an emotional dimension that purely synthetic European productions often lacked.",
        "image_url": ""
    },
    {
        "gear_id": "gear_sequential_six_trak",
        "name": "Sequential Circuits Six-Trak",
        "manufacturer": "Sequential Circuits",
        "type": "synthesizer",
        "released_year": 1984,
        "description": "A six-voice analog polyphonic synthesizer and the first commercially available multitimbral synthesizer — capable of playing six different sounds simultaneously across MIDI channels. Priced below the Prophet-5, the Six-Trak offered a credible analog synthesis platform for producers on limited budgets. Its built-in sequencer provided compositional flexibility that more expensive synthesizers lacked.",
        "notable_users": ["Juan Atkins", "Derrick May"],
        "historical_significance": "The Six-Trak's multitimbral capability and affordability made it an accessible entry point for Detroit producers who needed polyphonic synthesis without the cost of the Prophet-5. Its distinct analog character and built-in sequencer appear in early Detroit productions and it is part of the first generation of MIDI instruments that defined the Detroit studio.",
        "image_url": ""
    },
    {
        "gear_id": "gear_roland_mc202",
        "name": "Roland MC-202 MicroComposer",
        "manufacturer": "Roland Corporation",
        "type": "sequencer / synthesizer",
        "released_year": 1983,
        "description": "A step-sequencer combined with a built-in monophonic SH-101-based synthesizer — effectively a compact, keyboard-less SH-101 with step-programming capabilities. The MC-202's synth engine produced the same cutting bass and lead tones as the SH-101, while its two-track sequencer allowed complex melodic and bass patterns to be programmed and looped. Like the TB-303, it initially underperformed commercially and was sold cheaply on the used market, where Detroit producers found it.",
        "notable_users": ["Robert Hood", "Derrick May", "Suburban Knight"],
        "historical_significance": "An underappreciated but important piece of the Detroit Techno toolbox. The MC-202 provided tight bass and lead tones and a flexible step-sequencer that allowed producers to build interlocking melodic patterns alongside the rhythmic patterns of the TR-808 and TR-909 — expanding the compositional range of the classic Detroit studio setup.",
        "image_url": ""
    }
]

for item in gear:
    gear_table.put_item(Item=item)
    print(f"Seeded gear: {item['name']}")

print("\n✓ Wave 4 seed complete.")
print(f"  Artists:  {len(artists)}")
print(f"  Labels:   {len(labels)}")
print(f"  Releases: {len(releases)}")
print(f"  Events:   {len(events)}")
print(f"  Venues:   {len(venues)}")
print(f"  Gear:     {len(gear)}")
print(f"  Total:    {len(artists) + len(labels) + len(releases) + len(events) + len(venues) + len(gear)} new entries")
