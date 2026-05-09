import requests
import os
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("GITHUB_TOKEN")

def fetch_user(username):
    url = f"https://api.github.com/users/{username}"

    headers = {
    "Authorization": f"Bearer {TOKEN}"
    }

    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        raise Exception("User not found")

    return response.json()

def fetch_repositories(username):
    url = f"https://api.github.com/users/{username}/repos"

    headers = {
    "Authorization": f"Bearer {TOKEN}"
    }

    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        raise Exception("Repositories not found")

    return response.json()