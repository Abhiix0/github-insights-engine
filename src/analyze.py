def analyze_user(data):
    return {
        "name": data.get("name"),
        "followers": data.get("followers"),
        "public_repos": data.get("public_repos"),
        "following": data.get("following"),
        "bio": data.get("bio"),
    }
def analyze_repositories(repos):
    total_stars = 0
    total_forks = 0

    top_repo = None
    max_stars = -1

    for repo in repos:
        stars = repo["stargazers_count"]
        forks = repo["forks_count"]

        total_stars += stars
        total_forks += forks

        if stars > max_stars:
            max_stars = stars
            top_repo = repo["name"]

    return {
        "total_repositories": len(repos),
        "total_stars": total_stars,
        "total_forks": total_forks,
        "top_repository": top_repo,
    }