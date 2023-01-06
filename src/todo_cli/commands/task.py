from __future__ import annotations

import rich_click as click
from rich_click.cli import patch

patch()

@click.group(name="task")
def task() -> None:
    """Subcommand for tasks"""
    pass
