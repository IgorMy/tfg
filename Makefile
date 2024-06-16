dev:
	uvicorn src.app:app --reload --host 0.0.0.0 --port 8000
start:
	uvicorn src.app:app --host 0.0.0.0 --port 8000
docker:
	docker compose up -d --force-recreate