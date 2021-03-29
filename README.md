# [neper.kemet.ch](https://neper.kemet.ch)

An auction website for second hand (board) games.

## Naming

Neper is a god of grain in ancient Egyptian mythology.

## Development

### Prerequisites

* Docker
* Visual Studio Code
* Remote - Containers

### Developing container with Visual Studio Code

```
VSC > Remote-Containers: Reopen in Container
```

## CI

### Prerequisites

* Docker
* make

### Start frontend CI

```sh
make docker-frontend-run
```

### Start backend CI

```sh
make docker-backend-run
```

## Deployment

### Prerequisites

* Docker
* Docker Compose

```sh
DOCKER_HOST="ssh://user@host" docker-compose -f docker-compose.prod.yml up -d
```
