from pathlib import Path

from efms.managers.folder_manager import FolderManager


def test_scan_files(

    sample_directory: Path,

):

    manager = FolderManager()

    files = manager.scan_files(

        sample_directory,

    )

    assert len(files) == 2


def test_search_extension(

    sample_directory: Path,

):

    manager = FolderManager()

    result = manager.search_by_extension(

        sample_directory,

        ".pdf",

    )

    assert len(result) == 1


def test_search_keyword(

    sample_directory: Path,

):

    manager = FolderManager()

    result = manager.search_by_keyword(

        sample_directory,

        "note",

    )

    assert len(result) == 1