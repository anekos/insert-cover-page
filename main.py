import shutil
import subprocess
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
@click.argument("backup-directory", type=TypePath, required=True)
@click.argument("covers", type=TypePath, required=True, nargs=-1)
@click.option(
    "-n",
    "--notify",
    is_flag=True,
    help="Send a desktop notification after processing (requires notify-send).",
)
def main_insert(
    original: Path,
    output: Path,
    backup_directory: Path,
    covers: Iterator[Path],
    notify: bool,
) -> None:
    insert_covers(
        original=original,
        output=output,
        backup_directory=backup_directory,
        covers=covers,
    )

    if notify:
        notify_completion(output)


def notify_completion(output: Path) -> None:
    message = f"insert-cover-page: wrote {output}"

    if shutil.which("notify-send"):
        subprocess.run(["notify-send", "-u", "low", message], check=False)
    else:
        click.echo(message)


if __name__ == "__main__":
    main()
