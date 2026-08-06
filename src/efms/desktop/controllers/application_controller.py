from pathlib import Path

from efms.managers.file_manager import FileManager
from efms.managers.folder_manager import FolderManager
from efms.services.history_service import HistoryService

from efms.services.scan_service import ScanService
from efms.services.organizer_service import OrganizerService
from efms.services.duplicate_detection_service import (
    DuplicateDetectionService,
)
from efms.services.backup_service import BackupService
from efms.services.report_service import ReportService

from efms.database.repository import (
    FileRepository,
)


class ApplicationController:
    """
    Coordinates the Desktop UI with backend services.
    """

    def __init__(self) -> None:

        self.file_manager = FileManager()

        self.folder_manager = FolderManager()

        self.scan_service = ScanService()

        self.organizer_service = OrganizerService()

        self.duplicate_service = DuplicateDetectionService()

        self.backup_service = BackupService()

        self.report_service = ReportService()
        
        self.repository = FileRepository()
        
        self.history_service = HistoryService()

    def scan_directory(
        self,
        path: Path,
    ) -> dict:

        return self.scan_service.scan(path)
    
    def search(
        self,
        root: Path,
        value: str,
        search_type: str,
    ):

        if search_type == "Name":

            return self.folder_manager.search_by_name(
                root,
                value,
            )

        elif search_type == "Extension":

            if not value.startswith("."):

                value = "." + value

            return self.folder_manager.search_by_extension(
                root,
            value,
            )

        return self.folder_manager.search_by_keyword(
            root,
            value,
        )
        
        def organize(
            self,
            root: Path,
        ):

            self.organizer_service.organize_by_extension(
                root,
            )
        
    def find_duplicates(
        self,
        root: Path,
    ):

        return self.duplicate_service.find_duplicates(
            root
        )
        
    def create_backup(
        self,
        root: Path,
    ):

        return self.backup_service.create_backup(
            root
        )
        
    def generate_report(
        self,
        root: Path,
    ):

        return self.report_service.generate(
            root
        )
        
    def copy_file(
        self,
        source: Path,
        destination: Path,
    ):

        self.file_manager.copy(
            source,
            destination,
        )
        
        self.repository.add_history("COPY", str(source), "SUCCESS")
        
        self.history_service.push(
            {
                "action": "COPY",
                "source": str(source),
                "destination": str(destination),
            }
        )


    def move_file(
        self,
        source: Path,
        destination: Path,
    ):

        self.file_manager.move(
            source,
            destination,
        )
        
        self.repository.add_history("MOVE", str(source), "SUCCESS")
        
        self.history_service.push(
            {
                "action": "MOVE",
                "source": str(source),
                "destination": str(destination),
            }
        )


    def rename_file(
        self,
        source: Path,
        new_name: str,
    ):

        self.file_manager.rename(
            source,
            new_name,
        )
        
        self.repository.add_history("RENAME", str(source), "SUCCESS")
        self.history_service.push(
            {
                "action": "RENAME",
                "source": str(source),
                "destination": str(new_name),
            }
        )

    def delete_file(
            self,
            target: Path,
        ):

            trash = self.file_manager.delete(target)

            self.repository.add_history(

                "DELETE",

                str(target),

                "SUCCESS",

            )

            self.history_service.push(

                {

                    "action": "DELETE",

                    "source": str(target),

                    "trash": str(trash),

                }

            )
        
    def recent_history(self):

        return self.repository.get_recent_history()
    
    def undo(self):

        action = self.history_service.undo()

        if action is None:

            return False

        action_type = action["action"]

        if action_type == "COPY":

            self.file_manager.delete(

                Path(action["destination"])
                
            )

        elif action_type == "MOVE":

            self.file_manager.move(

                Path(action["destination"]),

                Path(action["source"]),

            )

        elif action_type == "RENAME":

            current = Path(action["source"]).with_name(

                action["new_name"]

            )

            self.file_manager.rename(

                current,

                Path(action["source"]).name,

            )

        else:

            return False

        return True
    
    def redo(self):

        action = self.history_service.redo()

        if action is None:

            return False

        action_type = action["action"]

        if action_type == "COPY":

            self.file_manager.copy(

                Path(action["source"]),

                Path(action["destination"]),

            )

        elif action_type == "MOVE":

            self.file_manager.move(

                Path(action["source"]),

                Path(action["destination"]),

            )

        elif action_type == "RENAME":

            self.file_manager.rename(

                Path(action["source"]),

                action["new_name"],

            )

        else:

            return False

        return True
    
    def restore_file(
            self,
            trash_file: Path,
            destination: Path,
        ):

            self.file_manager.restore(

                trash_file,

                destination,

            )


    def permanent_delete(
            self,
            trash_file: Path,
        ):

            self.file_manager.permanent_delete(

                trash_file,

        )
    
    def list_trash(self):

        trash = Path("data/.trash")

        if not trash.exists():

            return []

        return list(trash.rglob("*"))