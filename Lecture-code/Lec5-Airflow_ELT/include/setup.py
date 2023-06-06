#%%
from pathlib import Path
from airflow.decorators import task_group
from airflow.operators.bash import BashOperator

data_path = Path(__file__).parents[1] / "data" 
datalake_path = data_path / "data_lake"
data_warehouse_path = data_path / "data_warehouse"


print(data_path)

@task_group(group_id="setup_data_directories")
def setup_directories():

    setup_directories = BashOperator(
        task_id="setup_directories",
        bash_command=f"mkdir -p {datalake_path} {data_warehouse_path}",
    )

    successful_setup = BashOperator(task_id = "setup_success", bash_command="echo 'setup data directories successful'")

    setup_directories >> successful_setup
