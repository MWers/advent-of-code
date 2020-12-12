.PHONY: all
all: full

.PHONY: full
full:
	@python main.py input-full.txt

.PHONY: full-debug
full-debug:
	@python main.py --debug input-full.txt

.PHONY: sample
sample:
	@python main.py input-sample.txt

.PHONY: sample-debug
sample-debug:
	@python main.py --debug input-sample.txt

.PHONY: format
format:
	@black .

.PHONY: lint
lint:
	@black --check .

.PHONY: type-check
type-check:
	@mypy .

.PHONY: test
test:
	@pytest .
