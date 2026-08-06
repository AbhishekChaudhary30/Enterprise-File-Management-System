from pathlib import Path

from efms.managers.folder_manager import FolderManager


class ScanService:
    """
    Business service responsible for scanning directories.
    """

    def __init__(self) -> None:

        self.folder_manager = FolderManager()

    def scan(self, path: Path) -> dict:

        files = self.folder_manager.scan_files(path)

        return {

            "total_files": len(files),

            "files": [

                str(file)

                for file

                in files

            ],

        }