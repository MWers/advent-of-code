.PHONY: all
all: full

.PHONY: full
full:
	@python main.py input-full.txt

.PHONY: full-debug
full-debug:
	@LOGLEVEL=DEBUG python main.py input-full.txt

.PHONY: sample
sample:
	@python main.py input-sample.txt

.PHONY: sample-debug
sample-debug:
	@LOGLEVEL=DEBUG python main.py input-sample.txt

.PHONY: format
format:
	@autoflake --remove-all-unused-imports --remove-unused-variables --ignore-init-module-imports --recursive --in-place .
	@isort --trailing-comma --multi-line=3 .
	@black --line-length 79 --skip-string-normalization .

.PHONY: lint
lint:
	@flake8 .
	@black --check --diff --line-length 79 --skip-string-normalization  .

.PHONY: type-check
type-check:
	@mypy .

.PHONY: test
test:
	@pytest -s .
