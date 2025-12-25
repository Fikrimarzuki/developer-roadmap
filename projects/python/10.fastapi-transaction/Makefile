run:
	fastapi dev app/main.py

test:
	pytest -q

migrate:
	alembic upgrade head

downgrade:
	alembic downgrade -1

seed:
	python -m app.seed

reset-db:
	rm -f app.db
	alembic upgrade head
	python -m app.seed

dev-install:
	pip install -r dev-requirements.txt

lint:
	ruff check app tests

format:
	black app tests
	ruff check app tests --fix

typecheck:
	mypy app