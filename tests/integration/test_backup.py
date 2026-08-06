from pathlib import Path

from efms.services.backup_service import BackupService


def test_create_backup(tmp_path: Path):

    workspace = tmp_path / "workspace"
    workspace.mkdir()

    (workspace / "notes.txt").write_text(
        "Backup Test",
        encoding="utf-8",
    )

    service = BackupService()

    backup = service.create_backup(workspace)

    assert backup.exists()
    assert backup.is_dir()
    assert (backup / "notes.txt").exists()