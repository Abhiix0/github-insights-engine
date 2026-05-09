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