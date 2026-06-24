import boto3

session = boto3.Session(profile_name='techno-archive-dev', region_name='us-east-1')
dynamodb = session.resource('dynamodb')

# ─── Artists ───────────────────────────────────────────────────

artists_table = dynamodb.Table('detroit-techno-artists')

artists = [
    {
        "artist_id": "artist_stacey_pullen",
        "name": "Stacey Pullen",
        "birth_name": "Stacey Pullen",
        "born": "1970",
        "origin": "Detroit, MI",
        "active_years": "1991 - present",
        "genres": ["Detroit Techno", "Deep Techno", "House"],
        "aliases": ["Bango", "Silent Phase", "Kosmic Messenger"],
        "associated_labels": ["label_transmat", "label_planet_e"],
        "associated_acts": [],
        "biography": "A second-generation Detroit Techno producer who studied under Derrick May and released early work on Transmat. Known for a deeper, more hypnotic strain of Detroit Techno that influenced the minimal techno movement of the 2000s. His aliases Bango and Silent Phase produced some of the most sought-after Detroit records of the 1990s.",
        "notable_tracks": ["Elevation", "Fiery Flower", "Lost In My Own World", "Cosmic Movement"],
        "gear": ["Roland TR-909", "Roland Juno-106", "Korg M1"],
        "image_url": ""
    },
    {
        "artist_id": "artist_chez_damier",
        "name": "Chez Damier",
        "birth_name": "Chez Damier",
        "born": "1964",
        "origin": "Detroit, MI",
        "active_years": "1987 - present",
        "genres": ["Detroit Techno", "Deep House", "House"],
        "aliases": [],
        "associated_labels": ["label_kms_records", "label_transmat", "label_royal_oak"],
        "associated_acts": [],
        "biography": "Co-owner of The Music Institute alongside Alton Miller and George Baker — the first dedicated techno club in Detroit. A pivotal but often under-credited figure in the scene's early development. His deep, soulful take on Detroit Techno and house music was influential on Chicago producers and the European deep house movement. Founded Royal Oak Music with Ron Trent.",
        "notable_tracks": ["Can You Feel It", "Forever Monna", "I Never Knew Love"],
        "gear": ["Roland TR-909", "Roland TR-808", "Roland Juno-106"],
        "image_url": ""
    },
    {
        "artist_id": "artist_alan_oldham",
        "name": "Alan Oldham",
        "birth_name": "Alan Oldham",
        "born": "1966",
        "origin": "Detroit, MI",
        "active_years": "1988 - present",
        "genres": ["Detroit Techno", "Hard Techno"],
        "aliases": ["DJ T-1000"],
        "associated_labels": ["label_tresor", "label_axis"],
        "associated_acts": [],
        "biography": "A Detroit Techno producer and DJ who also worked as a comic book artist, illustrating the Detroit Metro Times strip Johnny Nemo. His DJ T-1000 alias became synonymous with a harder, more industrial strain of Detroit Techno that found a natural home in Berlin's Tresor club. One of the scene's most versatile creative figures.",
        "notable_tracks": ["Bionic", "Cyberlord", "Aggressor", "Into the Machine"],
        "gear": ["Roland TR-909", "Roland TR-808"],
        "image_url": ""
    },
    {
        "artist_id": "artist_claude_young",
        "name": "Claude Young",
        "birth_name": "Claude Young Jr.",
        "born": "1969",
        "origin": "Detroit, MI",
        "active_years": "1989 - present",
        "genres": ["Detroit Techno", "Electro", "Drum and Bass"],
        "aliases": [],
        "associated_labels": ["label_tresor"],
        "associated_acts": [],
        "biography": "A Detroit-born DJ and producer renowned for his technical turntablism and ferocious mixing style. A regular at Tresor in Berlin and a key figure in spreading the Detroit sound across Europe in the 1990s. His productions span electro, techno, and drum and bass, always underpinned by the Detroit aesthetic of disciplined machine funk.",
        "notable_tracks": ["What Happened", "Impulse", "Metaphysics"],
        "gear": ["Roland TR-909", "Technics SL-1200", "Roland TR-808"],
        "image_url": ""
    },
    {
        "artist_id": "artist_cybotron",
        "name": "Cybotron",
        "birth_name": "",
        "born": "",
        "origin": "Detroit, MI",
        "active_years": "1980 - 1985",
        "genres": ["Electro", "Proto-Techno", "Synth-Funk"],
        "aliases": [],
        "associated_labels": ["label_deep_space", "label_fantasy_records"],
        "associated_acts": [],
        "biography": "The duo of Juan Atkins and Vietnam veteran Rick Davis. Cybotron is the direct precursor to Detroit Techno — their electro-funk records absorbed the influence of Kraftwerk, Parliament-Funkadelic, and Giorgio Moroder and transmuted it into something entirely new. Clear (1983) is widely cited as the first Detroit Techno record. Their breakup led Juan Atkins to found Metroplex and launch the next phase of the movement.",
        "notable_tracks": ["Alleys of Your Mind", "Cosmic Cars", "Clear", "Enter"],
        "gear": ["Roland TR-808", "Korg MS-20", "Roland SH-101", "Oberheim DMX"],
        "image_url": ""
    },
    {
        "artist_id": "artist_underground_resistance",
        "name": "Underground Resistance",
        "birth_name": "",
        "born": "",
        "origin": "Detroit, MI",
        "active_years": "1989 - present",
        "genres": ["Detroit Techno", "Industrial Techno", "Electro", "Hardcore Techno"],
        "aliases": ["UR", "X-101", "X-102", "Galaxy 2 Galaxy", "Interstellar Fugitives"],
        "associated_labels": ["label_underground_resistance"],
        "associated_acts": [],
        "biography": "Founded in 1989 by Mad Mike Banks and Jeff Mills, with Robert Hood joining shortly after. Underground Resistance operates as a fiercely independent collective — part record label, part resistance movement. Their aesthetic is deliberately confrontational: black hoods, military discipline, anonymity, and uncompromising machine music. Their slogan Resist the Mainstream is not marketing — it is a philosophy carried through every release. One of the most influential and uncompromising forces in the history of techno.",
        "notable_tracks": ["Electronic Warfare", "Jaguar", "Riot", "Frictional Nevada", "Galaxy 2 Galaxy"],
        "gear": ["Roland TR-909", "Roland TR-808", "Oberheim Matrix-1000", "Roland TB-303"],
        "image_url": ""
    }
]

