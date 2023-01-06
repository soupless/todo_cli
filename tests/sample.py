from __future__ import annotations

import rich_click as click
from rich_click.cli import patch

patch()

@click.command()
@click.option('-i', '--id', prompt=True, help="The identifier of the path")
@click.option('-p', '--path', prompt=True, help="The path indeed")
def hello(id: str, path: str):
    click.echo(f"id: {id}\npath: {path.__repr__()}")

if __name__ == '__main__':
    hello()
