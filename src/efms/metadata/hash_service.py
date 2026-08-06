import hashlib

from pathlib import Path


class HashService:

    CHUNK_SIZE = 8192

    @staticmethod
    def sha256(file_path: Path) -> str:

        hash_object = hashlib.sha256()

        with open(file_path, "rb") as file:

            while chunk := file.read(HashService.CHUNK_SIZE):

                hash_object.update(chunk)

        return hash_object.hexdigest()