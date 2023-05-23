# Exercise 2 - Docker compose

In this exercise you will familiarize yourself with docker compose.

## 0. Warmup (*)

a) Here are some good commands related to docker compose that is good to know. Make a glossary on these commands and learn them by heart.

- docker compose up -d
- docker compose up --build
- docker compose down
- docker exec -it <container-name> /bin/bash 
- docker inspect
- docker ps 
- docker volume ls 
- docker container ls -a
- docker image ls -a
- docker image prune
- docker container prune

b) List out other common docker commands that we have used and add them to your glossary.

c) In later exercises and/or on lecture you will have docker containers that you can inspect. Also see if you can filter out only the volume part.

--- 

## 1. Pokemon lists (*)


a) Create a docker compose with python version 3.11 and bind mount your src folder into the docker container.

b) Create a Python script to scrape this [pokemon list](https://sv.wikipedia.org/wiki/Lista_%C3%B6ver_Pok%C3%A9mon). 

c) Remove the japanese name from it and save it as a csv file, in a data directory.

d) Run this code from your docker container and check that it's correctly mapped to your host system so that the file is saved in your host system as well.

e) Now scrape list of [pokemon species names by generation](https://en.wikipedia.org/wiki/List_of_Pok%C3%A9mon) and use information from here to divide pokemon list into different generations. Save these files into data/generations

```
generation1.csv
generation2.csv
...
generation9.csv
```

---
## 2. Pokeiness continue (*)

Now we will continue with your pokeiness app in exercise 1. 

a) Start with refactoring to use docker compose instead of docker run. 

b) Now implement a named volume

c) Implement a save button to save down an experiment with the pokemon happiness. This should save a csv file to an adequate location in your container.

d) Now close down your container and spin it up again and check if your data has persisted.

