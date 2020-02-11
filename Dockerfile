FROM python:3.8.1-alpine3.11

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . ./

CMD ["python", "/app/main.py"]
