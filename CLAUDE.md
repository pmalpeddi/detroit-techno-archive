## Data Seeding Guidelines

When helping seed data, only add artists, labels, releases, venues, or gear
that are not already in the archive. Before writing any seed script, query
the relevant DynamoDB table first to check what exists.

### Check existing data before seeding:
```bash
aws dynamodb scan --table-name detroit-techno-artists \
  --profile techno-archive-dev \
  --query "Items[*].artist_id.S" --output table

aws dynamodb scan --table-name detroit-techno-labels \
  --profile techno-archive-dev \
  --query "Items[*].label_id.S" --output table

aws dynamodb scan --table-name detroit-techno-releases \
  --profile techno-archive-dev \
  --query "Items[*].release_id.S" --output table

aws dynamodb scan --table-name detroit-techno-venues \
  --profile techno-archive-dev \
  --query "Items[*].venue_id.S" --output table

aws dynamodb scan --table-name detroit-techno-gear \
  --profile techno-archive-dev \
  --query "Items[*].gear_id.S" --output table
```

### Seeding rules:
- Focus on Detroit Techno and House music history — artists, labels, releases, venues, and gear directly connected to the Detroit scene
- Follow the wave pattern: next script is `seed_data_5.py`, `update_image_urls_5.py`
- Image filenames: lowercase underscore (`kenny_larkin.jpg`)
- IDs: lowercase underscore (`artist_kenny_larkin`)
- Always verify historical accuracy before adding an entry