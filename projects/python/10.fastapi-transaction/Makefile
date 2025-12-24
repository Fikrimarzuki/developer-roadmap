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
