# %%
from airflow.operators.bash import BashOperator
from airflow import DAG
from datetime import datetime
from dotenv import load_dotenv
import os
from pathlib import Path

load_dotenv()

API_NINJA_KEY = os.environ.get("API_NINJA")

data_lake_path = Path(__file__).parents[1] / "data" / "data_lake"

data_warehouse_path = Path(__file__).parents[1] / "data/data_warehouse"
time_variable = "$(date +%y%m%d_%H%M)"
# %%
with DAG(
    dag_id="joke_dag",
    schedule="*/2 * * * *",
    start_date=datetime(2023, 5, 28),
    catchup=False,
):
    setup_folders = BashOperator(
        task_id="setup_folders",
        bash_command=f"mkdir -p {data_lake_path} {data_warehouse_path}",
    )

    download_joke = BashOperator(
        task_id="random_joke",
        bash_command=f"curl -o {data_lake_path}/joke_{time_variable}.json https://official-joke-api.appspot.com/random_joke",
    )

    download_norris_joke = BashOperator(
        task_id="chuck_norris_joke",
        bash_command=f"curl -H 'X-Api-Key: {API_NINJA_KEY}' -o {data_lake_path}/norris_{time_variable}.json https://api.api-ninjas.com/v1/chucknorris",
    )

    notify_number_files = BashOperator(
        task_id="notify_number_files",
        bash_command=f"echo $(ls {data_lake_path}| wc -l) jokes downloaded",
    )

    setup_folders >> [download_joke, download_norris_joke] >> notify_number_files


