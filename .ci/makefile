UID := $(shell id -u)
GID := $(shell id -u)
PROJECT_ROOT := $(shell cd .. && pwd)

docker-backend-run: docker-backend-image
	docker run -v ${PROJECT_ROOT}:/data -u ${UID}:${GID} backend-check

docker-backend-image: ${PROJECT_ROOT}/.ci/Dockerfile.ci.backend
	docker build -t backend-check -f ${PROJECT_ROOT}/.ci/Dockerfile.ci.backend ${PROJECT_ROOT}
	touch docker-backend-image

backend-check:
	mypy **/*.py
	bandit **/*.py
	prospector --strictness high **/*.py
	pytest

docker-admin-run: docker-admin-image
	docker run -v ${PROJECT_ROOT}:/data -u ${UID}:${GID} admin-check

docker-admin-image: ${PROJECT_ROOT}/.ci/Dockerfile.ci.admin
	docker build -t admin-check -f ${PROJECT_ROOT}/.ci/Dockerfile.ci.admin ${PROJECT_ROOT}
	touch docker-admin-image

admin-install-dependencies: ${PROJECT_ROOT}/admin/package.json
	cd ${PROJECT_ROOT}/admin && yarn install
	touch admin-install-dependencies

admin-check: admin-install-dependencies
	cd ${PROJECT_ROOT}/admin && yarn lint

clean:
	rm -rf docker-backend-image admin-install-dependencies docker-admin-image .mypy_cache
