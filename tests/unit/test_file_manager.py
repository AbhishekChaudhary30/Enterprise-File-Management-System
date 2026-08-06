from pathlib import Path

from efms.managers.file_manager import FileManager


def test_copy(sample_text_file: Path):

    manager = FileManager()

    destination = sample_text_file.parent / "copy.txt"

    manager.copy(

        sample_text_file,

        destination,

    )

    assert destination.exists()

    assert (

        destination.read_text(

            encoding="utf-8"

        )

        ==

        sample_text_file.read_text(

            encoding="utf-8"

        )

    )


def test_move(sample_text_file: Path):

    manager = FileManager()

    destination = sample_text_file.parent / "moved.txt"

    manager.move(

        sample_text_file,

        destination,

    )

    assert destination.exists()

    assert not sample_text_file.exists()


def test_rename(sample_text_file: Path):

    manager = FileManager()

    manager.rename(

        sample_text_file,

        "renamed.txt",

    )

    renamed = sample_text_file.parent / "renamed.txt"

    assert renamed.exists()


def test_delete(sample_text_file: Path):

    manager = FileManager()

    manager.delete(

        sample_text_file,

    )

    assert not sample_text_file.exists()