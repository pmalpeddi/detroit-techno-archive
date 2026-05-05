# Dev Log

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