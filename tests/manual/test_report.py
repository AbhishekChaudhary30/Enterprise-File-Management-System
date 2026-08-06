from efms.core.constants import WORKSPACE_DIRECTORY

from efms.services.report_service import ReportService


service = ReportService()

report = service.generate(

    WORKSPACE_DIRECTORY

)

print(report)