#%%
from airflow.decorators import dag, task_group, task
from datetime import datetime
from include.setup import setup_directories, datalake_path
from include.queue_time.extract import extract_queue_time
from include.queue_time.load import load_datalake

#%%

@dag(dag_id = "queue_time_ELT", start_date=datetime(2023,6,2), schedule="*/5 * * * *", catchup=False)
def queue_time_ELT():
    setup = setup_directories()
    extract_queue_time_ = extract_queue_time()
    load = load_datalake()

    #TODO: ingest real airquality data 
    #TODO: refactor this to be on separate file 
    #TODO: schedule this differnetly somehow to be ingested once per hour
    @task_group(group_id = "airquality_ingestion")
    def airquality_ingestion():
        @task(task_id = "extract")
        def airquality_extract():
            return "temperatur"
        
        @task(task_id = "load") 
        def airquality_load_dummy():
            with open(datalake_path/f"log.txt", "a") as file:
                file.write(f"Temperature ingested {datetime.now()}\n")
        
        airquality_extract() >> airquality_load_dummy()

    setup >> extract_queue_time_ >> load

    setup >> airquality_ingestion()

# register DAG 
queue_time_ELT()


