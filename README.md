# [neper.kemet.ch](https://neper.kemet.ch)

An auction website for second hand (board) games.

## Naming

Neper is a god of grain in ancient Egyptian mythology.

## Development

### Prerequisites

* Docker
* Visual Studio Code
  * Remote - Containers

### Development container

Visual Studio Code `> Remote-Containers: Reopen in Container`

## CI [![CI](https://github.com/Level8Broccoli/neper.kemet.ch/actions/workflows/ci.yml/badge.svg)](https://github.com/Level8Broccoli/neper.kemet.ch/actions/workflows/ci.yml)

### Prerequisites

* Docker
* make

### Start admin CI

```sh
make --directory=./.ci ci-admin
```

### Start backend CI

// TODO

## CD [![CD](https://github.com/Level8Broccoli/neper.kemet.ch/actions/workflows/cd.yml/badge.svg)](https://github.com/Level8Broccoli/neper.kemet.ch/actions/workflows/cd.yml)

### Prerequisites

* Docker
* Docker Compose

```sh
DOCKER_HOST="ssh://user@host" docker-compose -f ./.cd/docker-compose.prod.yml up -d --build
```
