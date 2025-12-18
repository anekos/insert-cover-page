from pathlib import Path
from typing import Iterator


def insert_covers(original: Path, output: Path, covers: Iterator[Path]) -> None:
    print(f"Inserting covers {len(covers)} pages into {original}")
