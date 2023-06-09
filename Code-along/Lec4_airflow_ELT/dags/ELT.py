from airflow.decorators import dag, task_group, task
from datetime import datetime
from include.setup import setup_directories
from include.queue_time.extract import extract_queue_time
from include.queue_time.load import load_datalake


@dag(
    dag_id="queue_time_ELT",
    start_date=datetime(2023, 6, 8),
    schedule="*/5 * * * *",
    end_date=datetime(2023, 6, 11),
    catchup=False,
)
def queue_time_ELT():
    setup = setup_directories()
    extract_queue_time_ = extract_queue_time()
    load_queue_time = load_datalake()

    # dummy parallel task_group
    @task_group(group_id = "extract_airquality")
    def airquality():
        @task(task_id = "extract")
        def extract():
            return "temperature dummy"


    setup >> extract_queue_time_ >> load_queue_time

    setup >> airquality()

queue_time_ELT()

# %%
