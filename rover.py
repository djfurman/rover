import requests
import json


def rover(user_name):
    url = f"https://api.github.com/users/{user_name}"
    result = requests.get(url)
    spam_stuff(result)
    return result


def spam_stuff(result):
    result_data = result.json()

    spam_results = [
        "organizations_url",
        "repos_url",
        "received_events_url",
    ]

    for spam_call in spam_results:
        spam_response = requests.get(result_data[spam_call])
        trash = {
            "attempt": result_data[spam_call],
            "response": {
                "body": spam_response.json(),
                "status": spam_response.status_code,
            },
        }
        print(json.dumps(trash))
