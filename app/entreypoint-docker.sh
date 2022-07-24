#!bin/sh
set -e
echo start 
pwd 
ls -l 
cd app/ 

echo step2 
pwd 
ls -l 
cd app/ 

echo step3 
pwd 
ls -l 
cd db_connectors/

echo "and now we wait ....."
sleep 10 

echo step-alembic  
alembic upgrade head

uvicorn app.app:app --host 0.0.0.0 --port 80