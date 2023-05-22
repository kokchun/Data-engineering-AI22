# Lecture 2 - Docker compose

In this lecture you will learn
- docker compose 
- data persistance
  - named volumes
  - bind mount
- ports mapping in docker compose
- add save file on dash
  
## Some good commands 

<!-- TODO: exercise to write glossary on these terms-->

```
docker compose up -d
docker compose up --build
docker compose down
docker exec -it <container-name> /bin/bash 
docker inspect
docker ps 
docker volume ls 
docker container ls -a
docker image ls -a
docker image prune
docker container prune
```

---

## Under construction

Okay lets start with docker-compose.yaml 

```docker-compose
services:
  python:
    # to install python 3.11 from Dockerhub
    #image: python:3.11
    build: .
    ports:
      - "8050:8050"
    container_name: lecture2
```

and then we need to rewrite the Dockerfile to

```Dockerfile
FROM python:3.11

WORKDIR /app

COPY . . 
RUN pip install -r requirements.txt

EXPOSE 8050

CMD ["python", "./src/main.py"]
```

Lets go in and 


We write our docker comp

Topics to include:
- docker-compose.yaml
- map ports, service, Dockerfile
- docker compose up --build 
- docker compose up
- docker compose down
- docker exec <container-name> /bin/bash <!-- from Ubuntu WSL-->

- download files from dash app go inside of container to look at files
- go out and shut down container, go in again and see that files are removed 

- named volumes
- bind mount

- after fixed volumes we see that the files persists 