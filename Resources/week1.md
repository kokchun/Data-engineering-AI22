
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



### Docker

This is a good introduction, but in the concepts of Docker but the example is in node.js but it is fine, the principles still applies for you. 
- [Docker crash course for absolute beginners - Techworld with Nana (2023)](https://www.youtube.com/watch?v=pg19Z8LL06w)


This is in Python, hands on, but don't cover much theory 
- [Containerize Python applications with Docker - Neuralnine (2022)](https://www.youtube.com/watch?v=0TFWtfFY87U)

This is also in Python and here you will get concepts in Docker volumes, Docker compose and more
- [How to create a great dev environment with Docker - P. Loeber (2023)](https://www.youtube.com/watch?v=0H2miBK_gAk)

---
## Lecture notes :book:


---
## Theory :book:

---
## Exercises :running: