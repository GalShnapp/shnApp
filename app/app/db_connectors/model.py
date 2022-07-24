from ensurepip import version
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import Enum

Base = declarative_base()

class Association(Base):
    __tablename__ = "association"
    left_id = Column(ForeignKey("left.id"), primary_key=True)
    right_id = Column(ForeignKey("right.id"), primary_key=True)
    extra_data = Column(String(50))
    child = relationship("Child")


class Parent(Base):
    __tablename__ = "left"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    children = relationship("Association")


class Child(Base):
    __tablename__ = "right"
    id = Column(Integer, primary_key=True)
    name = Column(String)