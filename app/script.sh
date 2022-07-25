#!bin/bash
set -e

_wd=$(pwd)
echo slowly migrating 
cd app/db_connectors/


echo step alembic
alembic upgrade head

cd $_wd

uvicorn app.app:app --host 0.0.0.0 --port 80