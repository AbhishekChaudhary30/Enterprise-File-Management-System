from pathlib import Path


def get_extension(path: Path) -> str:
    """
    Return file extension without dot.
    """
    extension = path.suffix.lower().replace(".", "")
    return extension if extension else "no_extension"


def get_filename(path: Path) -> str:
    """
    Return filename with extension.
    """
    return path.name


def get_stem(path: Path) -> str:
    """
    Return filename without extension.
    """
    return path.stem
