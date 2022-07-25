from pydantic import BaseModel
from typing import List


class ChildBase(BaseModel):
    name: str


class ChildCreate(ChildBase):
    pass


class Child(ChildBase):
    id: int

    class Config:
        orm_mode = True


class ParentBase(BaseModel):
    name: str


class ParentCreate(ParentBase):
    pass


class Parent(ParentBase):
    id: int
    children: List[Child]

    class Config:
        orm_mode = True