import uvicorn
from fastapi import FastAPI
from db.model import Parent, Child, Association
from db.engine import get_sandbox_db_transaction

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/get_children_ids/{parent_id}")
async def get_children_ids(parrent_id: int):
    _p = None
    with get_sandbox_db_transaction() as transaction:
        p = transaction.query(Parent).join(Child).filter(Parent.id == parrent_id).first()
        _p = [child.id for child in p.children]
    return {"message": f"Hello parent {parrent_id}, your children will be right here!\n enjoy {_p}"}

@app.get("/get_parent_id/{child_id}")
async def get_parent_id(child_id: int):
    return {"message": f"Hello Child {child_id}, your parent will be right here!"}

@app.post("/new_parent")
async def create_new_parent():
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

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)