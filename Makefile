install:
	uv sync

lint:
	uv run ruff check

test:
	uv run pytest -v

test-coverage:
	uv run pytest --cov=csv_processing --cov-report xml