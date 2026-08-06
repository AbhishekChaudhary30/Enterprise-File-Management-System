from dataclasses import dataclass

from pathlib import Path

from datetime import datetime


@dataclass(slots=True)
class FileMetadata:

    name: str

    extension: str

    size: int

    absolute_path: Path

    created_time: datetime

    modified_time: datetime

    sha256: str