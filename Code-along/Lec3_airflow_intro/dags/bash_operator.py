from airflow.operators.bash import BashOperator
from airflow import DAG
from datetime import datetime

print(datetime.now())


with DAG(dag_id = "joke_DAG", start_date=datetime(2023,6,1)):
    say_hello = BashOperator(task_id = "say_hello", bash_command="echo 'hej hej'")

    

    say_hello