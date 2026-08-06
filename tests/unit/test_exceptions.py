import pytest

from pathlib import Path

from efms.managers.file_manager import FileManager
from efms.exceptions.file_exceptions import (
    SourceFileNotFoundError,
)


def test_source_not_found():

    manager = FileManager()

    with pytest.raises(
        SourceFileNotFoundError,
    ):

        manager.copy(
            Path("missing.txt"),
            Path("copy.txt"),
        )