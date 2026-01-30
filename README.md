# Log-service
Implement a simple log service that stores and retrieves log entries using an AWS database and two AWS Lambda functions.

This repository contains a **fully Infrastructure-as-Code (IaC)** implementation of a simple log service using **AWS Lambda**, **DynamoDB**, and **Terraform**.  

It provides:

- **Ingest Lambda**: Accepts log entries and stores them in DynamoDB.
- **ReadRecent Lambda**: Retrieves the 100 most recent log entries.
- **DynamoDB**: Stores log entries efficiently.
- **Terraform**: Automates deployment of all resources.

---

## Architecture

Client
|
| HTTP (Lambda Function URL)
v
Ingest Lambda ───▶ DynamoDB (log_entries)
▲
|
ReadRecent Lambda



- **Ingest Lambda**: Adds logs to the database via HTTP POST.
- **ReadRecent Lambda**: Returns up to 100 most recent logs via 
HTTP GET.

- **DynamoDB Table**: Optimized for fast retrieval of newest logs with single digit millisecond latency, serverless,easy to set up with lambda and IAM, secure even during availability zones failures.
- **Terraform**: Creates Lambda functions, DynamoDB table, IAM roles, and Lambda Function URLs.

---

## Database Design

### DynamoDB Table: `log_entries`

| Attribute | Type   | Purpose                                  |
|-----------|--------|------------------------------------------|
| pk        | String | Partition key (`LOG`)                    |
| sk        | String | Sort key (`<ISO8601>#<UUID>`)            |
| id        | String | Unique log ID                            |
| datetime  | String | Timestamp of log entry                   |
| severity  | String | `info`, `warning`, or `error`            |
| message   | String | Log message text                         |

- **Partition Key (`pk`)**: constant value `LOG` to group all logs
- **Sort Key (`sk`)**: timestamp + UUID ensures uniqueness and auto-sorting
- **Query**: `ScanIndexForward=false` + `Limit=100` → retrieves newest logs efficiently

## Repository Structure

log-service/
├── terraform/
├── lambdas/
│ ├── ingest/
│ └── read_recent/
├── tests/
└── README.md

## Prerequisites

- AWS account with an IAM user with permissions for DynamoDB, Lambda, and IAM
- AWS CLI installed and configured
- Terraform installed
- Python 3.11+ (for Lambda functions)

---





## Deployment Instructions

1. **Configure AWS CLI**
```batch
aws configure

2. **Zip Lambda Functions**
```batch
cd lambdas/ingest
zip handler.zip handler.py
cd ../read_recent
zip handler.zip handler.py
cd ../../terraform



3. **Deploy with Terraform**
```batch
terraform init
terraform apply


- Confirm with yes

- Terraform outputs:

    - ingest_url

    - read_recent_url

4. **Testing the Lambdas**
```powershell
cd tests
- for ingest 
python invoke_lambda_url.py
- for read_recent
python read_recent_lambda.py