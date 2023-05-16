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