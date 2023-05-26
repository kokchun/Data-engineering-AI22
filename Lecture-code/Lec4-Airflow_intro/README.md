# Airflow intro

Here are some Airflow glossary that could be good to check up:

- DAG
- DAG run
- task
- task instance
- operator
- sensor
- scheduler
- triggerer
- worker
- executor
- metadata database
- redis


## Setup

Go into this link and follow the instructions to download the docker-compose.yaml
- [Airflow in Docker](https://airflow.apache.org/docs/apache-airflow/stable/howto/docker-compose/index.html)

After you've fetched docker-compose.yaml we clean up the file to get a lightweight version, do the following:

- remove the part related to flower
- remove redis service as it is a caching server nessary for Celery backend
- change CeleryExecutor to LocalExecutor, which is single-node and instead of multi-node
- remove airflow-triggerer 
- remove airflow-workers

The instructions and motivations behind these are described in this [blog post](https://datatalks.club/blog/how-to-setup-lightweight-local-version-for-airflow.html). 