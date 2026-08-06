from pathlib import Path
import shutil
from efms.core.logger import logger


class FolderManager:
    """
    Handles folder-related operations.
    """

    def create_folder(self, path: Path) -> None:
        from efms.utils.path_utils import ensure_directory

        ensure_directory(path)
        logger.info(
            "Created folder: %s",
            path
        )

    def delete_empty_folder(self, path: Path) -> None:
        path.rmdir()

    def delete_folder(self, path: Path) -> None:
        shutil.rmtree(path)
        logger.info(
            "Deleted folder: %s",
            path
        )

    def list_contents(self, path: Path) -> list[Path]:
        return list(path.iterdir())

    def exists(self, path: Path) -> bool:
        return path.exists() and path.is_dir()

    def scan(self, path: Path) -> list[Path]:
        """
        Recursively scan a directory and return all files and folders.
        """
        return list(path.rglob("*"))

    def scan_files(self, path: Path) -> list[Path]:
        """
        Return all files recursively.
        """
        return [item for item in path.rglob("*") if item.is_file()]

    def scan_folders(self, path: Path) -> list[Path]:
        """
        Return all folders recursively.
        """
        return [item for item in path.rglob("*") if item.is_dir()]

    def search_by_name(self, path: Path, filename: str) -> list[Path]:
        """
        Search files by exact filename.
        """
        return [
            file
            for file in self.scan_files(path)
            if file.name.lower() == filename.lower()
        ]

    def search_by_extension(self, path: Path, extension: str) -> list[Path]:
        """
        Search files by extension.
        Example: ".pdf"
        """
        extension = extension.lower()

        return [
            file for file in self.scan_files(path) if file.suffix.lower() == extension
        ]

    def search_by_keyword(self, path: Path, keyword: str) -> list[Path]:
        """
        Search files whose filename contains a keyword.
        """
        keyword = keyword.lower()

        return [file for file in self.scan_files(path) if keyword in file.stem.lower()]
