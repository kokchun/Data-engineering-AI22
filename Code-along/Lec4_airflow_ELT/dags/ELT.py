from airflow.decorators import dag, task_group, task
from datetime import datetime
from include.setup import setup_directories


@dag(dag_id = "queue_time_ELT", start_date=datetime(2023,6,8))
def queue_time_ELT():
    setup = setup_directories()

    setup

queue_time_ELT()

#%%