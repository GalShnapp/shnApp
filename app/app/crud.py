from sqlalchemy.orm import Session

from . import schemas
from app.db_connectors.engine import get_sandbox_db_transaction
from app.db_connectors.model import Parent, Child, Association

def get_parent(db: Session, parent_id: int):
    return db.query(Parent).filter(Parent.id == parent_id).first()

def get_child(db: Session, child_id: int):
    return db.query(Child).filter(Child.id == child_id).first()

def get_associations_of_parent(db: Session, parent_id: int):
    return db.query(Association).filter(Association.left_id == parent_id).all()

def get_associations_of_child(db: Session, child_id: int):
    return db.query(Association).filter(Association.right_id == child_id).all()