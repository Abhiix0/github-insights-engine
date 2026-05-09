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


def extract_repo_data(repos):
    sorted_repos = sorted(
        repos, key=lambda repo: repo["stargazers_count"], reverse=True
    )

    repo_names = []
    repo_stars = []
    repo_forks = []

    for repo in sorted_repos:
        repo_names.append(repo["name"])
        repo_stars.append(repo["stargazers_count"])
        repo_forks.append(repo["forks_count"])

    repo_names = repo_names[:5]
    repo_stars = repo_stars[:5]
    return repo_names, repo_stars, repo_forks


def extract_commit_data(username, repos, fetch_commit_count):
    repo_names = []
    commit_counts = []

    for repo in repos:
        repo_name = repo["name"]

        commits = fetch_commit_count(username, repo_name)

        repo_names.append(repo_name)
        commit_counts.append(commits)

    return repo_names, commit_counts
