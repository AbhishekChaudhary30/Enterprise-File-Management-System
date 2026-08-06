from abc import ABC, abstractmethod
from pathlib import Path


class FileOperations(ABC):
    """
    Abstract base class defining file operations.
    """

    @abstractmethod
    def copy(self, source: Path, destination: Path) -> None:
        """Copy a file."""
        pass

    @abstractmethod
    def move(self, source: Path, destination: Path) -> None:
        """Move a file."""
        pass

    @abstractmethod
    def rename(self, source: Path, new_name: str) -> None:
        """Rename a file."""
        pass

    @abstractmethod
    def delete(self, target: Path) -> None:
        """Delete a file."""
        pass
