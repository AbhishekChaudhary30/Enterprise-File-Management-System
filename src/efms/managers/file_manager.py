from pathlib import Path
import shutil

from efms.core.logger import logger
from efms.core.constants import TRASH_DIRECTORY

from efms.core.interfaces import FileOperations
from efms.exceptions.file_exceptions import (
    DestinationAlreadyExistsError,
    InvalidFileError,
    SourceFileNotFoundError,
)


class FileManager(FileOperations):
    """
    Handles all file-related operations.
    """

    def _validate_source(self, source: Path) -> None:
        if not source.exists():
            raise SourceFileNotFoundError(f"Source file not found: {source}")

        if not source.is_file():
            raise InvalidFileError(f"Invalid file: {source}")

    def copy(self, source: Path, destination: Path) -> None:
        self._validate_source(source)

        if destination.exists():
            raise DestinationAlreadyExistsError(
                f"Destination already exists: {destination}"
            )

        shutil.copy2(source, destination)
        logger.info(
            "Copied file: %s -> %s",
            source,
            destination
        )

    def move(self, source: Path, destination: Path) -> None:
        self._validate_source(source)

        if destination.exists():
            raise DestinationAlreadyExistsError(
                f"Destination already exists: {destination}"
            )

        shutil.move(str(source), str(destination))
        logger.info(
            "Moved file: %s -> %s",
            source,
            destination
        )

    def rename(self, source: Path, new_name: str) -> None:
        self._validate_source(source)

        destination = source.with_name(new_name)

        if destination.exists():
            raise DestinationAlreadyExistsError(
                f"Destination already exists: {destination}"
            )
        
        source.rename(destination)

        logger.info(

            "Renamed file: %s -> %s",
            source,
            destination
        )

    def delete(self, target: Path) -> Path:

        self._validate_source(target)

        destination = TRASH_DIRECTORY / target.name

        counter = 1

        while destination.exists():

            destination = (
                TRASH_DIRECTORY /
                f"{target.stem}_{counter}{target.suffix}"
            )

            counter += 1

        shutil.move(
            str(target),
            str(destination),
        )

        logger.info(
            "Moved to trash: %s",
            destination
        )
        
        print("=" * 60)
        print("TARGET      :", target)
        print("DESTINATION :", destination)
        print("EXISTS      :", destination.exists())
        print("=" * 60)

        return destination
    
    def restore(
            self,
            trash_file: Path,
            destination: Path,
        ):

            shutil.move(
                str(trash_file),
                str(destination),
            )


    def permanent_delete(
            self,
            trash_file: Path,
        ):

            trash_file.unlink()
    
