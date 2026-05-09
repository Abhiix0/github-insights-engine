import sys

from fetch import fetch_user, fetch_repositories, fetch_commit_count
from analyze import (
    analyze_user,
    analyze_repositories,
    extract_repo_data,
    extract_commit_data,
)

from visualize import show_stats, plot_repo_stars, plot_commit_activity


def main():
    if len(sys.argv) < 2:
        print("Usage: python main.py <github_username>")
        return

    username = sys.argv[1]

    data = fetch_user(username)

    stats = analyze_user(data)

    repos = fetch_repositories(username)

    repo_stats = analyze_repositories(repos)

    repo_names, repo_stars, repo_forks = extract_repo_data(repos)

    repo_names, commit_counts = extract_commit_data(username, repos, fetch_commit_count)

    stats.update(repo_stats)

    show_stats(stats)

    plot_repo_stars(repo_names, repo_stars)

    plot_commit_activity(repo_names, commit_counts)


if __name__ == "__main__":
    main()
