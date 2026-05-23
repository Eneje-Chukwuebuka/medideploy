.PHONY: help install test lint run clean

help:
	@echo "MediDeploy - Available commands:"
	@echo ""
	@echo "  make install    Install all dependencies"
	@echo "  make test       Run test suite"
	@echo "  make lint       Run code linter"
	@echo "  make run        Start the app locally"
	@echo "  make clean      Remove cache files"

install:
	pip install -r requirements.txt

test:
	python -m pytest tests/ -v

lint:
	flake8 app/ tests/ --max-line-length=88 --ignore=E501

run:
	APP_ENV=dev python -m flask --app app.main run

clean:
	find . -type f -name "*.pyc" -delete
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type d -name ".pytest_cache" -exec rm -rf {} +
