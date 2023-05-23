
# Week 21 - Resources

[:house: Main page](https://github.com/kokchun/Data-engineering-AI22)

---
## Setup :wrench:

For this week we will setup Python venv, linux bash with WSL (windows) and docker. 


<details open>

<summary><b>Python venv setup</b></summary>

In this course we'll use Python venv as virtualenvironment instead of pip. This is to both learn another virtualenvironment tool that is common and also pipenv that we've used before has some problems with locking certain versions of packages and some dependency problems. 

1. Create a new repository on Github for this course and clone your repository to your local machine

2. Install venv using pip to your machine.

3. Create the virtual environment with python 3.9

```bash
python3.9 -m venv <your_venv_name>
```

4. Now activate your venv: 

For **windows** use this command: 

```bash
<your_venv_name>\Scripts\activate 
```

For **mac** or **linux**

```bash
source <your_venv_name>/bin/activate
```

Test your environment with the commands 

```bash
pip list 
which python
python
```

</details>

<details open>

<summary><b>Windows for subsystem (WSL) setup</b></summary>

You can read the documentation for installing WSL here 
- [WSL documentation - microsoft learn (2023)](https://learn.microsoft.com/en-us/windows/wsl/install)
- [WSL install if not working](https://www.omgubuntu.co.uk/how-to-install-wsl2-on-windows-10)
- If this doesn't work you can use microsoft store and install wsl and ubuntu latest version.

or simply put, go into powershell and type 

```powershell
wsl --install
```

This will install ubuntu for you in windows, which you can open directly from windows start menu. 

</details>


<details open> 

<summary><b>Docker engine setup</b></summary>

Go into this link to download and install Docker engine for your OS. 
- [Install Docker engine - Docker docs](https://docs.docker.com/engine/install/)

</details>


---   
## Video guides :video_camera:

The video guides are divided into setup, Linux bash and Docker 

### Setup
- [Python venv with Mac & Linux - C. Shafer (2019)](https://www.youtube.com/watch?v=Kg1Yvry_Ydk)
- [Python venv with Windows - C. Shafer (2019)](https://www.youtube.com/watch?v=APOPm01BVrk)
- [Install WSL on windows 10 - DevOps How-Tos (2023)](https://www.youtube.com/watch?v=VkJHRpgJxMY)
- [Docker installation on Windows 10 - Simplilearn (2021)](https://www.youtube.com/watch?v=5nX8U8Fz5S0)

### Linux bash

- [60 Linux Commands you NEED to know (in 10 minutes) - NetworkChuck (2022)](https://www.youtube.com/watch?v=gd7BXuUQ91w)


Bash Scripting on Linux (The Complete Guide) - Learn Linux TV (2022)
- [Hello World](https://www.youtube.com/watch?v=boqC9QenshY&list=PLT98CRl2KxKGj-VKtApD8-zCqSaN2mD4w&index=2)
- [Variables](https://www.youtube.com/watch?v=uQE_4Q-HZZw&list=PLT98CRl2KxKGj-VKtApD8-zCqSaN2mD4w&index=3)
- [While loop](https://www.youtube.com/watch?v=R0tTsdQ_9Vw&list=PLT98CRl2KxKGj-VKtApD8-zCqSaN2mD4w&index=7)
- [For loop](https://www.youtube.com/watch?v=HvzI7c3eK5k&list=PLT98CRl2KxKGj-VKtApD8-zCqSaN2mD4w&index=9)

Cron job 
- [Schedule Python with Cron Job - Tony Teaches Tech (2021)](https://www.youtube.com/watch?v=EgrpfvBc7ks)

### Docker

This is a good introduction, but in the concepts of Docker but the example is in node.js but it is fine, the principles still applies for you. 
- [Docker crash course for absolute beginners - Techworld with Nana (2023)](https://www.youtube.com/watch?v=pg19Z8LL06w)


This is in Python, hands on, but don't cover much theory 
- [Containerize Python applications with Docker - Neuralnine (2022)](https://www.youtube.com/watch?v=0TFWtfFY87U)

This is also in Python and here you will get concepts in Docker volumes, Docker compose and more
- [How to create a great dev environment with Docker - P. Loeber (2023)](https://www.youtube.com/watch?v=0H2miBK_gAk)

---
## Lecture notes :book:

- [Lecture 0 - Bash commands](https://github.com/kokchun/Data-engineering-AI22/blob/main/Lecture-code/Lec0-bash/README.md)
- [Lecture 1 - Docker](https://github.com/kokchun/Data-engineering-AI22/tree/main/Lecture-code/Lec1-docker)
- [Lecture 2 - Docker compose](https://github.com/kokchun/Data-engineering-AI22/tree/main/Lecture-code/Lec2-docker_compose)

---
## Theory :book:

Data engineer role
- [What is a Data Engineer - coursera (2023)](https://www.coursera.org/articles/what-does-a-data-engineer-do-and-how-do-i-become-one)
- [Data engineer roles and responsibility - simplilearn (2023)](https://www.simplilearn.com/data-engineer-role-article)

Data engineering concepts
- [Data engineering - wikipedia](https://en.wikipedia.org/wiki/Data_engineering)
- [Extract Transform Load (ETL) - wikipedia](https://en.wikipedia.org/wiki/Extract,_transform,_load)
- [Concept drift - wikipedia](https://en.wikipedia.org/wiki/Concept_drift)
- [Pipeline - wikipedia](https://en.wikipedia.org/wiki/Pipeline_(computing))
- [Data engineering lifecycle - The operator cencus blog (2022)](https://www.getcensus.com/blog/how-understanding-the-data-engineering-lifecycle-helps-us-all-work-better-with-data-engineers)


Linux
- [Linux - wikipedia](https://sv.wikipedia.org/wiki/Linux)
- [Bash programming - w3schools.io](https://www.w3schools.io/terminal/bash-tutorials/)
- [What is command line interface (CLI) - w3schools](https://www.w3schools.com/whatis/whatis_cli.asp)

Docker
- [Docker - wikipedia](https://en.wikipedia.org/wiki/Docker_(software))
- [Build Python image - Docker docs](https://docs.docker.com/language/python/build-images/)
- [Docker hub](https://hub.docker.com/_/python)
- [Docker compose - Docker docs](https://docs.docker.com/compose/gettingstarted/)
- [Manage data in Docker - Docker docs](https://docs.docker.com/storage/)
- [Volumes - Docker docs](https://docs.docker.com/storage/volumes/)
- [Bind mounts - Docker docs](https://docs.docker.com/storage/bind-mounts/)

---
## Exercises :running:

- [Exercise 0 - Bash commands](https://github.com/kokchun/Data-engineering-AI22/blob/main/Exercises/Exercise0-Bash_commands.md)
- [Exercise 1- Docker](https://github.com/kokchun/Data-engineering-AI22/blob/main/Exercises/Exercise1-docker.md)
- [Exercise 2 - Docker compose](https://github.com/kokchun/Data-engineering-AI22/blob/main/Exercises/Exercise2-docker-compose.md)
