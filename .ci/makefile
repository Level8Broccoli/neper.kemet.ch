# admin

UID := $(shell id -u)
GID := $(shell id -u)

ci-admin:
	docker build -t admin-ci -f Dockerfile.ci.admin ..
	docker run -u ${UID}:${GID} admin-ci admin-ci
