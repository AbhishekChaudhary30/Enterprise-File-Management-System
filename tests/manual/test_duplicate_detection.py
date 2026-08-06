from efms.services.duplicate_detection_service import (

    DuplicateDetectionService,

)

from efms.core.constants import SAMPLE_DATA_DIRECTORY


service = DuplicateDetectionService()

duplicates = service.find_duplicates(

    SAMPLE_DATA_DIRECTORY

)

if not duplicates:

    print("No duplicate files found.")

else:

    print("=" * 60)

    print("Duplicate Files")

    print("=" * 60)

    for file_hash, files in duplicates.items():

        print()

        print(f"HASH : {file_hash}")

        for file in files:

            print(

                f"   {file.absolute_path}"

            )