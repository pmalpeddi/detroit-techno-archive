# detroit-techno-archive
A public REST API and web interface archiving the history of Detroit Techno and House music. Covers artists, record labels, venues, releases, events, and gear. Built on AWS serverless architecture.

**Live:** https://d24pywqdzwrvb1.cloudfront.net

---

## Tech Stack
| Service | Purpose |
|---|---|
| AWS Lambda | Serverless functions handling API logic |
| AWS API Gateway | Exposes public REST API endpoints |
| AWS DynamoDB | Primary database for all entities |
| AWS S3 | Stores artist images, album artwork, and frontend build |
| AWS CloudFront | CDN layer for frontend delivery and performance |
| AWS Cognito | Admin authentication for protected endpoints |
| AWS CodePipeline | CI/CD pipeline orchestration |
| AWS CodeBuild | Builds and tests application code |
| AWS CloudWatch | Monitoring, dashboards, and alerting |
| AWS X-Ray | Distributed tracing across Lambda and API Gateway |
| AWS SAM | Serverless application framework for Lambda and API Gateway |
| Terraform | Infrastructure as Code for all non-serverless AWS resources |
| React | Frontend web interface |
| React Router | Client-side routing |

---

## API Endpoints

Base URL: `https://cvlthm6c36.execute-api.us-east-1.amazonaws.com/Prod`

| Method | Endpoint | Description |
|---|---|---|
| GET | /artists | List all artists |
| GET | /artists/{artist_id} | Get artist by ID |
| GET | /labels | List all labels |
| GET | /labels/{label_id} | Get label by ID |
| GET | /releases | List all releases |
| GET | /releases/{release_id} | Get release by ID |
| GET | /venues | List all venues |
| GET | /venues/{venue_id} | Get venue by ID |
| GET | /events | List all events |
| GET | /events/{event_id} | Get event by ID |
| GET | /gear | List all gear |
| GET | /gear/{gear_id} | Get gear by ID |

---

## Project Structure
```
functions/    # Lambda handlers
frontend/     # React web interface
scripts/      # Data seeding scripts
infra/        # Terraform definitions
docs/         # Architecture diagrams
```

## Pages
| Page | Route | Description |
|---|---|---|
| Home | / | Hero, stats, featured artists |
| Artists | /artists | All artists grid |
| Artist Detail | /artists/:id | Full artist profile with releases |
| Labels | /labels | Record labels chronological list |
| Venues | /venues | Venues with images and history |
| Gear | /gear | Machines with filter by type |
| Events | /events | Festivals, club nights, and events |

---

## Roadmap

### Phase 1 — Planning ✅
- Defined data model for all entities
- Created GitHub repo
- Set up AWS environment with IAM roles
- Installed and configured SAM CLI
- Drew architecture diagram

### Phase 2 — Backend Foundation ✅
- Created all DynamoDB tables via SAM
- Wrote Lambda functions for GET endpoints across all 6 entities
- Exposed 12 endpoints through API Gateway
- Deployed via SAM CLI

### Phase 3 — Data Population ✅ (Ongoing)
- Seeded 22 artists, 13 labels, 19 releases, 6 venues, 16 gear items, 1 event
- Uploaded images to S3 across all entity folders
- Validated data structure and API responses

### Phase 4 — Auth & Admin (In Progress)
- Cognito User Pool deployed via SAM
- Admin-only user pool — no public signups
- POST/PUT endpoints for admin data entry — in progress

### Phase 5 — Frontend (In Progress)
- React app with React Router
- Artists, Labels, Gear, Venues, Events pages
- Artist detail pages with release cross-referencing
- Hero section with Belleville Three
- Deployed to S3 + CloudFront — https://d24pywqdzwrvb1.cloudfront.net
- UI polish and refinement ongoing

### Phase 6 — CI/CD Pipeline
- CodePipeline triggered by GitHub push
- CodeBuild runs tests and builds React frontend
- SAM deploys updated Lambda functions
- S3 sync deploys frontend build
- CloudFront cache invalidation post-deploy

### Phase 7 — Observability
- CloudWatch Dashboards for API and Lambda metrics
- CloudWatch Alarms for error rate thresholds
- AWS X-Ray distributed tracing across Lambda and API Gateway

### Phase 8 — Production Quality
- Terraform for all infrastructure provisioning
- Full README with architecture diagram
- Blog post / LinkedIn article about the build
- Submit to Detroit Techno community groups

---

## Documentation
- [Data Model](docs/data-model.md)
  [![Architecture Diagram](docs/architecture.png)](docs/architecture.svg)
- [Dev Log](docs/DEVLOG.md)

---

## Local Development

### Prerequisites
- AWS CLI configured
- SAM CLI installed
- Docker running
- Node.js installed
- Terraform installed

### Run API locally
```bash
sam build --use-container
sam local start-api
```

### Run frontend locally
```bash
cd frontend
npm install
npm start
```

### Deploy to AWS
```bash
sam deploy --guided
```