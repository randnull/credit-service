from .job_config import scheduler
from .job_functions import send_to_origination, check_overdue

from config.settings import settings


async def start_scheduler():
    delay: int = settings.SECONDS_DELAY_SCHEDULE
    check_overdue_delay: int = settings.SECONDS_DELAY_SCHEDULE_OVERDUE
    print('Scheduler starting...')
    scheduler.add_job(send_to_origination, 'interval', seconds=delay)
    scheduler.add_job(check_overdue, 'interval', seconds=check_overdue_delay)
    scheduler.start()


async def stop_scheduler():
    print('Scheduler stoping...')
    scheduler.shutdown()
