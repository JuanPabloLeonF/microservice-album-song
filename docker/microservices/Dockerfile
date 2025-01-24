FROM python:3

WORKDIR microservice-album-song
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY app/ app/
COPY main.py .
COPY .env .

CMD ["python", "main.py"]