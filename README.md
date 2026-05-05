# detroit-techno-archive
A public REST API and discovery platform archiving the history of Detroit Techno and House music. Built on AWS serverless architecture.

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