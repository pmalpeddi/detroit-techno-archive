# Dev Log

## 05/20/2026
05/20/2026
Architecture & Roadmap Revision
Revisited project architecture and roadmap — making several additions to better reflect real world cloud engineering practices and expand the project's value as a portfolio piece
Infrastructure as Code

Adding Terraform alongside SAM CLI for infrastructure provisioning
Terraform will own VPC, S3, CloudFront, Cognito, and DynamoDB resources
SAM will remain responsible for Lambda functions and API Gateway
Separating infra concerns from application concerns — standard practice in production environments

CI/CD Pipeline Expansion

Original plan was CodePipeline + CodeBuild — keeping both but fleshing out the full pipeline
Full pipeline flow:

GitHub push triggers CodePipeline
CodeBuild runs tests and builds React frontend
SAM deploys updated Lambda functions
S3 sync deploys frontend build
CloudFront cache invalidation runs automatically post-deploy


Adding GitLab as a mirrored repository to get hands on experience with GitLab CI/CD pipelines
GitLab is widely used in enterprise DevOps environments — worth knowing

Observability

Adding Phase 7 to the roadmap focused entirely on observability
CloudWatch Dashboards for API metrics and Lambda performance
CloudWatch Alarms for error rate thresholds
AWS X-Ray for distributed tracing across Lambda functions and API Gateway
None of this was in the original plan — adding it because monitoring is a non-negotiable in real production systems

Decisions Made

Terraform added not to replace SAM but to complement it — SAM handles serverless, Terraform handles everything else, this is a realistic split used in real engineering teams
GitLab added as a mirror rather than a full migration — GitHub stays primary, GitLab gives CI/CD pipeline experience without disrupting existing workflow
Observability added as its own phase rather than tacked onto Phase 6 — it deserves dedicated attention and is a major resume differentiator
All of these additions are intentional for portfolio purposes — the goal is to build something that reflects what cloud engineers actually work with day to day

Next Steps

Finish POST/PUT endpoints for admin data entry protected by Cognito
Deploy frontend to S3 + CloudFront
Add Events page and seed Events data
Continue seeding artist, label, release, venue, and gear data
Begin Phase 6 CI/CD pipeline setup once frontend is live

## 05/18/2026

### Data — Wave 2 Seed
- Added `scripts/seed_data_2.py` — 6 artists, 8 labels, 6 releases, 4 venues, 8 gear items
- Added `scripts/update_image_urls_2.py` — image URLs for all 34 new entries
- Uploaded 34 images to S3 across artists/, gear/, labels/, releases/, venues/ folders
- Ran both scripts via WSL — all records seeded and image URLs updated clean
- Archive now has 16 artists, 11 labels, 9 releases, 6 venues, 12 gear items

### New Artists
- Stacey Pullen, Chez Damier, Alan Oldham (DJ T-1000), Claude Young
- Cybotron (Juan Atkins + Rick Davis) — added as standalone act, direct precursor to Detroit Techno
- Underground Resistance — added as collective entry separate from Mad Mike Banks individual entry

### New Labels
- Planet E, Plus 8, Minus, Axis, Underground Resistance, M-Plant, Tresor, Network Records
- Closes all dangling label_id references from seed_artists.py

### New Releases
- Cybotron: Alleys of Your Mind (1981), Clear (1983)
- Underground Resistance: Electronic Warfare (1991)
- Plastikman: Spastik (1993)
- Jeff Mills: The Bells (1996)
- 69 (Carl Craig): At Les (1992)

### New Venues
- The Shelter, Packard Automotive Plant, Elektricity, Submerge

### New Gear
- Korg MS-20, Roland SH-101, Oberheim DMX, Akai MPC60, Korg M1, E-mu SP-1200, Yamaha DX7, Technics SL-1200

### Decisions Made
- Underground Resistance exists as both an artist entry and a label entry — intentional, reflects reality
- Submerge added as a venue entry — primarily a distribution hub and record store, Museum of Techno housed inside
- Cybotron seeded as its own artist entry rather than just referenced in Juan Atkins' biography

### Next Steps
- Deploy frontend to S3 + CloudFront to get the site live
- Add POST/PUT endpoints for admin data entry protected by Cognito
- Add Events page
- Add Events entity and seed data

## 05/12/2026

### Data & Artists
- Seeded 5 new artists: Carl Craig, Richie Hawtin, Jeff Mills, Robert Hood, Mad Mike Banks
- Uploaded press photos for all 5 new artists to S3 artists/ folder
- Uploaded Belleville Three group photo to S3 for hero section
- Wrote `scripts/seed_artists_2.py` and `scripts/update_artist_images_2.py`
- Archive now has 10 artists total

### Frontend — Hero Section
- Added Belleville Three photo to hero section — two column layout, text left, image right
- Added founders tagline beneath the image: "Juan Atkins, Derrick May, and Kevin Saunderson. Three kids from Belleville, Michigan who changed music forever. The founders of Detroit Techno."
- Removed samconfig.toml from Git tracking via git rm --cached

### Decisions Made
- Belleville Three treated as a historical reference in the hero section rather than a standalone artist entry — the three are already individually archived
- Richie Hawtin included despite being from Windsor, Ontario — directly across the Detroit River, deeply embedded in the Detroit scene

### Next Steps
- Continue tweaking frontend design — still in progress, layout and visual details being refined
- Deploy frontend to S3 + CloudFront to get the site live on the internet
- Add POST/PUT endpoints for admin data entry protected by Cognito
- Seed more data — more labels, releases, venues, events
- Add Events page
- Add Underground Resistance as a label entry

