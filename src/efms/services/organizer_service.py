from pathlib import Path

from efms.managers.file_manager import FileManager
from efms.managers.folder_manager import FolderManager

from efms.utils.file_utils import get_extension

from efms.core.settings import settings

from efms.core.logger import logger
 
class OrganizerService:
    """
    Organizes files by their extensions.
    """

    def __init__(self) -> None:
        self.file_manager = FileManager()
        self.folder_manager = FolderManager()

    def organize_by_extension(self, root: Path) -> None:
        """
        Organize files into folders based on file extension.
        """

        files = self.folder_manager.scan_files(root)

        for file in files:

            extension = get_extension(file)

            organization_root = root / settings["organization_folder"]

            destination_folder = organization_root / extension

            self.folder_manager.create_folder(destination_folder)

            destination = destination_folder / file.name

            if file == destination:
                continue

            self.file_manager.move(file, destination)
            
            logger.info(
                "Organized file: %s",
                file.name,
            )
            
        logger.info(
            "Organization completed."
        )