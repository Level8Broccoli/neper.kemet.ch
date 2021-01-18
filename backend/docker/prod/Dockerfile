FROM tiangolo/uvicorn-gunicorn:python3.8

ENV WORKDIR=/usr/src/app
ENV USER=app

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE=1

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED=1

RUN mkdir $WORKDIR
WORKDIR $WORKDIR

# Install pip requirements
RUN pip install --upgrade pip
COPY . .
RUN python -m pip install -r requirements.txt

# Run all tests
# RUN pytest

# Switching to a non-root user, please refer to https://aka.ms/vscode-docker-python-user-rights
# RUN adduser --system --group $USER
# RUN chown -R $USER:$USER $WORKDIR
# USER $USER
