from pathlib import Path

from efms.services.organizer_service import OrganizerService


def test_organizer(

    sample_directory: Path,

):

    OrganizerService().organize_by_extension(

        sample_directory,

    )

    assert (

        sample_directory

        /

        "organized"

        /

        "txt"

        /

        "notes.txt"

    ).exists()

    assert (

        sample_directory

        /

        "organized"

        /

        "pdf"

        /

        "report.pdf"

    ).exists()