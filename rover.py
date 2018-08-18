import requests


def rover(user_name):
    url = f"https://api.github.com/users/{user_name}"
    return requests.get(url)
