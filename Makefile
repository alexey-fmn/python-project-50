lint:
	ruff check .

install:
	uv sync

test:
	pytest