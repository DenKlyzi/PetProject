.DEFAULT_GOAL := start

start:
	docker compose -f docker-compose.yml --project-name petproject up

rebuild:
	docker compose -f docker-compose.yml --project-name petproject up --build

stop:
	docker compose -f docker-compose.yml --project-name petproject down --remove-orphans

.PHONY: start rebuild stop
