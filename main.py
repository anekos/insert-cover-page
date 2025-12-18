from pathlib import Path
from typing import Iterator

import click

from app.core import insert_covers

TypePath = click.types.Path(path_type=Path)


@click.group()
@click.pass_context
def main(ctx: click.Context) -> None:
    # ctx.obj = App()
    pass


@main.command("insert")
@click.argument("original", type=TypePath, required=True)
@click.argument("output", type=TypePath, required=True)
@click.argument("covers", type=TypePath, required=True, nargs=-1)
def main_insert(original: Path, output: Path, covers: Iterator[Path]) -> None:
    insert_covers(original, output, covers)


if __name__ == "__main__":
    main()
