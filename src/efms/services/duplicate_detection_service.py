from pathlib import Path

from collections import defaultdict

from efms.metadata.metadata_service import MetadataService

from efms.models.file_metadata import FileMetadata

from efms.managers.folder_manager import FolderManager


class DuplicateDetectionService:

    def __init__(self) -> None:

        self.folder_manager = FolderManager()

    def find_duplicates(

        self,

        root: Path,

    ) -> dict[str, list[FileMetadata]]:

        duplicates = defaultdict(list)

        files = self.folder_manager.scan_files(root)

        for file in files:

            metadata = MetadataService.build(file)

            duplicates[metadata.sha256].append(metadata)

        return {

            file_hash: metadata_list

            for file_hash, metadata_list in duplicates.items()

            if len(metadata_list) > 1

        }