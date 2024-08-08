# your_app/tasks.py

from celery import shared_task
from django.core.management import call_command
from django.core.cache import cache
import datetime
import logging

# Global variable to store the job status
job_status = {
    "job_name": "",
    "start_time": None,
    "end_time": None,
    "execution_time": None,
    "current_status": "Not started",
    "records_processed": 0  # Initialize records processed counter
}

STOP_JOB_FLAG = "stop_job_flag"

logging.basicConfig(filename='job_execution.log', level=logging.INFO, format='%(asctime)s - %(levelname)s: %(message)s')

@shared_task
def run_etl_task(jurisdiction):
    try:
        job_status["job_name"] = jurisdiction
        job_status["start_time"] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        job_status["current_status"] = "Running"

        # Reset the stop flag
        cache.set(STOP_JOB_FLAG, False)

        # Call your management command 'etl' and pass jurisdiction
        records = call_command('etl', jurisdiction=jurisdiction)

        job_status["end_time"] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        job_status["execution_time"] = str(datetime.datetime.strptime(job_status["end_time"], "%Y-%m-%d %H:%M:%S") - datetime.datetime.strptime(job_status["start_time"], "%Y-%m-%d %H:%M:%S"))
        job_status["current_status"] = "Completed"
        job_status["records_processed"] = records
        logging.info(f"Job '{jurisdiction}' completed successfully. Records processed: {records}")
    except Exception as e:
        job_status["current_status"] = "Failed"
        logging.error(f"Job '{jurisdiction}' failed with error: {str(e)}")
