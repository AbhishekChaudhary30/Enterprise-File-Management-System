from pathlib import Path

from efms.metadata.metadata_service import MetadataService


def test_metadata(

    sample_text_file: Path,

):

    metadata = MetadataService.build(

        sample_text_file,

    )

    assert metadata.name == "sample.txt"

    assert metadata.extension == ".txt"

    assert metadata.size > 0

    assert len(

        metadata.sha256

    ) == 64