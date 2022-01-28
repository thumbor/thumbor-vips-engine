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

docker-build:
	@docker build -t thumbor-pyvips-engine .

docker-shell: docker-build
	@docker run --rm -it -v $$(pwd):/app thumbor-pyvips-engine:latest /bin/bash -l

docker-run: docker-build
	@docker run --rm -it -v $$(pwd):/app thumbor-pyvips-engine:latest /bin/bash -l -c "make local-run"

docker-test: docker-build
	@docker run --rm -it -v $$(pwd):/app thumbor-pyvips-engine:latest /bin/bash -l -c "make local-unit"
