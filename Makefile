ifeq ($(OS),Windows_NT)
	POETRY=poetry
else
	POETRY=$(shell which poetry)
endif

test: install lint
	$(POETRY) run pytest

lint:
	$(POETRY) run pycodestyle src tests
