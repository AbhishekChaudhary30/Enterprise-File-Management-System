from pathlib import Path

from efms.metadata.metadata_service import MetadataService

from efms.core.constants import SAMPLE_DATA_DIRECTORY


metadata = MetadataService.build(

    SAMPLE_DATA_DIRECTORY /

    "documents" /

    "Resume1.docx"

)

print(metadata)