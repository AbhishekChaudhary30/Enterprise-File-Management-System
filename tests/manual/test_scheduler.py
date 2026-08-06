from datetime import datetime

from efms.services.scheduler_service import SchedulerService


def sample_job():

    print(
        "Running Job",
        datetime.now(),
    )


SchedulerService.register(
    sample_job,
    every_minutes=1,
)

SchedulerService.start()