# Lecture 4 - Airflow intro

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

Here are some good commands to know by heart 

```
airflow dags list 
airflow dags test <dag_name> <execution_date>
airflow tasks test <dag_name> <task_name> <execution_date>
```

---
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

Now we want to choose another image to build, with a specific version of Python, so that we can customize installations. This can be done in a Dockerfile, and specify in docker-compose.yaml to build from this Dockerfile. Docker images for Airflow can be found in [this page](https://airflow.apache.org/docs/docker-stack/index.html).  

Now run this command to initialize airflow

```bash
docker compose up airflow-init
```

Go into [localhost:8080](http://localhost:8080/home) and log into airflow using airflow as username and airflow as password. Note that these can be set in docker-compose.yaml but you should do this with an .env file so that it doesn't get tracked and published in a repository available for others. For now we keep the default as it is.

--- 
## First DAG

Now we will build your first DAG...