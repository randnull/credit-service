from .job_config import scheduler
from .job_functions import job_scoring, job_check_approved

from config.settings import settings


async def start_scheduler():
    delay: int = settings.SECONDS_DELAY_SCHEDULE
    check_approved_delay: int = settings.SECONDS_DELAY_SCHEDULE_APPROVED
    print('Scheduler starting...')
    scheduler.add_job(job_scoring, 'interval', seconds=delay)
    scheduler.add_job(job_check_approved, 'interval', seconds=check_approved_delay)
    scheduler.start()


async def stop_scheduler():
    print('Scheduler stoping...')
    scheduler.shutdown()
