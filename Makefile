# Python version can be specified with `$ PYTHON_EXE=python3.x make conf`
PYTHON_EXE?=python3
ACTIVATE?=. bin/activate;
BLACK_ARGS=--exclude="data|docs" .

virtualenv:
	@echo "-> Bootstrap the virtualenv with PYTHON_EXE=${PYTHON_EXE}"
	@${PYTHON_EXE} -m venv .

conf: virtualenv
	@echo "-> Install dependencies"
	@${ACTIVATE} pip install -e .

dev: conf
	@echo "-> Configure and install development dependencies"
	@${ACTIVATE} pip install -r etc/requirements/dev.txt

check:
	# @echo "-> Run pycodestyle (PEP8) validation"
	# @${ACTIVATE} pycodestyle --max-line-length=88 --exclude=lib,thirdparty,docs,bin,migrations,settings,data,pipelines,var .
	@echo "-> Run isort imports ordering validation"
	@${ACTIVATE} isort --check-only src tests
	@echo "-> Run black validation"
	@${ACTIVATE} black --check ${BLACK_ARGS}
	@echo "-> Run doc8 validation"
	@${ACTIVATE} doc8 --max-line-length 100 --ignore-path docs/_build/ --quiet docs/

isort:
	@echo "-> Apply isort changes to ensure proper imports ordering"
	bin/isort src tests

black:
	@echo "-> Apply black code formatter"
	bin/black ${BLACK_ARGS}

valid: isort black

clean:
	@echo "-> Clean the Python env"
	rm -rf bin/ lib/ lib64/ include/ build/ dist/ scancodeio.egg-info/ docs/_build/ pip-selfcheck.json pyvenv.cfg
	find . -type f -name '*.py[co]' -delete -o -type d -name __pycache__ -delete

test:
	@echo "-> Run the test suite"
	@${PYTHON_EXE} -m unittest discover

# package: conf
# 	@echo "-> Create package for offline installation"
# 	@echo "-> Fetch dependencies in thirdparty/ for offline installation"
# 	rm -rf thirdparty && mkdir thirdparty
# 	bin/pip download -r etc/requirements/base.txt --no-cache-dir --dest thirdparty
# 	@echo "-> Create package in dist/ for offline installation"
# 	bin/python setup.py sdist

install: virtualenv
	@echo "-> Install and configure the Python env with base dependencies, offline"
	bin/pip install --upgrade --no-index --no-cache-dir --find-links=thirdparty -e .
