# Lecture 5 - ELT pipeline with Airflow 

- note that this lecture is not finished yet

In this lecture we build an ELT pipeline using Airflows TaskFlow API, which is a newer way of writing Airflow DAGs using decorators. This makes developing workflows more pythonic than the traditional way. Note that a lot of documentation still uses the traditional way. We will also cover the following concepts

- schedule data extraction 
- XComs using TaskFlow API 
- structuring the DAG using TaskGroups 
- structuring a data pipeline code 

Here are some parts that will be covered in week 34, that isn't finished yet

- fix scheduling so that it follows Lisebergs opening hours
- setup a Postgres database and connect it for datalake storage
- ingest airquality data 
- scheduling strategy for ingesting airquality data once per hour while waiting time data once per five minutes
- serve a Plotly dashboard to display current waiting time, and historical waiting time for different attractions
- connect a machine learning task to predict waiting time for different attractions
- show the results from this prediction in the dashboard

This part will require a refactoring of the code so it will be in Lec6 instead. 





