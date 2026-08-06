from pathlib import Path

import shutil

from efms.services.duplicate_detection_service import (

    DuplicateDetectionService,

)


def test_duplicate_detection(

    tmp_path: Path,

):

    file1 = tmp_path / "a.txt"

    file2 = tmp_path / "b.txt"

    file1.write_text(

        "HELLO",

        encoding="utf-8",

    )

    file2.write_text(

        "HELLO",

        encoding="utf-8",

    )

    duplicates = (

        DuplicateDetectionService()

        .find_duplicates(

            tmp_path,

        )

    )

    assert len(

        duplicates

    ) == 1