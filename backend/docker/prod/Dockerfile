FROM tiangolo/uvicorn-gunicorn:python3.8

ENV WORKDIR=/usr/src/app
ENV USER=app

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE=1

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED=1

RUN mkdir $WORKDIR
WORKDIR $WORKDIR

# Install pip requirements and general setup
COPY . .
RUN chmod +x ./setup.sh && ./setup.sh

# Run all tests
RUN python -m pytest

# Switching to a non-root user, please refer to https://aka.ms/vscode-docker-python-user-rights
RUN adduser --system --group $USER
RUN chown -R $USER:$USER $WORKDIR
USER $USER
