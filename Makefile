.PHONY: dev down restart postgres redis

dev:
	docker compose -f docker-compose.local.yaml up -d

down:
	docker compose -f docker-compose.local.yaml down

restart: down dev
	@echo restarted

postgres:
	docker exec -ti db psql -U username database_name
