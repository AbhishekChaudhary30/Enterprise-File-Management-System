class FileManagerError(Exception):
    """Base exception for file manager."""


class SourceFileNotFoundError(FileManagerError):
    """Raised when source file does not exist."""


class DestinationAlreadyExistsError(FileManagerError):
    """Raised when destination already exists."""


class InvalidFileError(FileManagerError):
    """Raised when path is not a valid file."""