# ─── Labels ────────────────────────────────────────────────────
# Includes all labels referenced by existing artist entries that have no seed yet

labels_table = dynamodb.Table('detroit-techno-labels')

labels = [
    {
        "label_id": "label_network_records",
        "name": "Network Records",
        "variations": ["Network"],
        "founded": 1989,
        "founder": ["Neil Rushton"],
        "origin": "Birmingham, UK",
        "contact": "",
        "parent_label": "",
        "sublabels": [],
        "distribution": "Independent",
        "genres": ["Detroit Techno", "House", "Electronic"],
        "profile": "A Birmingham-based UK label founded by Neil Rushton that played a crucial role in bringing Detroit Techno to European audiences. Compiled and released Techno! The New Dance Sound of Detroit in 1988 — the first major compilation to present Detroit Techno to a mainstream international audience — in partnership with Virgin Records. Licensed and released records by Juan Atkins, Kevin Saunderson, and others.",
        "notable_artists": ["Juan Atkins", "Kevin Saunderson", "Derrick May"],
        "notable_releases": ["Techno! The New Dance Sound of Detroit"],
        "links": {},
        "image_url": ""
    },
    {
        "label_id": "label_planet_e",
        "name": "Planet E Communications",
        "variations": ["Planet E", "Planet E Records"],
        "founded": 1991,
        "founder": ["Carl Craig"],
        "origin": "Detroit, MI",
        "contact": "",
        "parent_label": "",
        "sublabels": [],
        "distribution": "Submerge",
        "genres": ["Detroit Techno", "Deep Techno", "House", "Electronic"],
        "profile": "Founded by Carl Craig in 1991. Planet E became one of the defining labels of second-generation Detroit Techno — deeper, more atmospheric, and more jazz-influenced than the first wave. Home to Craig's many aliases as well as key releases from Stacey Pullen and others.",
        "notable_artists": ["Carl Craig", "Stacey Pullen", "BFC", "Paperclip People", "Innerzone Orchestra"],
        "notable_releases": [],
        "links": {},
        "image_url": ""
    },
    {
        "label_id": "label_plus_8",
        "name": "Plus 8 Records",
        "variations": ["Plus 8", "+8"],
        "founded": 1990,
        "founder": ["Richie Hawtin", "John Acquaviva"],
        "origin": "Windsor, Ontario / Detroit, MI",
        "contact": "",
        "parent_label": "",
        "sublabels": [],
        "distribution": "Independent",
        "genres": ["Detroit Techno", "Acid Techno", "Hard Techno"],
        "profile": "Co-founded by Richie Hawtin and John Acquaviva in 1990. Plus 8 defined a harder, more industrial strain of Detroit-influenced techno that was hugely influential on the European rave scene. Released key early records by Hawtin's FUSE alias and helped establish the Windsor/Detroit corridor as a hotbed of techno innovation.",
        "notable_artists": ["Richie Hawtin", "John Acquaviva", "FUSE", "Speedy J"],
        "notable_releases": [],
        "links": {},
        "image_url": ""
    },
    {
        "label_id": "label_minus",
        "name": "Minus",
        "variations": ["Minus Records", "M_nus"],
        "founded": 1998,
        "founder": ["Richie Hawtin"],
        "origin": "Windsor, Ontario",
        "contact": "",
        "parent_label": "",
        "sublabels": [],
        "distribution": "Independent",
        "genres": ["Minimal Techno", "Detroit Techno"],
        "profile": "Richie Hawtin's second label, founded in 1998. Minus became the home of his Plastikman project and the center of the minimal techno movement. Known for its stark monochrome design aesthetic and uncompromising sound.",
        "notable_artists": ["Richie Hawtin", "Plastikman", "Magda", "Troy Pierce"],
        "notable_releases": [],
        "links": {},
        "image_url": ""
    },
    {
        "label_id": "label_axis",
        "name": "Axis Records",
        "variations": ["Axis"],
        "founded": 1992,
        "founder": ["Jeff Mills"],
        "origin": "Detroit, MI",
        "contact": "",
        "parent_label": "",
        "sublabels": ["Purpose Maker"],
        "distribution": "Submerge",
        "genres": ["Detroit Techno", "Hardcore Techno", "Industrial"],
        "profile": "Founded by Jeff Mills in 1992 following his departure from Underground Resistance. Axis became the vehicle for some of Mills' most uncompromising and visionary work — fast, precise, and demanding. The Purpose Maker sublabel explored more functional dancefloor material.",
        "notable_artists": ["Jeff Mills", "Robert Hood"],
        "notable_releases": [],
        "links": {},
        "image_url": ""
    },
    {
        "label_id": "label_underground_resistance",
        "name": "Underground Resistance",
        "variations": ["UR", "Underground Resistance Records"],
        "founded": 1989,
        "founder": ["Mad Mike Banks", "Jeff Mills"],
        "origin": "Detroit, MI",
        "contact": "",
        "parent_label": "",
        "sublabels": [],
        "distribution": "Submerge (self-distributed)",
        "genres": ["Detroit Techno", "Industrial Techno", "Electro", "Hardcore Techno"],
        "profile": "Founded in 1989 by Mad Mike Banks and Jeff Mills. Underground Resistance is as much a political movement as a record label. Operating under strict anonymity, they built their own independent distribution infrastructure through Submerge and refused all major label involvement. Their releases span brutal industrial techno, Afrofuturist electro, and orchestral space jazz — unified by an uncompromising anti-corporate ethos.",
        "notable_artists": ["Mad Mike Banks", "Jeff Mills", "Robert Hood", "Galaxy 2 Galaxy", "X-101", "X-102"],
        "notable_releases": [],
        "links": {},
        "image_url": ""
    },
    {
        "label_id": "label_m_plant",
        "name": "M-Plant",
        "variations": ["M_Plant"],
        "founded": 1995,
        "founder": ["Robert Hood"],
        "origin": "Detroit, MI",
        "contact": "",
        "parent_label": "",
        "sublabels": [],
        "distribution": "Submerge",
        "genres": ["Minimal Techno", "Detroit Techno"],
        "profile": "Founded by Robert Hood in 1995 after leaving Underground Resistance. M-Plant became the home for Hood's stripped-back, minimal approach to Detroit Techno — long before minimal became a genre label. Every release is characterised by economy: each element serves a purpose, nothing is decorative.",
        "notable_artists": ["Robert Hood", "Floorplan"],
        "notable_releases": [],
        "links": {},
        "image_url": ""
    },
    {
        "label_id": "label_tresor",
        "name": "Tresor Records",
        "variations": ["Tresor", "Tresor Berlin"],
        "founded": 1991,
        "founder": ["Dimitri Hegemann"],
        "origin": "Berlin, Germany",
        "contact": "",
        "parent_label": "",
        "sublabels": [],
        "distribution": "Independent",
        "genres": ["Detroit Techno", "Industrial Techno", "Hard Techno"],
        "profile": "Founded in Berlin in 1991 as the label arm of the legendary Tresor club. While not a Detroit label, Tresor is inseparable from the history of Detroit Techno — it was the primary European home for Detroit artists including Jeff Mills, Robert Hood, Blake Baxter, and Underground Resistance, and it forged the enduring connection between Detroit and Berlin that defines techno's global story.",
        "notable_artists": ["Jeff Mills", "Robert Hood", "Blake Baxter", "Alan Oldham", "Underground Resistance"],
        "notable_releases": [],
        "links": {},
        "image_url": ""
    }
]

