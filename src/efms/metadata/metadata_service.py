from datetime import datetime

from pathlib import Path

from efms.metadata.hash_service import HashService

from efms.models.file_metadata import FileMetadata


class MetadataService:

    @staticmethod
    def build(path: Path) -> FileMetadata:

        stat = path.stat()

        return FileMetadata(

            name=path.name,

            extension=path.suffix.lower(),

            size=stat.st_size,

            absolute_path=path.resolve(),

            created_time=datetime.fromtimestamp(stat.st_ctime),

            modified_time=datetime.fromtimestamp(stat.st_mtime),

            sha256=HashService.sha256(path),

        )