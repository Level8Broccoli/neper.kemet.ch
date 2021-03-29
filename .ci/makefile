UID := $(shell id -u)
GID := $(shell id -u)

docker-backend-run: docker-backend-image
	docker run -v $$PWD:/data -u ${UID}:${GID} backend-check

docker-backend-image: Dockerfile.ci.backend
	docker build -t backend-check -f Dockerfile.ci.backend ..
	touch docker-backend-image

backend-check:
	mypy **/*.py
	bandit **/*.py
	prospector --strictness high **/*.py
	pytest

docker-admin-run: docker-admin-image
	docker run -v $$PWD:/data -u ${UID}:${GID} admin-check

docker-admin-image: Dockerfile.ci.admin
	docker build -t admin-check -f Dockerfile.ci.admin ..
	touch docker-admin-image

admin-install-dependencies: ../admin/package.json
	cd ../admin && yarn install
	touch admin-install-dependencies

admin-check: admin-install-dependencies
	cd ../admin && yarn lint

clean:
	rm -rf docker-backend-image admin-install-dependencies docker-admin-image .mypy_cache
