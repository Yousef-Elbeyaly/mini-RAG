from celery_app import celery_app
from helpers.config import get_settings
import logging
from time import sleep
from datetime import datetime
import asyncio

logger = logging.getLogger("celery.task")

@celery_app.task(bind=True, name="tasks.mail_sevice.send_email_reports")
def send_email_reports(self, mail_wait_seconds: int):

    return asyncio.run(_send_email_reports(self, mail_wait_seconds))

async def _send_email_reports(task_instance, mail_wait_seconds: int):

    started_at = str(datetime.now())

    task_instance.update_state(
          state="PROGRESS",
          metadata={
                "started_at":started_at
          }
    )

    for ix in range(15):
            logger.info(f"Send email to user: {ix}")
            await asyncio.sleep(3)

    return {
          "no_emails": 15,
          "end_at": str(datetime.now())
    }