
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

- [Python venv with Mac & Linux - C. Shafer (2019)](https://www.youtube.com/watch?v=Kg1Yvry_Ydk)
- [Python venv with Windows - C. Shafer (2019)](https://www.youtube.com/watch?v=APOPm01BVrk)

---
## Lecture notes :book:


---
## Theory :book:

---
## Exercises :running: