def analyze_user(data):
    return {
        "name": data.get("name"),
        "followers": data.get("followers"),
        "public_repos": data.get("public_repos"),
        "following": data.get("following"),
        "bio": data.get("bio"),
    }