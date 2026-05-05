# Data Model — Detroit Techno Archive API

This document outlines the data model for all entities in the Detroit Techno Archive. Each entity maps to a DynamoDB table. Entities reference each other via ID fields (e.g. `artist_id`, `label_id`, `venue_id`).

---

## Entities Overview

| Entity | Description |
|---|---|
| Artist | Musicians, DJs, and producers in the Detroit Techno/House scene |
| Record Label | Independent labels that released Detroit Techno and House music |
| Release | Albums, EPs, singles, and compilations |
| Venue | Clubs, warehouses, festival grounds, and theaters |
| Event | Festivals, club nights, warehouse parties, and raves |
| Gear | Drum machines, synthesizers, and studio equipment |

---

## Artist

| Field | Type | Description |
|---|---|---|
| `artist_id` | String (PK) | Unique identifier e.g. `artist_kevin_saunderson` |
| `name` | String | Stage/artist name |
| `birth_name` | String | Legal birth name |
| `born` | String | Date of birth |
| `origin` | String | City/region of origin |
| `active_years` | String | e.g. `1982 - present` |
| `genres` | List | e.g. `[Detroit Techno, House]` |
| `aliases` | List | Solo projects under different names |
| `associated_labels` | List | Label IDs or label names |
| `associated_acts` | List | Collaborative projects |
| `biography` | String | Artist biography |
| `notable_tracks` | List | Key tracks |
| `gear` | List | Equipment used |
| `image_url` | String | Profile image |

### Example — Kevin Saunderson
```json
{
  "artist_id": "artist_kevin_saunderson",
  "name": "Kevin Saunderson",
  "birth_name": "Kevin Maurice Saunderson",
  "born": "September 5, 1964",
  "origin": "Brooklyn, NY (raised in Belleville, MI)",
  "active_years": "1984 - present",
  "genres": ["Detroit Techno", "House", "Acid House", "Dance-Pop"],
  "aliases": ["Reese", "Reese Project", "Tronikhouse", "Kreem", "Essaray"],
  "associated_labels": ["KMS Records", "Metroplex", "Incognito Records", "Network Records"],
  "associated_acts": ["Inner City", "E-Dancer", "The Belleville Three"],
  "biography": "One third of the legendary Belleville Three alongside Juan Atkins and Derrick May. Known as The Elevator for bringing Detroit Techno to the mainstream. Founded KMS Records. Inner City with vocalist Paris Grey achieved six million combined sales and nine UK top 40 hits. His Reese Bassline became foundational to jungle and drum and bass. Now performs E-Dancer with son Dantiez Saunderson.",
  "notable_tracks": ["Big Fun", "Good Life", "Just Want Another Chance", "Velocity Funk", "Pump The Move", "Triangle of Love"],
  "gear": ["Roland TR-909", "Roland TR-808", "Roland TR-727", "Yamaha DX100", "Casio CZ-1000", "Fostex 8-Track Recorder"],
  "image_url": ""
}
```

---

## Record Label

| Field | Type | Description |
|---|---|---|
| `label_id` | String (PK) | Unique identifier e.g. `label_kms_records` |
| `name` | String | Label name |
| `variations` | List | Alternative name spellings |
| `founded` | Number | Year founded |
| `founder` | List | Founder name(s) |
| `origin` | String | City/region of origin |
| `contact` | String | Business contact info |
| `parent_label` | String | Parent label if applicable |
| `sublabels` | List | Any sublabels |
| `distribution` | String | Distribution partners |
| `genres` | List | Genres released |
| `profile` | String | Label description |
| `notable_artists` | List | Key artists on the roster |
| `notable_releases` | List | Key releases |
| `links` | Map | Website and social links |
| `image_url` | String | Label logo |

