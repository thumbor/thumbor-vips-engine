DOCKER_IMAGE=thumbororg/docker-pyvips-engine
PYTHON_VERSION?=3.10

setup:
	@python3 -m pip install -e .[tests]

test: docker-test flake pylint

run: docker-run

local-test: local-unit flake pylint

local-unit:
	@python3 -m pytest --cov=thumbor_vips_engine tests/

format:
	@python3 -m black .

flake:
	@python3 -m flake8 --config .flake8

pylint:
	@python3 -m pylint thumbor_vips_engine tests

local-run:
	@thumbor -c thumbor.conf -l debug

publish:
	@python setup.py sdist
	@twine upload dist/*
	@rm -rf dist/

ci-venv:
	@. ~/pyvips/bin/activate

docker-build:
	@docker build -t ${DOCKER_IMAGE}:latest --build-arg PYTHON_VERSION=${PYTHON_VERSION} .

docker-shell: docker-build
	@docker run --rm -it -v $$(pwd):/app ${DOCKER_IMAGE}:latest /bin/bash -l

docker-run: docker-build
	@docker run --rm -v $$(pwd):/app ${DOCKER_IMAGE}:latest /bin/bash -l -c "make local-run"

docker-test: docker-build docker-unit

docker-test-coverage: docker-build docker-unit-with-coverage

docker-unit:
	@docker run --rm -v $$(pwd):/app ${DOCKER_IMAGE}:latest /bin/bash -l -c "make local-unit"

docker-unit-with-coverage:
	@docker run --rm -v $$(pwd):/app ${DOCKER_IMAGE}:latest /bin/bash -l -c "COVERALLS_REPO_TOKEN=${COVERALLS_REPO_TOKEN} make local-unit coveralls"

coveralls:
	@pip install --upgrade coveralls
	@coveralls --service=github

docker-lint:
	@docker run --rm -v $$(pwd):/app ${DOCKER_IMAGE}:latest /bin/bash -l -c "make flake pylint"

docker-push:
	@docker push ${DOCKER_IMAGE}:latest
