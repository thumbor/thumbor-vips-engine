setup:
	@python3 -m pip install -e .[tests]

test: unit flake pylint

unit:
	@python3 -m pytest --cov=thumbor_vips_engine tests/

format:
	@python3 -m black .

flake:
	@python3 -m flake8 --config .flake8

pylint:
	@python3 -m pylint thumbor_vips_engine tests

run:
	@python3 -m thumbor -c thumbor.conf -l debug

publish:
	@python setup.py sdist
	@twine upload dist/*
	@rm -rf dist/

ci-venv:
		@. ~/thumbor-libvips-engine/bin/activate
