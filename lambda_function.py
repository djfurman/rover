from aws_xray_sdk.core import xray_recorder
from aws_xray_sdk.core import patch_all
from rover import rover

xray_recorder.configure(aws_xray_tracing_name="Rover")
patch_all()


def lambda_handler(event, context):
    response = rover(event["body"].get("username"))
    print(response.json())
    return {
        "body": response.json(),
        "headers": dict(response.headers),
        "status_code": int(response.status_code),
    }
