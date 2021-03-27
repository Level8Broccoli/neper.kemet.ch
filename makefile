UID := $(shell id -u)
GID := $(shell id -u)

docker-backend-run: docker-backend-image
	docker run -v ./:/data -u ${UID}:${GID} backend-check

docker-backend-image: Dockerfile.ci.backend
	docker build -t backend-check -f Dockerfile.ci.backend .
	touch docker-backend-image

backend-check:
	mypy **/*.py
	bandit **/*.py
	prospector --strictness high **/*.py
	pytest

frontend-check:
	eslint .
