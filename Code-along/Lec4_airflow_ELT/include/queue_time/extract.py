#%%
from airflow.operators.python import PythonOperator
import requests, pytz
from datetime import datetime
from airflow.decorators import task_group

theme_parks = {"liseberg": 11, "asterix": 9}

# TODO: for reader explore timezones yourself to see how it works
stockholm_timezone = pytz.timezone("Europe/Stockholm")

#%%

def _extract_queue_time(theme_park):
    pass


@task_group(group_id="extract_liseberg")
def extract_queue_time():
    extract_queue_time = PythonOperator(
        task_id="extract_queue_time", python_callable=_extract_queue_time
    )
