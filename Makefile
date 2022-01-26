setup:
	@pip install -e .[tests]

test: unit flake pylint

unit:
	@pytest --cov=thumbor_vips_engine tests/

format:
	@black .

flake:
	@flake8 --config .flake8

pylint:
	@pylint thumbor_vips_engine tests

run:
	@thumbor -c thumbor.conf -l debug

publish:
	@python setup.py sdist
	@twine upload dist/*
	@rm -rf dist/

ci-libvips:
		@echo "Setting up libvips..."
		@wget https://github.com/libvips/libvips/releases/download/v8.12.2/vips-8.12.2.tar.gz
		@tar xzf vips-8.12.2.tar.gz
		@cd vips-8.12.2