# ─── Releases ──────────────────────────────────────────────────

releases_table = dynamodb.Table('detroit-techno-releases')

releases = [
    {
        "release_id": "release_cybotron_alleys_of_your_mind",
        "title": "Alleys of Your Mind",
        "artist": "Cybotron",
        "aliases_used": None,
        "label_id": "label_deep_space",
        "catalog_number": "DS-001",
        "year": 1981,
        "format": "12\"",
        "genres": ["Electro", "Synth-Funk"],
        "tracklist": ["Alleys of Your Mind", "Cosmic Cars"],
        "description": "The debut Cybotron single, produced by Juan Atkins and Rick Davis. Fused Kraftwerk's electronic rigidity with the groove of Parliament-Funkadelic and the futurism of Giorgio Moroder.",
        "historical_significance": "The starting point of the lineage that leads directly to Detroit Techno. One of the earliest records to synthesize European electronic music with African-American funk and soul — the core cultural fusion of the entire genre.",
        "image_url": ""
    },
    {
        "release_id": "release_cybotron_clear",
        "title": "Clear",
        "artist": "Cybotron",
        "aliases_used": None,
        "label_id": "label_fantasy_records",
        "catalog_number": "",
        "year": 1983,
        "format": "12\"",
        "genres": ["Electro", "Proto-Techno"],
        "tracklist": ["Clear", "Cosmic Raindance"],
        "description": "Produced by Juan Atkins and Rick Davis. A harder, more machine-driven follow-up to Alleys of Your Mind that stripped away funk warmth and pushed further into cold, industrial electro territory.",
        "historical_significance": "Widely cited as the first true Detroit Techno record, predating the Metroplex era. Clear established the template Juan Atkins would refine as Model 500 — minimal, mechanical, and deeply futuristic.",
        "image_url": ""
    },
    {
        "release_id": "release_ur_electronic_warfare",
        "title": "Electronic Warfare",
        "artist": "Underground Resistance",
        "aliases_used": "UR",
        "label_id": "label_underground_resistance",
        "catalog_number": "UR-007",
        "year": 1991,
        "format": "12\"",
        "genres": ["Detroit Techno", "Industrial Techno", "Hardcore Techno"],
        "tracklist": ["Electronic Warfare", "Sonic Destroyer", "Elimination"],
        "description": "One of Underground Resistance's most ferocious and uncompromising releases. Brutal, distorted, and unrelenting — designed as a direct assault on the commercialisation of rave culture.",
        "historical_significance": "A defining statement of UR's ideology: techno as resistance. Became a touchstone for the harder, more political strain of Detroit Techno and a direct ancestor of industrial techno.",
        "image_url": ""
    },
    {
        "release_id": "release_plastikman_spastik",
        "title": "Spastik",
        "artist": "Richie Hawtin",
        "aliases_used": "Plastikman",
        "label_id": "label_plus_8",
        "catalog_number": "PLUS 8 LP3",
        "year": 1993,
        "format": "12\"",
        "genres": ["Detroit Techno", "Acid Techno", "Minimal Techno"],
        "tracklist": ["Spastik"],
        "description": "A single looping acid line over a minimal groove — almost nothing else. One of the most radical exercises in reduction in techno history, mutating almost imperceptibly over its runtime.",
        "historical_significance": "A foundational minimal techno record. Spastik demonstrated that maximal impact could be achieved through maximal restraint — a lesson that would shape a decade of minimal techno.",
        "image_url": ""
    },
    {
        "release_id": "release_jeff_mills_the_bells",
        "title": "The Bells",
        "artist": "Jeff Mills",
        "aliases_used": None,
        "label_id": "label_axis",
        "catalog_number": "AX-013",
        "year": 1996,
        "format": "12\"",
        "genres": ["Detroit Techno", "Hardcore Techno"],
        "tracklist": ["The Bells", "Utamara", "Stinger"],
        "description": "Built around a single repeated bell motif over a relentless kick drum. Austere, hypnotic, and emotionally devastating — one of the most played records in Jeff Mills' DJ sets for decades.",
        "historical_significance": "One of the most iconic records in techno history. The Bells demonstrated that pure repetition and reduction could achieve transcendence.",
        "image_url": ""
    },
    {
        "release_id": "release_69_at_les",
        "title": "At Les",
        "artist": "Carl Craig",
        "aliases_used": "69",
        "label_id": "label_planet_e",
        "catalog_number": "",
        "year": 1992,
        "format": "12\"",
        "genres": ["Detroit Techno", "Deep Techno"],
        "tracklist": ["At Les"],
        "description": "A sustained chord progression over a deep, loping groove. Named after a Detroit bar frequented by Craig and his peers. One of the most atmospheric and emotionally rich records in the Detroit canon.",
        "historical_significance": "A defining record of second-generation Detroit Techno and one of the earliest examples of the deep, chord-driven sound that distinguished Carl Craig's work from the first wave.",
        "image_url": ""
    }
]

