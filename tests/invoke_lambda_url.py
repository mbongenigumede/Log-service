import json
import requests
from botocore.auth import SigV4Auth
from botocore.awsrequest import AWSRequest
from botocore.session import Session

FUNCTION_URL = "https://cfzwxr4feibsrjaf5baanedgri0pgxot.lambda-url.us-east-1.on.aws/"
REGION = "us-east-1"
SERVICE = "lambda"

payload = {
    "severity": "info",
    "message": "test log"
}

session = Session()
credentials = session.get_credentials()

aws_request = AWSRequest(
    method="POST",
    url=FUNCTION_URL,
    data=json.dumps(payload),
    headers={"Content-Type": "application/json"}
)

SigV4Auth(credentials, SERVICE, REGION).add_auth(aws_request)

response = requests.post(
    FUNCTION_URL,
    headers=dict(aws_request.headers),
    data=aws_request.body
)

print("Status:", response.status_code)
print("Response:", response.text)
