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

## Documentation
- [Data Model](docs/data-model.md)

## Local Development

### Prerequisites
- AWS CLI configured
- SAM CLI installed
- Docker running

### Run locally
```bash
sam build --use-container
sam local start-api
```

### Deploy to AWS
```bash
sam deploy --guided
```