echo "SANDBOX_DB_USERNAME = 'postgres' 
SANDBOX_DB_PASSWORD = 'postgres' 
SANDBOX_DB_NAME = 'sandbox' 
SANDBOX_DB_HOST = 'localhost' 
SANDBOX_DB_SCHEMA = 'sandbox'" > secret_store/secret_store.py

echo "SANDBOX_DB_USERNAME=postgres \
SANDBOX_DB_PASSWORD=postgres \
SANDBOX_DB_NAME=sandbox \
SANDBOX_DB_HOST=db \
SANDBOX_DB_SCHEMA=sandbox \
POSTGRES_PASSWORD=postgres" > db/.env

echo "SANDBOX_DB_USERNAME=postgres \
SANDBOX_DB_PASSWORD=postgres \
SANDBOX_DB_NAME=sandbox \
SANDBOX_DB_HOST=localhost \
SANDBOX_DB_SCHEMA=sandbox" > app/.env

docker-compose build
docker-compose up