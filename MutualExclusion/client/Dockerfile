FROM python:3.9-slim

ARG ID
ENV ID=$ID

WORKDIR /app

COPY client/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY client/client.py .

ENV PYTHONUNBUFFERED=1

ENV RUNCOMMAND="python3 client.py --id=${ID}"
ENTRYPOINT $RUNCOMMAND
