FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY lock_manager.py .

ENV PYTHONUNBUFFERED=1

CMD ["python", "lock_manager.py"]
