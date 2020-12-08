.PHONY: all
all:
	@python main.py input-full.txt

.PHONY: sample
sample:
	@python main.py input-sample.txt

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
