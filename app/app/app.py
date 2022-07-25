from copy import deepcopy
from sqlalchemy.orm import Session
import logging
import uvicorn
from fastapi import Depends, FastAPI, HTTPException
from app.db_connectors.model import Parent, Child, Association

from app.db_connectors.engine import get_sandbox_db_transaction
from logging.config import dictConfig
import logging
from app.logconfig import LogConfig
from app.crud import get_associations_of_parent

app = FastAPI()

dictConfig(LogConfig().dict())
logger = logging.getLogger("mycoolapp")


def get_db():
    with get_sandbox_db_transaction() as db: 
        yield db

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/get_children_ids/{parent_id}")
async def get_children_ids(parent_id: int, db: Session = Depends(get_db)):
    return {"new": [a.right_id for a in get_associations_of_parent(db=db, parent_id=parent_id)]}

@app.get("/get_parent_id/{child_id}")
async def get_parent_id(child_id: int):
    return {"message": f"Hello Child {child_id}, your parent will be right here!"}

@app.post("/new_parent")
async def create_new_parent():
    p = Parent()
    with get_sandbox_db_transaction() as transaction:
        transaction.add(p)
        transaction.commit()
        pid = p.id
    return {"message": f"Hello new parent. Your parent id is {pid}"}

@app.post("/new_parent_with_child")
async def create_new_parent_with_child():
    p = Parent()
    a = Association(extra_data="some data")
    a.child = Child()
    p.children.append(a)
    pid = 0
    with get_sandbox_db_transaction() as transaction:
        transaction.add(p)
        transaction.commit()
        pid = p.id
    return {"message": f"Hello new parent. Your parent id is {pid}"}

@app.post("/new_child_for_parent/{parrent_id}")
async def create_new_child_for_parent(parrent_id: int):
    cid = 0
    with get_sandbox_db_transaction() as transaction:
        p = transaction.query(Parent).filter(Parent.id == parrent_id).all().pop()
        a = Association(extra_data="some data")
        a.child = Child()
        p.children.append(a)
        transaction.commit()
        cid = a.right_id
    return {"message": f"Hello new child. Your child id is {cid}"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
