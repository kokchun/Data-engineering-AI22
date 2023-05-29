# Exercise 4 - Airflow

This is your first introduction to Airflow, so it is important to understand the tool well.

---

## 0. Warmup

a) Do similar setup as in the lecture, you can reference the [lecture note](https://github.com/kokchun/Data-engineering-AI22/tree/main/Lecture-code/Lec4-Airflow_intro) and/or the video lecture (only available for those officially taking the course).

b) Try to briefly understand the docker-compose.yaml file, at least in a higher conceptual level. Document your findings.

c) What is the path to your working directory inside the scheduler container?

d) We made a bind mount for the data folder in the lecture. Instead of a bind mount rewrite it to be a named volume.

e) Familiarize yourself with Airflow UI and document your findings.

---

## 1. Trigger rule

a) Refactor the lecture code download_joke and download_norris_joke in a way to crash when not getting a successful response from the APIs. Make it fail and test the task manually.

b) Create a new task that prints out success when at least one of the download_joke and download_norris_joke succeeded. Make one of the task fail and run the dag to see the result. Now make both tasks fail and run the dag to see it fail. 

---
## 2. Data warehouse

a) Use the Pythonoperator to write a csv-file with all the jokes, it should include these columns
- date and time of joke download 
- joke_type, give Chuck Norris its own type
- concatenate setup and punchline into the header joke
- joke_id, create an id system for Chuck Norris id

It should be saved under data_warehouse directory. 

b) Schedule to run this DAG every 5 minutes a time of your choice. Make it stop after one hour. 

---
## 3 Dashboard

a) Create a dashboard to display the data from the data warehouse. You can use DataTable in dash.

b) Make a filter to filter out high quality jokes (i.e. Chuck Norris jokes :D)

c) Make the dashboard run in a container and map the ports so that you can access the dashboard from the host.

d) Implement a save button to download the filtered data as a csv file. Save this to your data warehouse in a directory called exports. Make a timestamp for each saved csv file. 

---

## 4. Email (\*\*)

Implement a task to send an email notification with a nice message when all tasks finishes. 

---

X. Glossary

a) Terminology

| Terminology       | Meaning |
| ----------------- | ------- |
| DAG               |         |
| DAG run           |         |
| task              |         |
| task instance     |         |
| operator          |         |
| scheduler         |         |
| sensor            |         |
| triggerer         |         |
| executor          |         |
| worker            |         |
| metadata database |         |
| redis             |         |
| trigger rules     |         |

b) Commands

| Command                                                    | Meaning |
| ---------------------------------------------------------- | ------- |
| docker exec -it <scheduler_container> /bin/bash            |         |
| airflow dags list                                          |         |
| airflow dags test <dag_name> <execution_date>              |         |
| airflow tasks test <dag_name> <task_name> <execution_date> |         |
