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

## Docker compose

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

Lets now go into the container and check it out, navigate around. Also lets inspect the container. 

---
## Data persistance

Now we implement a save button on our dash app and try saving files. Try and see that it works locally. 

Now we spin up a container and save file, go into the container to see that it works, which is very coool. Now we shut down the container and spins it up again and with tears in our eyes see that the data has not persisted. 

So we will test out and implement bind mounts and named volumes. 

--- 
### Bind mounts
Bind mounts are direct mapping of the host directory to a container, which means we mount a directory or file from host to the container. All changes are reflected directly and visible to both host and container. Bind mount is good for development, but not good when it comes to portability and sharing data between containers.

### Named volumes
Named volumes on the other hand is good for portability and can share between containers. Data is persisted as in bind mounts, but here it can be accessed by several services. The named volume is managed by docker independently and thus the storage location on the host is not exposed. 