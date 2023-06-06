#%%
from airflow.decorators import task_group
from airflow.operators.python import PythonOperator
import requests

# TODO: find a way to not extract all, but filter out in the api call 
def _extract_raw_airquality():
    response = requests.get('https://catalog.goteborg.se/rowstore/dataset/cb541050-487e-4eea-b7b6-640d58f28092?_limit=100&_offset=0')
    if response.status_code == 200: 
        return response.json()[:11] # 0-11 has station Femman 
    
#%%
# once per hour HH:03 
@task_group(group_id="extract_weather")
def extract():
    extract_airquality = PythonOperator(task_id = "extract_airquality", python_callable=_extract_raw_airquality)

    extract_airquality

# %%
