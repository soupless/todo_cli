from __future__ import annotations

import rich_click as click
from rich_click.cli import patch

patch()

from .commands.group import group
from .commands.task import task
# from commands import group, task

@click.group()
def main():
    """
    Make todos
    """
    pass

if __name__ == '__main__':
    main.add_command(group)
    main.add_command(task)
    main()
