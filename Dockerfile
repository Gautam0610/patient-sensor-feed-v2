FROM python:3.9

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY producer ./producer
COPY app ./app

CMD ["python", "app/app.py"]