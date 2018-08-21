from aws_xray_sdk.core import patch_all
from rover import rover
import json


def lambda_handler(event, context):
    if hasattr(context, 'aws_request_id'):
        patch_all()
    response = rover(event["body"].get("username"))

    print(json.dumps(response.json()))
    return {
        "body": response.json(),
        "headers": dict(response.headers),
        "status_code": int(response.status_code),
    }
