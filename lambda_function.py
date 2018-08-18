from rover import rover


def lambda_handler(event, context):
    response = rover(event["body"].get("username"))
    print(response.json())
    return response
