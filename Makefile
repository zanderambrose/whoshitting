up:
	docker compose up -d --build --force-recreate;

dev:
	docker compose up -d --force-recreate;

down:
	docker compose down;

db:
	docker compose exec -it mongo mongosh --username root --password example ;

exec:
	docker exec -it scraper bash;

server:
	docker exec -it api bash;

server-logs:
	docker logs -f api ;
