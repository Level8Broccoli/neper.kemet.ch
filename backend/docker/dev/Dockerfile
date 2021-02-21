FROM tiangolo/uvicorn-gunicorn:python3.8

ENV WORKDIR=/usr/src/app
ENV USER=app
ENV PORT=8080
ENV VARIABLE_NAME=app

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE=1

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED=1

# Setup workdir
RUN mkdir $WORKDIR
WORKDIR $WORKDIR

# Install pip requirements and general setup
COPY . .
RUN chmod +x ./setup.sh && ./setup.sh
