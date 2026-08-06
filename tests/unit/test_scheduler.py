import schedule

from efms.services.scheduler_service import SchedulerService


def dummy():

    pass


def test_scheduler_register():

    schedule.clear()

    SchedulerService.register(

        dummy,

        every_minutes=1,

    )

    jobs = schedule.get_jobs()

    assert len(jobs) == 1

    schedule.clear()