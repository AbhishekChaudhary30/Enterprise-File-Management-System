from datetime import datetime
from pathlib import Path

from efms.core.constants import REPORT_DIRECTORY
from efms.managers.folder_manager import FolderManager
from efms.services.duplicate_detection_service import (
    DuplicateDetectionService,
)
from efms.core.logger import logger


class ReportService:
    """
    Generates project reports.
    """

    def __init__(self) -> None:

        self.folder_manager = FolderManager()

        self.duplicate_service = DuplicateDetectionService()

    def generate(self, root: Path) -> Path:

        REPORT_DIRECTORY.mkdir(
            parents=True,
            exist_ok=True,
        )

        files = self.folder_manager.scan_files(root)

        folders = self.folder_manager.scan_folders(root)

        duplicates = self.duplicate_service.find_duplicates(root)

        report = REPORT_DIRECTORY / "report.txt"

        with open(

            report,

            "w",

            encoding="utf-8",

        ) as file:

            file.write(

                "Enterprise File Management Report\n"

            )

            file.write(

                "=" * 50 + "\n\n"

            )

            file.write(

                f"Generated : {datetime.now()}\n\n"

            )

            file.write(

                f"Total Files : {len(files)}\n"

            )

            file.write(

                f"Total Folders : {len(folders)}\n"

            )

            file.write(

                f"Duplicate Groups : {len(duplicates)}\n"

            )

            duplicate_files = sum(

                len(group)

                for group

                in duplicates.values()

            )

            file.write(

                f"Duplicate Files : {duplicate_files}\n"

            )

        logger.info(

            "Report generated: %s",

            report,

        )

        return report