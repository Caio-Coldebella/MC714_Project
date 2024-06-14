FROM python:3.9-slim

WORKDIR /app

COPY client/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY client/client.py .

ENV PYTHONUNBUFFERED=1

CMD ["python", "./client.py"]
