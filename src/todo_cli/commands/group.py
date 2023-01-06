from __future__ import annotations

import rich_click as click
from rich_click.cli import patch

patch()

@click.group(name="group")
def group() -> None:
    """Subcommand for todo groups"""
    pass

@group.command()
@click.option('-i', '--id', prompt=True, help="The identifier of the path", type=str)
@click.option('-p', '--path', prompt=True, help="The path indeed", type=str)
def create(id, path) -> None:
    click.echo(f"Received id '{id}' and path '{path}'")
