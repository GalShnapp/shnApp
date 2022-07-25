#!bin/sh
set -e
echo slowly migrating 

cd app/

echo app

cd db_connectors/

echo db_connectors
echo going to sleep 10 seconds
sleep 10 

echo step alembic
alembic upgrade head