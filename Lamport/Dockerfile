# Use an official Python runtime as a parent image
FROM python:3.9-slim

ARG ADDRESS
ARG FREQUENCY
ENV ADDR=$ADDRESS
ENV FREQ=$FREQUENCY
# Set the working directory
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE $ADDR

ENV RUNCOMMAND="python3 server.py --address=${ADDR} --frequency=${FREQ}"
ENTRYPOINT $RUNCOMMAND