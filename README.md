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

## CI

### Prerequisites

* Docker
* make

### Start admin CI

```sh
make --directory=./.ci ci-admin
```

### Start backend CI

// TODO

## CD

### Prerequisites

* Docker
* Docker Compose

```sh
DOCKER_HOST="ssh://user@host" docker-compose -f ./.cd/docker-compose.prod.yml up -d --build
```
