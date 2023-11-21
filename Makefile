
.PHONY: all
all: makemigrations migrate up

run:
	python3 manage.py runserver 0.0.0.0:8000

up: down
	docker compose -f docker-compose-dev.yml up -d

down:
	docker compose -f docker-compose-dev.yml down --remove-orphans

lint:
	set -xe
	isort .
	flake8 apps/

check_lint:
	isort . --check-only
	flake8 apps/ --show-source

test:
	python3 manage.py test apps/ --pattern="test_*.py"

migrate:
	python3 manage.py migrate

makemigrations:
	python3 manage.py makemigrations

createsuperuser:
	python3 manage.py createsuperuser

collectstatic:
	python3 manage.py collectstatic --no-input

shell:
	python3 manage.py shell

clean:
	git clean -Xfd .
