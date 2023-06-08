from airflow.operators.bash import BashOperator
from pathlib import Path
from airflow.decorators import task_group

data_path = Path(__file__).parents[1] / "data"
datalake_path = data_path / "data_lake"
data_warehouse_path = data_path / "data_warehouse"


@task_group(group_id="setup_data_directories")
def setup_directories():
    pass


