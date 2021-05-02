-include ./User.mk
-include ../User.mk
-include ~/User.mk

.PHONY: all
all:test

.PHONY: test
test:
	pytest

cover:
	pytest --cov=gameoflife tests/

.PHONY: build
build:
	poetry install

.PHONY: run
run:
	echo 'not implemented'

.PHONY: clean
clean:
	echo 'not implemented'

