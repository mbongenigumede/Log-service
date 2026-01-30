import json, os, boto3

db = boto3.resource("dynamodb").Table(os.environ["TABLE_NAME"])

def handler(event, context):
    res = db.query(
        KeyConditionExpression="pk = :pk",
        ExpressionAttributeValues={":pk": "LOG"},
        ScanIndexForward=False,
        Limit=100
    )

    return {"statusCode": 200, "body": json.dumps(res.get("Items", []))}
