from rover import rover


def lambda_handler(event, context):
    response = rover(event["body"].get("username"))
    print(response.json())
    return {
        "body": response.json(),
        "headers": dict(response.headers),
        "status_code": int(response.status_code),
    }
