build:
	docker-compose build

run:
	docker-compose run coinbase

test:
	docker-compose run coinbase pytest
