run:
	fastapi dev app/main.py

dev-install:
	pip install -r dev-requirements.txt

lint:
	ruff check app tests

format:
	black app tests
	ruff check app tests --fix

