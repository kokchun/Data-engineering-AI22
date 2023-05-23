FROM python:3.11

# host container
ADD main.py .

RUN pip install plotly_express dash

EXPOSE 8050

CMD ["python", "./main.py"]