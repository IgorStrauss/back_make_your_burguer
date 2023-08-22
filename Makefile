# bin/bash

db:
	docker compose up -d

up:
	python back_myb/manage.py runserver 0.0.0.0:8000

migrate:
	python back_myb/manage.py makemigrations
	python back_myb/manage.py migrate
