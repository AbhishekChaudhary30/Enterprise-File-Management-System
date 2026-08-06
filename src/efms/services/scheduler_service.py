import time
import schedule

from efms.core.logger import logger


class SchedulerService:

    @staticmethod
    def register(job, every_minutes: int = 1):

        schedule.every(
            every_minutes
        ).minutes.do(job)

        logger.info(
            "Scheduler job registered."
        )

    @staticmethod
    def start():

        logger.info(
            "Scheduler started."
        )

        while True:

            schedule.run_pending()

            time.sleep(1)