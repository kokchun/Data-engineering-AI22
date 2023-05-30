# Lecture 1 - Docker

In this lecture you'll learn the basics of Docker and containerize a Python application. We will work extensively with command line tools (CLI) so make sure to learn the commands and don't just ChatGPT all the time.

Follow instructions in resources to install docker on your machine.

---

## Warmup settings
It's good for us to build our virtualenvironment before dockerizing Python apps, so we use 

```bash
python -m venv venv
```

Okay so before we dockerize an app we actually surprise surprise need an app. So lets create a dash app that simulates dices, I know not so original but it will be fun :)


## Creating a Python docker container

Okay so you want to create a container. Questions that arise could be what are the dimensions? Colors? Materials? ...

Fine, we need some instructions then so that we can **build** an **image** of how the container should look like. From this image we can then **spin** up as many containers as we want from this image, and they will have the same configurations. We'll write the specifications in a Dockerfile.

```bash
touch Dockerfile
```

Now lets use Python 3.11 as a base image, and create a file called main.py with a short print statement inside.

```Dockerfile
# gets python3.11 image from Dockerhub with their configurations, so we don't have to manually install Python3.11 as we do in our own machine
FROM python:3.11

# adds main.py into . (dot) which means this folder inside the container
# where is this folder, you might ask - we'll inspect it later
ADD main.py .

# run these commands when the docker container is run
CMD ["python", "./main.py"]
```

Building time

```bash
# builds the image with repository name lec1-docker and tag latest
# can choose to tag it something else using : e.g. lec1-docker:v1
docker build -t lec1-image .

# check the image
docker image ls

# if you have many images use to search for it
docker image ls | grep lec1
```

Woah that was fast and efficient, time to spin up our container, an analogy to OOP is that image is a class and container is an instance of that class. Spin spin spin ...

```bash
# spins up a container by name lec1-container using lec1 as image
docker run --name lec1-container lec1-image
```

Isn't that supercool, we see our Python program is running with the supercool printing message that we added into our script. We start by listing our container

```bash
# probably we don't see any containers, as ours have closed
docker container ls

# now this lists all containers, including closed ones
# also pipe with grep if you have many containers and need to find a particular one
docker container ls -a
```

Cool, that we ran the container, but let's dive deeper to find out what the container is and what it contains (höhö)

```bash
# -it flag for interactive mode, /bin/bash opens up a bash shell inside the container
docker run -it lec1-image /bin/bash
```

Imagine you have come into a new world that was isolated from your current world, but you could before just see the surface. Now you have found the key to unlock its secrets, so dig in and explore

```bash
whoami # root
date
echo "My OS is: $OSTYPE"
pwd # /
ls -al
which python
ls | grep main # seems like our script got copied to the root
cat main.py
python main.py
mkdir cool_src_code
mv main.py cool_src_code
```

So we can run a python shell inside the container

```py
import sys
sys.version # 3.11.3 (main, May  4 2023, 05:53:32) [GCC 10.2.1 20210110]

from datetime import datetime
datetime.now() # another time zone

import plotly_express # oh crap it doesn't exist, hmm ...

quit() # or ctrl+D to get out
```

Now we shut down our container by ctrl+D, we can check that our container is closed

```bash
docker container ls -a

# note that this spins up a new container from the same image
docker run -it --name lec1_container2 lec1_image /bin/bash

# we see that the changes we made is not here as this is a new fresh container
ls
```

Okay jump out with ctrl+D and inspect our containers created

```bash
# ah there are two containers
docker container ls -a | grep lec1
```

Now start up the first container and see if the changes we made are there

```bash
# this prints out our original messsage, so apparently it didn't persist after shutdown
docker start -i lec1-container
```

---

## Clean up containers and images

Lets reset and remove all containers and images that are not running

```bash
docker container prune && docker image prune
docker image ls
docker container ls -a
```

---

## Install python packages

We noticed before that plotly_express didn't exist in our python, so we modify Dockerfile to install it when spinning up the container

```Dockerfile
FROM python:3.11
ADD main.py .
# new line
RUN pip install plotly_express
CMD ["python", "./main.py"]
```

So we need to build another image and spin up a container from it

```bash
docker build -t lec1-image:v2 .
docker run -it --name lec1-container3 lec1-image:v2 /bin/bash
pip list # and we can see it there
pip list | grep plotly # if you are lazy to read through all packages
```

Okay but there is a bunch of packages I want to install, say I want to run a dash application now. Let's install them to our venv from outside of the container first. This is to simplify development outside of a container. To get the same packages with same version as those in venv we create a requirements.txt with the packages that we want:

```bash
# view packages of plotly, dash and numpy
# however this approach don't have == between package and version
pip list | grep "plotly\|dash\|numpy"

# use pip freeze instead
pip freeze | grep "plotly\|dash\|numpy"

# now use output redirection to requirements.txt file
pip freeze | grep "plotly\|dash\|numpy"  > requirements.txt

cat requirements.txt
```

We fresh up our skills in plotly dash and build a [dice simulator app](https://github.com/kokchun/Data-engineering-AI22/blob/main/Lecture-code/Lec1-docker/main.py).

Okay to make this work in Docker we modify the Dockerfile

```Dockerfile
FROM python:3.11
# changes current working directory to /app
WORKDIR /app

# copies all files in this directory to the current working directory in container
COPY . .

# informs Docker that container listens to this port at runtime
EXPOSE 8081

# installs from the requirements
RUN pip install -r requirements.txt
CMD ["python", "./main.py"]
```

Build the image and spin up a container

```bash
docker build -t lec1-image:v3 .
docker run lec1-image:v3 --name dice-app
```

Oh cool the dash app is running on the container, but when we navigate ourself to localhost port 8081 [http://localhost:8081/](http://localhost:8081/), we see a failure. The port is exposed to the docker container but it isn't published to the host machine.

```bash
# publishes port 8081 from the container to the host machine
docker run -p 8081:8081 --name dice-app lec1-image:v3
```

Wupp wupp we have dockerized our dice app, the app itself is very ugly but the dockerization worked.
