from io import BytesIO
from pathlib import Path
from typing import Iterator

from PIL import Image
from pypdf import PdfReader, PdfWriter


def insert_covers(original: Path, output: Path, covers: Iterator[Path]) -> None:
    """
    Insert the pages generated from cover images before the original PDF pages.

    :param original: path to the original PDF
    :param output: path to write the combined PDF
    :param covers: iterable of image file paths to place before the PDF
    """
    cover_paths: list[Path] = [Path(path) for path in covers]

    writer = PdfWriter()

    # Convert each cover image into a PDF page and append.
    for cover_path in cover_paths:
        with Image.open(cover_path) as img:
            rgb_image = img.convert("RGB")
            buffer = BytesIO()
            rgb_image.save(buffer, format="PDF")
            buffer.seek(0)

            cover_pdf = PdfReader(buffer)
            for page in cover_pdf.pages:
                writer.add_page(page)

    # Append original PDF pages.
    original_pdf = PdfReader(str(original))
    for page in original_pdf.pages:
        writer.add_page(page)

    output.parent.mkdir(parents=True, exist_ok=True)
    with output.open("wb") as fp:
        writer.write(fp)
