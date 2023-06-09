from airflow.decorators import task_group
from include.setup import datalake_path
from airflow.operators.python import PythonOperator
import json


def _load_datalake(task_instance):
    data = task_instance.xcom_pull(task_ids = "extract_liseberg.transform_stockholm_timezone")

    filename = datalake_path / f"{data[0]['last_updated']}.json"

    with open(filename, "w") as file:
        json.dump(data, file)


@task_group(group_id="load_queue_time")
def load_datalake():
    load = PythonOperator(task_id = "load_datalake", python_callable=_load_datalake)
    
    load