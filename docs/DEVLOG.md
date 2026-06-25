# Dev Log

## 06/24/2026

### Phase 6 — CI/CD Setup (CodeBuild + CodePipeline)

#### CodeBuild
- Created `buildspec.yml` at project root defining install, build, and post_build phases
  - Install: aws-sam-cli (pip), npm dependencies
  - Build: `sam build` + `sam deploy`, `npm run build`
  - Post-build: `aws s3 sync` to frontend bucket, CloudFront invalidation
- Created CodeBuild project `detroit-techno-archive` via AWS console
  - Source: GitHub via GitHub App connection
  - Environment: Amazon Linux, standard runtime, 2 vCPUs / 4 GiB
  - Service role: `codebuild-detroit-techno-archive-service-role` (auto-generated + custom inline policy)
  - Buildspec: uses `buildspec.yml` from repo root
  - CloudWatch logs enabled at `/aws/codebuild/detroit-techno-archive`
  - Environment variable: `CLOUDFRONT_DISTRIBUTION_ID` (plaintext)
- Resolved several build failures iteratively:
  - Removed `profile = "techno-archive-dev"` from `samconfig.toml` — CodeBuild uses IAM role, not named profiles
  - Added explicit flags to `sam deploy` command (`--stack-name`, `--region`, `--capabilities`, `--resolve-s3`, `--s3-prefix`)
  - Expanded CodeBuild IAM role to include `aws-sam-cli-managed-default` CloudFormation stack
- **First successful build confirmed**

#### IAM Refactor
- Replaced 10 attached managed policies on `techno-archive-dev` with a single customer managed policy `techno-archive-dev-policy` — scoped to project resources following least privilege principle
- Added CodeBuild execution inline policy to `codebuild-detroit-techno-archive-service-role`

#### GPG Commit Signing
- Generated GPG key (RSA 4096) in WSL
- Added public key to GitHub — verified commits now enabled
- Configured git globally: `user.signingkey`, `commit.gpgsign`, `GPG_TTY`
- Added `export GPG_TTY=$(tty)` to `~/.bashrc` for persistent passphrase prompting

#### Next Steps
- Complete CodePipeline setup (stopped mid-creation — needs `ec2:DescribeVpcs` permission added to `techno-archive-dev-policy`)
- Add EC2 read-only statement to managed policy, resume pipeline creation
- Test end-to-end: push to `main` → pipeline triggers → CodeBuild runs → deploy succeeds
- Write DEVLOG entry for completed pipeline once live
- Lock down `iam:*` in `techno-archive-dev-policy` back to specific actions once setup is complete

## 06/18/2026

