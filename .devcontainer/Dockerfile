FROM alpine:3

ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

RUN apk add --update --no-cache\
  git\
  python3\
  && python3 -m ensurepip\
  && ln -sf python3 /usr/bin/python\
  && ln -sf pip3 /usr/bin/pip
