from airflow.operators.bash import BashOperator
from airflow import DAG
from datetime import datetime
from pathlib import Path
from dotenv import load_dotenv
import os 

load_dotenv()

API_NINJA_KEY = os.environ.get("API_NINJA")

print(API_NINJA_KEY)

data_lake_path = Path(__file__).parents[1] / "data" /"datalake"

data_warehouse_path = Path(__file__).parents[1] /"data"/"data_warehouse"

print(data_lake_path)

time_variable = "$(date +%y%m%d_%H%M%S)"


with DAG(dag_id = "joke_DAG", start_date=datetime(2023,6,1)):
    say_hello = BashOperator(task_id = "say_hello", bash_command="echo 'hej hej joking time'")

    setup_folders = BashOperator(task_id = "setup_folders", bash_command=f"mkdir -p {data_lake_path} {data_warehouse_path}")

    download_joke = BashOperator(task_id="random_joke", bash_command=f"curl -o {data_lake_path}/joke_{time_variable}.json https://official-joke-api.appspot.com/random_joke" )    

    download_norris_joke = BashOperator(
        task_id = "chuck_norris_joke",
        bash_command=f"curl -H 'X-Api-Key: {API_NINJA_KEY}' -o {data_lake_path}/norris_{time_variable}.json https://api.api-ninjas.com/v1/chucknorris"
    )

    notify_number_files = BashOperator(
        task_id = "notify_number_files",
        bash_command=f"echo $(ls {data_lake_path} | wc -l) jokes downloaded"
    )

    say_hello >> setup_folders >> download_joke >> download_norris_joke >> notify_number_files