import json
import requests
from botocore.auth import SigV4Auth
from botocore.awsrequest import AWSRequest
from botocore.session import Session

# ReadRecent Lambda URL
FUNCTION_URL = "https://6ayprkruksldb7q3pp3ssraxre0hwlcw.lambda-url.us-east-1.on.aws/"
REGION = "us-east-1"
SERVICE = "lambda"

payload = {}

# Get AWS credentials from IAM user
session = Session()
credentials = session.get_credentials()

# Prepare AWS signed request
aws_request = AWSRequest(
    method="GET", 
    url=FUNCTION_URL,
    data=json.dumps(payload),
    headers={"Content-Type": "application/json"}
)

# Sign request using SigV4
SigV4Auth(credentials, SERVICE, REGION).add_auth(aws_request)

# Make the HTTP request
response = requests.request(
    method="GET",
    url=FUNCTION_URL,
    headers=dict(aws_request.headers),
    data=aws_request.body
)

# Print the results
print("Status:", response.status_code)
print("Response:", response.text)
