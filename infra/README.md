# Infrastructure

Terraform configurations and Dockerfiles for deploying services and supporting infrastructure.

Available modules:

- `modules/bedrock` – AWS Bedrock agent setup
- `modules/s3` – S3 bucket provisioning
- `modules/glue` – Glue catalog database
- `modules/athena` – Athena workgroup
- `modules/redis` – Elasticache Redis cluster
- `modules/mongodb-atlas` – MongoDB Atlas cluster via provider
- `modules/sap-btp` – SAP BTP Connector instance

The legacy `redis.tf` file provisions a simple Elasticache cluster used for real-time coordination and pub/sub.
