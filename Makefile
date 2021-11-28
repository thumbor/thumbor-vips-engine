setup:
	@pip install -e .[tests]

test: unit coverage flake

unit:
	@pytest --cov=thumbor_vips_engine tests/

format:
	@black .

flake:
	@flake8 --config .flake8

pylint:
	@pylint thumbor_aws tests

run:
	@thumbor -c thumbor.conf -l debug

publish:
	@python setup.py sdist
	@twine upload dist/*
	@rm -rf dist/
