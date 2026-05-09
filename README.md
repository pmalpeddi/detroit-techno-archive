# detroit-techno-archive
A public REST API and web interface archiving the history of Detroit Techno and House music. Covers artists, record labels, venues, releases, events, and gear. Built on AWS serverless architecture 

## Tech Stack
| Service | Purpose |
|---|---|
| AWS Lambda | Serverless functions handling API logic |
| AWS API Gateway | Exposes public REST API endpoints |
| AWS DynamoDB | Primary database for all entities |
| AWS S3 | Stores artist images and album artwork |
| AWS CloudFront | CDN layer for performance |
| AWS Cognito | Admin authentication |
| AWS CodePipeline | CI/CD pipeline |
| AWS SAM | Local development and deployment |

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

## Project Structure
functions/ #Lambda handlers (one per endpoint)
frontend/ # React web interface
scripts/ # Data seeding scripts
docs/ # Architecture diagrams and data model

## Documentation
- [Data Model](docs/data-model.md)
- [Architecture Diagram](docs/architecture.drawio.png)
- [Dev log](docs/DEVLOG.md)

## Local Development

### Prerequisites
- AWS CLI configured
- SAM CLI installed
- Docker running
- Node.js installed

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