### Example — KMS Records
```json
{
  "label_id": "label_kms_records",
  "name": "KMS Records",
  "variations": ["KMS", "K.M.S. Records"],
  "founded": 1987,
  "founder": ["Kevin Saunderson"],
  "origin": "Ypsilanti, MI (later Detroit, MI)",
  "contact": "KMS Productions LLC, 1249 Washington Blvd, Suite 650, Detroit, Michigan 48226, USA",
  "parent_label": "Armada Music B.V.",
  "sublabels": ["KMS 25th Anniversary Classics", "Spinnin Records"],
  "distribution": "Submerge (original), Above Board Distribution (2012 - present)",
  "genres": ["Detroit Techno", "House", "Deep House"],
  "profile": "Detroit-based techno label founded in 1987 by Kevin Saunderson. KMS stands for Kevin Maurice Saunderson. Relaunched on its 25th anniversary in 2012 with new UK distribution via Above Board Distribution.",
  "notable_artists": ["Kevin Saunderson", "Blake Baxter", "R-Tyme", "MK", "Chez Damier", "Derrick Carter", "Dantiez Saunderson", "Bicep"],
  "notable_releases": [],
  "links": {
    "website": "kmsrecordsus.com",
    "armada": "armadamusic.com",
    "facebook": "facebook.com/kmsrecordsus",
    "soundcloud": "soundcloud.com/kmsrecords",
    "twitter": "x.com/kmsrecordsus",
    "youtube": "youtube.com/kmsrecords"
  },
  "image_url": ""
}
```

---

## Release

| Field | Type | Description |
|---|---|---|
| `release_id` | String (PK) | Unique identifier e.g. `release_inner_city_big_fun` |
| `title` | String | Release title |
| `artist` | String | Artist name |
| `aliases_used` | String | Alias used for this release if applicable |
| `label_id` | String (FK) | Reference to label entity |
| `catalog_number` | String | Label catalog number e.g. `KMS-001` |
| `year` | Number | Year of release |
| `format` | String | `12"`, `EP`, `Album`, `Single`, `Digital`, `Compilation` |
| `genres` | List | Genre tags |
| `tracklist` | List | Track names |
| `description` | String | Release description |
| `historical_significance` | String | Why it matters |
| `image_url` | String | Sleeve/cover artwork |

### Example — Inner City "Big Fun"
```json
{
  "release_id": "release_inner_city_big_fun",
  "title": "Big Fun",
  "artist": "Inner City",
  "aliases_used": null,
  "label_id": "label_kms_records",
  "catalog_number": "",
  "year": 1988,
  "format": "Single",
  "genres": ["Detroit Techno", "House", "Dance-Pop"],
  "tracklist": ["Big Fun", "Big Fun (Instrumental)"],
  "description": "Accidentally created when Kevin Saunderson recorded a backing track and brought in Chicago vocalist Paris Grey. Became a worldwide smash after being included on the Techno - The New Dance Sound of Detroit Virgin Records compilation.",
  "historical_significance": "One of the defining releases that brought Detroit Techno to mainstream global audiences. Nine UK top 40 hits followed for Inner City.",
  "image_url": ""
}
```

---

## Venue

| Field | Type | Description |
|---|---|---|
| `venue_id` | String (PK) | Unique identifier e.g. `venue_music_institute` |
| `name` | String | Venue name |
| `status` | String | `active`, `closed`, `historical` |
| `opened` | Number | Year opened |
| `closed` | Number | Year closed (if applicable) |
| `address` | String | Street address |
| `neighborhood` | String | Neighborhood/area |
| `city` | String | City |
| `capacity` | Number | Approximate capacity |
| `type` | String | `club`, `festival grounds`, `warehouse`, `theater`, `outdoor` |
| `genres` | List | Music genres associated |
| `historical_significance` | String | Why it matters |
| `notable_events` | List | Key events held here |
| `notable_artists_performed` | List | Notable artists who played here |
| `image_url` | String | Venue image |

