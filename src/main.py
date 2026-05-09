import sys

from fetch import fetch_user
from analyze import analyze_user
from visualize import show_stats
from fetch import fetch_user, fetch_repositories
from analyze import analyze_user, analyze_repositories

def main():
    if len(sys.argv) < 2:
        print("Usage: python main.py <github_username>")
        return

    username = sys.argv[1]

    data = fetch_user(username)

    stats = analyze_user(data)

    repos = fetch_repositories(username)

    repo_stats = analyze_repositories(repos)

    stats.update(repo_stats)

    show_stats(stats)


if __name__ == "__main__":
    main()