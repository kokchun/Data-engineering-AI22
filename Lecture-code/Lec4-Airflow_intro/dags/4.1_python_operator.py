#%%
from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.bash import BashOperator
from datetime import datetime
import numpy as np 
from pathlib import Path
 
simulation_data_path = Path(__file__).parents[1] / "data" /"dice_simulations"


#%%

# https://betterdatascience.com/apache-airflow-xcoms/

def _dice_rolls(number_rolls):
    return list(np.random.randint(1,7, size = number_rolls))

def _save_dice_experiment(task_instance):
    simulation_data = task_instance.xcom_pull(task_ids = ["dice_roll"])

    if not simulation_data:
        raise ValueError("No value stored in XComs")
    
    with open(simulation_data_path / "dice_rolls.txt", "a") as file:
        file.write(f"Dice rolls {datetime.now()} \n")
        file.write(f"{simulation_data}\n\n")


with DAG(dag_id="dice_simulator", start_date=datetime(2023,5,1), schedule = "0 8 * * *",catchup= True):
    
    # XComs lets tasks talk to each other

    # uses XComs to move data to a task that writes data to a txt file

    setup_directories = BashOperator(task_id = "setup_directories", bash_command = f"mkdir -p {simulation_data_path.as_posix()}")

    dice_roll = PythonOperator(task_id = "dice_roll", do_xcom_push = True, python_callable = _dice_rolls, op_args=[10])

    save_dice_experiment = PythonOperator(task_id = "save_dice", python_callable=_save_dice_experiment) 

    setup_directories >> dice_roll >> save_dice_experiment
