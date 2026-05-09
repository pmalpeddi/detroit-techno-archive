# Dev Log

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

