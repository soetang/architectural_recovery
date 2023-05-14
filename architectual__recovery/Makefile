SHELL := /usr/bin/bash

installdeps:
	python3 -m virtualenv .venv
	source .venv/bin/activate
	python3 -m pip install -r ./requirements.txt

installpkg:
	pip install -e . --trusted-host dsl -i http://dsl/repository/pfapython/simple --proxy=""

clean:
	rm -rf .venv

freeze:
	python3 -m pip freeze > requirements.txt

build:
	python3 setup.py bdist_wheel

test:
	PYTHONPATH=. pytest --doctest-modules --junitxml=junit/test-results.xml --cov=src --cov-report=xml
	coverage report --fail-under=95
	
lint:
	pylint src --exit-zero