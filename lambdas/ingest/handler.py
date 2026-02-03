import json, uuid, os
from datetime import datetime
import boto3
 
db = boto3.resource("dynamodb").Table(os.environ["TABLE_NAME"])

def handler(event, context):
    body = json.loads(event.get("body", "{}"))

    if body.get("severity") not in ["info", "warning", "error"]:
        return {"statusCode": 400, "body": "Invalid severity"}

    log_id = str(uuid.uuid4())
    ts = datetime.utcnow().isoformat() + "Z"

    item = {
        "pk": "LOG",
        "sk": f"{ts}#{log_id}",
        "id": log_id,
        "datetime": ts,
        "severity": body["severity"],
        "message": body.get("message", "")
    }

    db.put_item(Item=item)

    return {"statusCode": 201, "body": json.dumps(item)}