### Data — Wave 5 Seed (Venues)
- Added `scripts/seed_data_5.py` — 2 venues
- Used Claude Code to scan the venues table before writing — confirmed neither entry existed yet
- Uploaded images directly to S3 via AWS CLI (`aws s3 cp`) instead of the console — faster, scriptable, and consistent with the rest of the seeding workflow
- Added `scripts/update_image_urls_5.py` — image URLs for both new venues
- Source: [Spot Lite and UFO Bar to close in Detroit as owners move away from nightlife](https://www.metrotimes.com/food-drink/spot-lite-and-ufo-bar-to-close-in-detroit-as-owners-move-away-from-nightlife/) — Detroit Metro Times, June 2026
- Archive now has 11 venues

### New Venues
- Spot Lite — Islandview hybrid space (bar, gallery, record store, coworking, dance floor) opened 2021 by Roula David and Jesse Cory; closing June 28, 2026 after a 5-year run
- UFO Bar — Corktown venue, formerly UFO Factory, reopened under Roula David in 2024; closing June 30, 2026, to reopen under new ownership as Detroit Vinyl Bar

### Next Steps
- Add POST/PUT admin endpoints protected by Cognito authorizer
- Set up CI/CD pipeline via CodePipeline and CodeBuild
- CloudWatch monitoring and alarms
- Continue seeding data — more artists, releases, venues

## 06/13/2026

### Bug Fix — Labels Page
- Fixed blank screen crash on Labels page — `founder` field stored as string in DynamoDB but component was calling `.join()` on it expecting an array
- Fixed incorrect field reference: `label.profile` → `label.description`
- Added `.catch()` error handling to the labels fetch so network failures surface as a message instead of a silent hang
- Rebuilt and redeployed to S3 + CloudFront manually

### Tooling — Claude Code Integration
- Installed Claude Code CLI in WSL (`npm install -g @anthropic-ai/claude-code`)
- Added `CLAUDE.md` to project root — gives Claude Code persistent context on stack, AWS profile, table names, API URL, and seeding conventions
- Added `.claudeignore` to exclude `.env`, credentials, and build artifacts from Claude Code's file access
- Added Claude Code to README tech stack — agentic CLI used to streamline data seeding, scans live DynamoDB tables before each wave to prevent duplicate entries and generate historically accurate seed scripts

### Data — Wave 4 Seed
- Used Claude Code to scan all 6 DynamoDB tables before writing any scripts — prevented duplicate entries automatically
- Added `scripts/seed_data_4.py` — 5 artists, 3 labels, 5 releases, 1 event, 3 venues, 4 gear items
- Added `scripts/update_image_urls_4.py` — image URLs for all wave 4 entries
- Uploaded images to S3 across artists/, labels/, releases/, venues/, events/, gear/ folders
- Fixed `venue_elektricity` — corrected opened year to 2011, status to active, updated description
- Archive now has 27 artists, 16 labels, 24 releases, 9 venues, 20 gear items, 2 events

### New Artists
- Kenny Larkin — second-wave Detroit producer, Azimuth (1994, Warp Records)
- DJ Minx (Jennifer Witcher) — Detroit underground DJ, founder of Women on Wax Recordings
- Omar S (Alex Omar Smith) — FXHE Records founder, raw Detroit house and techno
- Dopplereffekt (Gerald Donald) — EBM-influenced project, Gerald Donald's post-Drexciya work
- Terrence Dixon — minimal Detroit Techno, Population One imprint

### New Labels
- FXHE Records — Omar S's artist-owned Detroit imprint
- Women on Wax — DJ Minx's label, dedicated to female and femme-identifying producers
- Population One — Terrence Dixon's minimal techno imprint

### New Releases
- Carl Craig: Landcruising (1995, Planet E)
- Model 500: Night Drive (Thru-Babylon) (1985, Metroplex)
- Underground Resistance: Interstellar Fugitives (1998, UR)
- Eddie Fowlkes: Goodbye Kiss (1986, Metroplex)
- Omar S: Thank U 4 Letting Me Be Myself (2007, FXHE)

### New Events
- Detroit Electronic Music Festival 2000 — inaugural DEMF at Hart Plaza, ~1 million attendees, first public recognition of Detroit Techno's cultural significance at scale

### New Venues
- St. Andrews Hall — historic downtown Detroit concert hall and home of The Shelter
- Bookies Club 870 — late 1970s punk/new wave club, cultural pre-history of Detroit Techno
- Marble Bar — early 1980s alternative underground venue, formative for the generation that created Detroit Techno

### New Gear
- Roland Jupiter-8, Akai S950, Sequential Circuits Six-Trak, Roland MC-202 MicroComposer

### Next Steps
- Add POST/PUT admin endpoints protected by Cognito authorizer
- Set up CI/CD pipeline via CodePipeline and CodeBuild
- CloudWatch monitoring and alarms
- Continue seeding data — more releases, more venues

## 06/08/2026

### Docs — Architecture Diagram Redraw
- Redrawn architecture diagram as SVG replacing original `architecture.drawio.png`
- Corrected several inaccuracies from the original:
  - Split CloudFront role — now correctly shown as frontend CDN (not in front of API Gateway)
  - Added `detroit-techno-archive-frontend` S3 bucket as a distinct node from the media/images bucket
  - Added X-Ray for distributed tracing alongside CloudWatch
  - Added frontend CI/CD deploy path — CodeBuild → S3 sync + CloudFront cache invalidation
  - Split CodeBuild out as its own explicit node (was folded into CodePipeline)
  - Fixed CodePipeline → SAM/CloudFormation → Lambda deploy chain (was an incorrect dotted line directly to Lambda)
- Exported PNG from SVG for GitHub README rendering
- Updated README to embed PNG with link to SVG source: `[![Architecture Diagram](docs/architecture.png)](docs/architecture.svg)`

## 06/01/2026

### Data — Wave 3 Seed
- Added `scripts/seed_data_3.py` — 6 artists, 2 labels, 10 releases, 1 event, 4 gear items
- Added `scripts/update_image_urls_3.py` — image URLs for all wave 3 entries
- Added `scripts/fix_label_founders.py` — hotfix correcting founder field type mismatch on wave 3 labels
- Uploaded images to S3 across artists/, labels/, releases/, gear/, events/ folders
- Created events/ folder in S3 media bucket for the first time
- Archive now has 22 artists, 13 labels, 19 releases, 6 venues, 16 gear items, 1 event
### New Artists
- Drexciya — Gerald Donald & James Stinson, foundational Detroit Electro act
- DJ Rolando — Underground Resistance member, known for Jaguar (1999)
- Suburban Knight (James Pennington) — Transmat artist, dark techno pioneer
- Octave One (Lenny & Lawrence Burden) — Detroit Techno duo, founders of 430 West
- Anthony "Shake" Shakir — longtime Detroit producer, Metroplex circle
- Aux 88 (Tommy Hamilton & Keith Tucker) — definitive Detroit Electro duo
### New Labels
- 430 West Records — Octave One's artist-owned imprint
- Direct Beat — Detroit Electro label co-founded by Aux 88 and DJ Stingray
### New Releases
- Robert Hood: Minimal Nation (1994)
- Jeff Mills: Waveform Transmission Vol. 1 (1992)
- Underground Resistance: Galaxy 2 Galaxy (1993)
- Drexciya: The Unknown Aquatic Habitat (1994)
- Aztec Mystic (DJ Rolando): Jaguar (1999)
- Reese (Kevin Saunderson): Just Want Another Chance (1988) — origin of the Reese Bassline
- Model 500: Interference (1990)
- Paperclip People (Carl Craig): The Climax (1994)
- Suburban Knight: The Art of Stalking (1990)
- Aux 88: Is It Man or Machine? (1995)
### New Events
- Movement Music Festival 2026 — 20th anniversary edition, Hart Plaza, May 23–25 2026
- Headlined by Carl Cox, Sara Landry, Dom Dolla
- 115+ artists across 6 stages including Juan Atkins, Richie Hawtin, Carl Craig, Kevin Saunderson
### New Gear
- Sequential Circuits Prophet-5, Moog Source, Ensoniq ESQ-1, Oberheim Matrix-1000
### Frontend — Events Page
- Built `Events.js` and `Events.css` — full Events page matching existing design system
- Events display with image, status badge, date, type, description, historical significance, and lineup tags
- Added Events route to `App.js` and Events link to `Navbar.js`
### Frontend — S3 + CloudFront Deployment
- Built React app via `npm run build`
- Created S3 bucket `detroit-techno-archive-frontend` in us-east-1
- Synced build/ folder to S3 via `aws s3 sync`
- Disabled Block Public Access and attached public read bucket policy
- Attached CloudFrontFullAccess policy to `techno-archive-dev` IAM user via root account
- Created CloudFront distribution (ID: EMP03ACQED95W) pointing at frontend S3 bucket
- Configured 403 → index.html custom error response for React Router client-side routing
- Frontend is live at https://d24pywqdzwrvb1.cloudfront.net
### Decisions Made
- Dropped GitLab mirror plan — GitHub + AWS CodePipeline covers CI/CD needs without added friction
- Events page built now that real data exists (Movement 2026) rather than leaving it as coming soon
- Reese Bassline origin record (Just Want Another Chance) prioritized as a release entry — culturally significant beyond Detroit Techno into jungle and drum and bass
### Next Steps
- Add POST/PUT admin endpoints protected by Cognito authorizer
- Set up CI/CD pipeline via CodePipeline and CodeBuild
- Seed more data — Kenny Larkin, more releases, more venues
- CloudWatch monitoring and alarms

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