# ─── Venues ────────────────────────────────────────────────────

venues_table = dynamodb.Table('detroit-techno-venues')

venues = [
    {
        "venue_id": "venue_the_shelter",
        "name": "The Shelter",
        "status": "active",
        "opened": 1990,
        "closed": None,
        "address": "431 E Congress St, Detroit, MI 48226",
        "neighborhood": "Downtown",
        "city": "Detroit, MI",
        "capacity": 400,
        "type": "club",
        "genres": ["Detroit Techno", "House", "Electronic"],
        "historical_significance": "The basement club beneath St. Andrews Hall. One of the most important underground techno and rave spaces in Detroit throughout the 1990s. Hosted landmark nights that kept the scene alive between the closure of The Music Institute and the founding of Movement.",
        "notable_events": [],
        "notable_artists_performed": ["Richie Hawtin", "Carl Craig", "Derrick May"],
        "image_url": ""
    },
    {
        "venue_id": "venue_packard_plant",
        "name": "Packard Automotive Plant",
        "status": "demolished",
        "opened": 1903,
        "closed": 1958,
        "address": "E Grand Blvd & Concord St, Detroit, MI",
        "neighborhood": "East Side",
        "city": "Detroit, MI",
        "capacity": None,
        "type": "industrial / illegal rave",
        "genres": ["Detroit Techno", "Rave"],
        "historical_significance": "The abandoned Packard Plant became a symbol of Detroit's industrial decay and a site of illegal rave parties throughout the 1980s and 1990s. Its vast crumbling interior — once the most advanced auto plant in the world — embodied the Afrofuturist narrative at the heart of Detroit Techno: technology discarded, reclaimed, and repurposed as art. Demolished in 2019.",
        "notable_events": [],
        "notable_artists_performed": [],
        "image_url": ""
    },
    {
        "venue_id": "venue_elektricity",
        "name": "Elektricity",
        "status": "closed",
        "opened": 2005,
        "closed": 2015,
        "address": "45 N Saginaw St, Pontiac, MI 48342",
        "neighborhood": "Downtown Pontiac",
        "city": "Pontiac, MI",
        "capacity": 1200,
        "type": "club",
        "genres": ["Detroit Techno", "House", "Electronic"],
        "historical_significance": "One of the longest-running dedicated electronic music clubs in the Detroit metro area. Located in nearby Pontiac, Elektricity hosted international techno and house acts alongside Detroit's own for a decade, becoming a cornerstone of the regional scene in the 2000s and early 2010s.",
        "notable_events": [],
        "notable_artists_performed": ["Carl Craig", "Richie Hawtin", "Kevin Saunderson", "Stacey Pullen"],
        "image_url": ""
    },
    {
        "venue_id": "venue_submerge",
        "name": "Submerge",
        "status": "active",
        "opened": 1992,
        "closed": None,
        "address": "3000 E Grand Blvd, Detroit, MI 48202",
        "neighborhood": "New Center",
        "city": "Detroit, MI",
        "capacity": None,
        "type": "record store / distribution hub",
        "genres": ["Detroit Techno", "House", "Electronic"],
        "historical_significance": "Founded by Mad Mike Banks, Submerge is simultaneously a record shop, distribution company, and cultural archive. It distributes the majority of Detroit's independent techno labels — Underground Resistance, Axis, Planet E, Transmat, and more — and its physical space serves as the institutional memory of the Detroit Techno movement. Also home to the Museum of Techno.",
        "notable_events": [],
        "notable_artists_performed": [],
        "image_url": ""
    }
]

