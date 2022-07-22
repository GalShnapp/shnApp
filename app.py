from fastapi import FastAPI
from db.model import Parent, Child
from db.engine import get_sandbox_db_session

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}
