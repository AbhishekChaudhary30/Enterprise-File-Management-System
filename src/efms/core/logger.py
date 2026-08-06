import logging

from pathlib import Path

from efms.core.constants import LOG_DIRECTORY
from efms.core.settings import settings

LOG_DIRECTORY.mkdir(parents=True, exist_ok=True)

LOG_FILE = LOG_DIRECTORY / "application.log"


logger = logging.getLogger("EFMS")

logger.setLevel(settings["log_level"])


formatter = logging.Formatter("%(asctime)s | %(levelname)s | %(message)s")


file_handler = logging.FileHandler(LOG_FILE, encoding="utf-8")

file_handler.setFormatter(formatter)


console_handler = logging.StreamHandler()

console_handler.setFormatter(formatter)


if not logger.handlers:

    logger.addHandler(file_handler)

    logger.addHandler(console_handler)