# ─── Gear ──────────────────────────────────────────────────────

gear_table = dynamodb.Table('detroit-techno-gear')

gear = [
    {
        "gear_id": "gear_korg_ms20",
        "name": "Korg MS-20",
        "manufacturer": "Korg",
        "type": "synthesizer",
        "released_year": 1978,
        "description": "A semi-modular analog synthesizer with a built-in patchbay. Capable of extreme, aggressive sounds through external signal processing and self-patching. Its filter is particularly distinctive — harsh and resonant in a way few other synthesizers replicate.",
        "associated_artists": ["Juan Atkins", "Derrick May"],
        "role_in_detroit_techno": "Used by Juan Atkins on early Metroplex recordings. The MS-20's harsh filter and semi-modular flexibility allowed for unusual and aggressive sounds that contributed to the industrial edge of early Detroit Techno.",
        "image_url": ""
    },
    {
        "gear_id": "gear_roland_sh101",
        "name": "Roland SH-101",
        "manufacturer": "Roland Corporation",
        "type": "synthesizer",
        "released_year": 1982,
        "description": "A monophonic analog synthesizer with a built-in sequencer and arpeggiator. Lightweight, portable, and battery-powered. Capable of thick bass lines and piercing leads.",
        "associated_artists": ["Juan Atkins", "Richie Hawtin"],
        "role_in_detroit_techno": "Used by Juan Atkins on early Model 500 and Metroplex recordings. Its built-in sequencer made it useful for generating bass lines without additional equipment — valuable for producers working with minimal setups.",
        "image_url": ""
    },
    {
        "gear_id": "gear_oberheim_dmx",
        "name": "Oberheim DMX",
        "manufacturer": "Oberheim Electronics",
        "type": "drum machine",
        "released_year": 1981,
        "description": "A digital drum machine with sampled drum sounds and programmable patterns. Its crisp, punchy sounds were distinct from Roland's analog machines — brighter and more aggressive. Widely used in early hip-hop and electro.",
        "associated_artists": ["Juan Atkins", "Derrick May"],
        "role_in_detroit_techno": "Used in early Cybotron and Belleville Three productions before the TR-909 became dominant. The DMX's fingerprints are on some of the earliest proto-Detroit Techno records, bridging the gap between funk and electro.",
        "image_url": ""
    },
    {
        "gear_id": "gear_akai_mpc60",
        "name": "Akai MPC60",
        "manufacturer": "Akai Professional",
        "type": "sampler / sequencer",
        "released_year": 1988,
        "description": "Designed by Roger Linn, the MPC60 combined a 12-bit sampler with a 48-track sequencer and iconic velocity-sensitive pads. Its swing quantisation gave sampled rhythms a distinctly human, loping feel.",
        "associated_artists": ["Carl Craig", "Kevin Saunderson"],
        "role_in_detroit_techno": "Carl Craig used the MPC60 extensively on his Planet E productions, giving second-generation Detroit Techno its more organic, jazz-influenced rhythmic feel. Its swing quantisation introduced a looseness that contrasted with the rigid grid of earlier Roland drum machines.",
        "image_url": ""
    },
    {
        "gear_id": "gear_korg_m1",
        "name": "Korg M1",
        "manufacturer": "Korg",
        "type": "synthesizer / workstation",
        "released_year": 1988,
        "description": "The best-selling synthesizer of all time. A digital workstation with an onboard sequencer and a vast ROM sample library. Its organ, piano, and pad sounds are immediately recognisable — ubiquitous in house, techno, and dance music from 1988 onward.",
        "associated_artists": ["Carl Craig", "Stacey Pullen", "Kevin Saunderson"],
        "role_in_detroit_techno": "The Korg M1's piano and organ patches appear throughout late-1980s and 1990s Detroit Techno and house productions. Carl Craig used it on key Planet E recordings. Its affordability and versatility made it a staple of Detroit producers working on limited budgets.",
        "image_url": ""
    },
    {
        "gear_id": "gear_emu_sp1200",
        "name": "E-mu SP-1200",
        "manufacturer": "E-mu Systems",
        "type": "sampler / drum machine",
        "released_year": 1987,
        "description": "A 12-bit sampler with a built-in sequencer, limited sample time, and a distinctively gritty sound caused by its low bit and sample rate. Its sonic limitations became aesthetic assets — the crunch and warmth of the SP-1200 became a defining texture of late-1980s and early 1990s music.",
        "associated_artists": ["Carl Craig", "Underground Resistance"],
        "role_in_detroit_techno": "Used by Carl Craig and some Underground Resistance producers. The SP-1200's gritty 12-bit texture added an industrial, lo-fi quality to Detroit productions that contrasted with the cleaner Roland machines.",
        "image_url": ""
    },
    {
        "gear_id": "gear_yamaha_dx7",
        "name": "Yamaha DX7",
        "manufacturer": "Yamaha",
        "type": "synthesizer",
        "released_year": 1983,
        "description": "The first commercially successful FM synthesis synthesizer. Its electric piano, marimba, and bass patches are among the most recognised sounds in 1980s music. 16-voice polyphony and MIDI made it the dominant synthesizer of its era.",
        "associated_artists": ["Kevin Saunderson", "Derrick May"],
        "role_in_detroit_techno": "The DX7's FM bass and electric piano sounds appear in early Detroit Techno and house productions. Kevin Saunderson used FM synthesis heavily in his Inner City work. Its digital coldness complemented the analog warmth of the Roland machines.",
        "image_url": ""
    },
    {
        "gear_id": "gear_technics_sl1200",
        "name": "Technics SL-1200",
        "manufacturer": "Technics (Panasonic)",
        "type": "turntable",
        "released_year": 1972,
        "description": "A direct-drive turntable that became the industry standard for DJs worldwide. Its torque, stability, and pitch control made it the definitive tool of DJ culture for over four decades.",
        "associated_artists": ["Jeff Mills", "Derrick May", "Claude Young", "Richie Hawtin"],
        "role_in_detroit_techno": "The SL-1200 is the instrument of Detroit Techno DJs. Jeff Mills' three-turntable technique — operating mixer, drum machine, and multiple decks simultaneously — is inseparable from the 1200's capabilities. The turntable as an instrument, not merely a playback device, is a core part of the Detroit Techno philosophy.",
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