from pathlib import Path

from efms.metadata.hash_service import HashService


def test_sha256(

    sample_text_file: Path,

):

    value = HashService.sha256(

        sample_text_file,

    )

    assert isinstance(

        value,

        str,

    )

    assert len(value) == 64