## 05/11/2026

### Demo (5/11/2026)

https://github.com/user-attachments/assets/d5fb2579-3827-455b-9244-1ad0d06d2c0a

### S3 Media Bucket
- Created S3 bucket `detroit-techno-archive-media` in us-east-1
- Disabled public access block and attached bucket policy for public read
- Created folder structure: artists/, gear/, labels/, releases/, venues/
- Uploaded JPEG images for all 5 artists, 4 gear items, 3 labels, 3 releases, 2 venues
- Wrote `scripts/update_image_urls.py` to update image_url fields in DynamoDB via boto3
- All 17 image_url fields updated across 5 DynamoDB tables

### Frontend — Pages & Images
- Built Artist detail page with full profile, biography, aliases, gear sidebar
- Added release cross-referencing on artist detail page — fetches releases table and matches by artist name, alias, and associated acts
- Release artwork now shows inline next to notable tracks
- Added image rendering across all pages — artist grid, gear grid, labels list, venues list
- Built Venues page with full-width image, status badge, historical significance
- Added Releases section to artist detail page showing matched release artwork
- Skipped standalone Releases page — releases live in artist context instead

### Decisions Made
- Cross-referenced releases to artists via three match conditions: artist name, aliases_used, and associated_acts — catches Inner City releases on Kevin Saunderson's page
- Venues page uses horizontal layout with large image left, info right — matches the editorial feel of the Labels page
- No standalone Releases page for now — too few entries to justify, better in artist context

### Next Steps
- Deploy frontend to S3 + CloudFront
- Add POST/PUT endpoints for admin data entry protected by Cognito
- Seed more data — more artists, labels, releases
- Add Events page

## 05/09/2026
### Data & Auth
- Wrote unified seed script covering all 6 entities — 5 artists, 3 labels, 3 releases, 2 venues, 4 gear items
- Fixed Decimal serialization bug across all Lambda list endpoints — DynamoDB returns numbers as Decimal type which json.dumps can't handle by default, added custom DecimalEncoder
- Added Cognito User Pool and User Pool Client to template.yaml
- Attached AmazonCognitoPowerUser policy to techno-archive-dev IAM user
- Deployed Cognito stack via SAM — User Pool ID: us-east-1_YE3s2IwJd
- Created admin user in Cognito with permanent password
- Added samconfig.toml to .gitignore to avoid leaking AWS account details

### Frontend Init
- Initialized React app in frontend/ using create-react-app
- Installed react-router-dom and axios
- Resolved WSL/Windows filesystem permission issues by building in Linux fs then moving to Windows fs

### Decisions Made
- AllowAdminCreateUserOnly set to true on Cognito pool — no public signups, admin-only access
- Access tokens set to 24hr validity, refresh tokens to 30 days
- Frontend lives inside the same repo under frontend/ for simplicity

### Next Steps
- Build React frontend — artists, labels, gear pages
- Dark minimal UI aesthetic
- Connect frontend to live API endpoints
- Host on S3 + CloudFront

## 05/07/2026
### Backend Foundation
- Rewrote template.yaml replacing SAM boilerplate with full 
  Detroit Techno Archive infrastructure
- Deployed all 6 DynamoDB tables to AWS via SAM CLI
- Wrote and deployed GET endpoints for all 6 entities (12 endpoints total)
- Seeded Belleville Three artist data (Juan Atkins, Derrick May, 
  Kevin Saunderson)
- Tested live API endpoints via curl and browser
- Added .aws-sam to .gitignore to prevent local paths leaking to GitHub

### Decisions Made
- Used PAY_PER_REQUEST billing on all DynamoDB tables — no capacity 
  planning needed at this stage
- Kept Lambda functions simple and single responsibility — one handler 
  per endpoint
- Skipped Postman testing for now — will revisit when POST/PUT/DELETE 
  endpoints are added

### Next Steps
- Seed data for remaining 5 entities (labels, releases, venues, events, gear)
- Write POST endpoints for admin data entry
- Set up Cognito authentication for write endpoints
- Set up S3 bucket for artist images

## 05/06/2026
### AWS Environment Setup
- Created IAM user `techno-archive-dev` with least privilege permissions
- Attached policies: Lambda, DynamoDB, S3, API Gateway, CloudFormation, 
  IAM, CloudWatch
- Generated access keys and configured named AWS CLI profile
- Updated samconfig.toml with profile and region (us-east-1)
- Drew initial architecture diagram and committed to docs/

### Decisions Made
- Chose separate IAM user over separate AWS account to preserve 
  existing learning environment
- Chose us-east-1 as deployment region

## 05/05/2026
### Planning & Setup
- Defined complete data model for all 6 entities: Artist, Record Label, 
  Release, Venue, Event, Gear
- Populated real example entries for each entity using Kevin Saunderson, 
  KMS Records, Inner City, The Music Institute etc.
- Initialized GitHub repository with README and tech stack documentation
- Set up SAM CLI project with Python 3.14 runtime
- Configured local development environment (AWS CLI, SAM CLI, Docker)

### Decisions Made
- Chose DynamoDB over RDS — flexible schema, serverless scaling, 
  no server management
- Chose Python 3.14 as Lambda runtime
- Chose Serverless API as project architecture
- Added aliases field to Artist entity to separate solo pseudonyms 
  from collaborative acts

### Next Steps
- Design DynamoDB access patterns
- Modify template.yaml for Detroit Techno Archive resources
- Write first Lambda function for Artist entity (GET /artists)
- Seed initial data

