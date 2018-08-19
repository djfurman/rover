from aws_xray_sdk.core import patch_all
from rover import rover


def lambda_handler(event, context):
    if "aws_request_id" not in context.keys():
        patch_all()
    response = rover(event["body"].get("username"))
    print(response.json())
    return {
        "body": response.json(),
        "headers": dict(response.headers),
        "status_code": int(response.status_code),
    }
