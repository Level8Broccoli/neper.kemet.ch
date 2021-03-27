UID := $(shell id -u)
GID := $(shell id -u)

docker-backend-run: docker-backend-image
	docker run -v $$PWD:/data -u ${UID}:${GID} backend-check

docker-backend-image: Dockerfile.ci.backend
	docker build -t backend-check -f Dockerfile.ci.backend .
	touch docker-backend-image

backend-check:
	mypy **/*.py
	bandit **/*.py
	prospector --strictness high **/*.py
	pytest

docker-frontend-run: docker-frontend-image
	docker run -v $$PWD:/data -u ${UID}:${GID} frontend-check

docker-frontend-image: Dockerfile.ci.frontend
	docker build -t frontend-check -f Dockerfile.ci.frontend .
	touch docker-frontend-image

frontend-install-dependencies: ./frontend/package.json
	cd ./frontend && yarn install
	touch frontend-install-dependencies

frontend-check: frontend-install-dependencies
	pwd
	eslint .
