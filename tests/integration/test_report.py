from pathlib import Path

from efms.services.report_service import ReportService


def test_generate_report(tmp_path: Path):

    (tmp_path / "a.txt").write_text(
        "Hello",
        encoding="utf-8",
    )

    service = ReportService()

    report = service.generate(tmp_path)

    assert report.exists()
    assert report.name == "report.txt"