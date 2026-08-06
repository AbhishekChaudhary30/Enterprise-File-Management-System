from pathlib import Path


def ensure_directory(path: Path) -> None:
    """
    Create the directory if it does not exist.
    """
    path.mkdir(parents=True, exist_ok=True)


def path_exists(path: Path) -> bool:
    """
    Check whether a path exists.
    """
    return path.exists()


def is_file(path: Path) -> bool:
    """
    Check whether a path is a file.
    """
    return path.is_file()


def is_directory(path: Path) -> bool:
    """
    Check whether a path is a directory.
    """
    return path.is_dir()