### Example — The Music Institute
```json
{
  "venue_id": "venue_music_institute",
  "name": "The Music Institute",
  "status": "closed",
  "opened": 1988,
  "closed": 1990,
  "address": "1315 Broadway, Detroit, MI",
  "neighborhood": "Downtown",
  "city": "Detroit, MI",
  "capacity": null,
  "type": "club",
  "genres": ["Detroit Techno", "House", "Acid House"],
  "historical_significance": "Widely considered the first dedicated techno club in Detroit. No alcohol served — purely music focused. Open midnight to 8-9am. United a previously scattered scene into an underground family. Owned by Chez Damier, Alton Miller, and George Baker.",
  "notable_events": [],
  "notable_artists_performed": ["Derrick May", "Juan Atkins", "Kevin Saunderson", "Eddie Fowlkes", "Blake Baxter"],
  "image_url": ""
}
```

---

## Event

| Field | Type | Description |
|---|---|---|
| `event_id` | String (PK) | Unique identifier e.g. `event_movement_2025` |
| `name` | String | Event name |
| `type` | String | `festival`, `club night`, `warehouse party`, `rave`, `concert` |
| `venue_id` | String (FK) | Reference to venue entity |
| `date` | String | Date or date range |
| `year` | Number | Year of event |
| `status` | String | `historical`, `recurring`, `upcoming` |
| `lineup` | List | Artists who performed |
| `description` | String | Event description |
| `historical_significance` | String | Why it matters |
| `image_url` | String | Event flyer or photo |

### Example — Movement 2025
```json
{
  "event_id": "event_movement_2025",
  "name": "Movement Music Festival 2025",
  "type": "festival",
  "venue_id": "venue_hart_plaza",
  "date": "May 24-26, 2025",
  "year": 2025,
  "status": "historical",
  "lineup": [],
  "description": "Annual Detroit Techno and House music festival held at Hart Plaza on the Detroit Riverfront.",
  "historical_significance": "Started in 2000 as the Detroit Electronic Music Festival (DEMF). Free admission in early years. Now draws international crowds from Europe, Japan and beyond. Approaching its 20th anniversary in 2026.",
  "image_url": ""
}
```

---

## Gear

| Field | Type | Description |
|---|---|---|
| `gear_id` | String (PK) | Unique identifier e.g. `gear_roland_tr909` |
| `name` | String | Full product name |
| `manufacturer` | String | Brand/manufacturer |
| `type` | String | `drum machine`, `synthesizer`, `sequencer`, `sampler`, `mixer`, `recorder` |
| `released_year` | Number | Year of manufacture/release |
| `description` | String | Technical description |
| `associated_artists` | List | Artists known to use this gear |
| `role_in_detroit_techno` | String | Significance to the genre |
| `image_url` | String | Product image |

### Example — Roland TR-909
```json
{
  "gear_id": "gear_roland_tr909",
  "name": "Roland TR-909 Rhythm Composer",
  "manufacturer": "Roland Corporation",
  "type": "drum machine",
  "released_year": 1983,
  "description": "Analog/digital hybrid drum machine with programmable patterns. Distinctive hi-hats, kicks and snares that became the sonic foundation of Techno and House music worldwide.",
  "associated_artists": ["Kevin Saunderson", "Juan Atkins", "Derrick May", "Richie Hawtin"],
  "role_in_detroit_techno": "The defining drum machine of Detroit Techno. Its punchy kick drum and crisp hi-hats are instantly recognizable in virtually every classic Detroit Techno record.",
  "image_url": ""
}
```

---

## Entity Relationships

```
Artist ──────────> Record Label (via associated_labels)
Release ─────────> Artist (via artist field)
Release ─────────> Record Label (via label_id)
Event ───────────> Venue (via venue_id)
Artist ──────────> Gear (via gear field)
```

> Note: DynamoDB is non-relational. These are soft references by ID, not enforced foreign keys like in SQL. Query patterns need to be designed around access patterns, not relationships.

---

## Notes
- All IDs follow the pattern: `entity_type_name` e.g. `artist_kevin_saunderson`
- `image_url` fields are populated from S3 bucket paths
- `historical_significance` fields are what make this archive valuable — prioritize quality descriptions
