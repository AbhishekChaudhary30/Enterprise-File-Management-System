from datetime import datetime
from pathlib import Path
import shutil

from efms.core.constants import BACKUP_DIRECTORY
from efms.core.logger import logger


class BackupService:
    """
    Handles backup and restore operations.
    """

    def create_backup(self, source: Path) -> Path:
        """
        Create a timestamped backup of a directory.
        """

        if not source.exists():
            raise FileNotFoundError(f"Source not found: {source}")

        BACKUP_DIRECTORY.mkdir(parents=True, exist_ok=True)

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

        backup_path = BACKUP_DIRECTORY / f"{source.name}_{timestamp}"

        shutil.copytree(source, backup_path)

        logger.info(
            "Backup created: %s",
            backup_path,
        )

        return backup_path

    def list_backups(self) -> list[Path]:
        """
        Return all backups.
        """

        if not BACKUP_DIRECTORY.exists():
            return []

        return sorted(
            BACKUP_DIRECTORY.iterdir(),
            key=lambda item: item.stat().st_mtime,
            reverse=True,
        )

    def restore_backup(
        self,
        backup_path: Path,
        destination: Path,
    ) -> None:
        """
        Restore a backup.
        """

        if destination.exists():
            shutil.rmtree(destination)

        shutil.copytree(
            backup_path,
            destination,
        )

        logger.info(
            "Backup restored: %s -> %s",
            backup_path,
            destination,
        )