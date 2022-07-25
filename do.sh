#!/bin/sh

docker-compose kill 

echo "SANDBOX_DB_USERNAME=postgres\n\
SANDBOX_DB_PASSWORD=postgres\n\
SANDBOX_DB_NAME=sandbox\n\
SANDBOX_DB_HOST=db\n\
SANDBOX_DB_SCHEMA=sandbox \n\
POSTGRES_PASSWORD=postgres"  > secret_store/secret_store.py

echo "SANDBOX_DB_USERNAME=postgres\n\
SANDBOX_DB_PASSWORD=postgres\n\
SANDBOX_DB_NAME=sandbox\n\
SANDBOX_DB_HOST=db\n\
SANDBOX_DB_SCHEMA=sandbox \n\
POSTGRES_PASSWORD=postgres"  > db/.env

echo "SANDBOX_DB_USERNAME=postgres\n\
SANDBOX_DB_PASSWORD=postgres\n\
SANDBOX_DB_NAME=sandbox\n\
SANDBOX_DB_HOST=db\n\
SANDBOX_DB_SCHEMA=sandbox \n\
POSTGRES_PASSWORD=postgres" > app/.env

ln -s secret_store/secret_store.py app/app/db_connectors

docker-compose build
docker-compose up 
