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
    response = requests.get(f"https://queue-times.com/parks/{theme_park}/queue_times.json")

    if response.status_code == 200: 
        return response.json()["rides"]

def _transform_stockholm_timezone(task_instance):
    data = task_instance.xcom_pull(task_ids = "extract_liseberg.extract_queue_time")

    



@task_group(group_id="extract_liseberg")
def extract_queue_time():
    extract_queue_time = PythonOperator(
        task_id="extract_queue_time", python_callable=_extract_queue_time
    )
