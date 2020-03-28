POETRY=$(shell which poetry)

test: install lint
	$(POETRY) run pytest

lint:
	$(POETRY) run pycodestyle src tests
