import matplotlib.pyplot as plt
from rich.console import Console
from rich.table import Table


console = Console()


def show_stats(stats):
    table = Table(title="GitHub Profile Analysis")

    table.add_column("Metric", style="cyan")
    table.add_column("Value", style="green")

    for key, value in stats.items():
        table.add_row(key, str(value))

    console.print(table)


def plot_repo_stars(repo_names, repo_stars):
    top_repo_names = repo_names[:5]
    top_repo_stars = repo_stars[:5]

    plt.figure(figsize=(12, 6))

    plt.bar(top_repo_names, top_repo_stars)

    plt.title("Top GitHub Repository Stars")
    plt.xlabel("Repositories")
    plt.ylabel("Stars")

    plt.xticks(rotation=15)

    plt.tight_layout()

    plt.show()


def plot_commit_activity(repo_names, commit_counts):
    plt.figure(figsize=(12, 6))

    plt.bar(repo_names, commit_counts)

    plt.title("Repository Commit Activity")
    plt.xlabel("Repositories")
    plt.ylabel("Commit Count")

    plt.xticks(rotation=15)

    plt.tight_layout()

    plt.show()
