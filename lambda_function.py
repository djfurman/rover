import rover


def lambda_function(event, context):
    response = rover(event.get("username"))
    print(response)
    return response
