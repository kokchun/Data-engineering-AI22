FROM python:3.11

WORKDIR /app

COPY . . 
RUN pip install -r requirements.txt

EXPOSE 8050

CMD ["python", "./src/main.py"]