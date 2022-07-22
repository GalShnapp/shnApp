from ensurepip import version
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import Enum

Base = declarative_base()

class Parent(Base):
    __tablename__ = 'parent'
    id = Column(Integer, primary_key=True)
    children = relationship("Child", lazy="joined")

    def __repr__(self):
        return f''


class Child(Base):
    __tablename__ = 'child'
    id = Column(Integer, primary_key=True)

    def __repr__(self):
        return f''
