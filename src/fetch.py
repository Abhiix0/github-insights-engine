import requests


def fetch_user(username):
    url = f"https://api.github.com/users/{username}"

    response = requests.get(url)

    if response.status_code != 200:
        raise Exception("User not found")

    return response.json()