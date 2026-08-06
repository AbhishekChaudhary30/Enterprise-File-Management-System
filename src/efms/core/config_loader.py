import json

from pathlib import Path


class ConfigLoader:

    def __init__(self, config_file: Path):

        self._config_file = config_file

        self._config = self.load()

    def load(self) -> dict:

        with open(self._config_file, "r", encoding="utf-8") as file:

            return json.load(file)

    @property
    def config(self):

        return self._config