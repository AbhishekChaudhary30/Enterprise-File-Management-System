from pathlib import Path

from efms.core.constants import WORKSPACE_DIRECTORY
from efms.services.backup_service import BackupService


service = BackupService()

workspace = WORKSPACE_DIRECTORY

backup = service.create_backup(workspace)

print("Backup Created")
print(backup)

print()

print("Available Backups")

for item in service.list_backups():

    print(item)