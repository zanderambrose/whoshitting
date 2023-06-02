server:
	cd api && uvicorn main:app --reload

up:
	docker compose up -d --build --force-recreate;

down:
	docker compose down;

db:
	docker compose exec -it mongo mongosh --username root --password example;
