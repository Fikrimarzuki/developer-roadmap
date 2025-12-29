init-db:
	@echo "Initializing database..."
	@python -m app.scripts.init_db

migrate:
	@echo "Running Alembic migrations..."
	@alembic upgrade head

setup-db: init-db migrate

test:
	pytest -q

downgrade:
	alembic downgrade -1

seed:
	python -m app.seed

dev-install:
	pip install -r dev-requirements.txt

run:
	fastapi dev app/main.py

lint:
	ruff check app tests

format:
	black app tests
	ruff check app tests --fix

typecheck:
	mypy app

