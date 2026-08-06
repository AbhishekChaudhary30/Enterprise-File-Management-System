from pathlib import Path

import pytest


@pytest.fixture
def sample_text_file(tmp_path: Path) -> Path:
    """
    Creates a temporary text file.
    """

    file = tmp_path / "sample.txt"

    file.write_text(

        "Hello Enterprise File Manager",

        encoding="utf-8",

    )

    return file


@pytest.fixture
def sample_pdf_file(tmp_path: Path) -> Path:
    """
    Creates a temporary PDF file.
    """

    file = tmp_path / "report.pdf"

    file.write_bytes(

        b"PDF CONTENT"

    )

    return file


@pytest.fixture
def sample_directory(tmp_path: Path) -> Path:
    """
    Creates a temporary directory with files.
    """

    folder = tmp_path / "workspace"

    folder.mkdir()

    (folder / "notes.txt").write_text(

        "Notes",

        encoding="utf-8",

    )

    (folder / "report.pdf").write_bytes(

        b"PDF"

    )

    return folder