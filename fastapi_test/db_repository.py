from typing import TypeVar
from requests import session

from sqlalchemy import Select
from sqlalchemy.orm.session import Session
from sqlalchemy.orm import Mapped, mapped_column, relationship

from typing import Protocol
from models.song import Song
from models.artist import Artist

class HasId(Protocol):
    id: Mapped[int]

T = TypeVar('T', bound=HasId)

def create(db: Session, instance:T) -> T:
    db.add(instance)
    db.commit()
    return instance

def read_by_id(db: Session, instance_id:int, orm_class: type[T]) -> T | None:
    if not hasattr(orm_class, 'id'):
        raise ValueError("Instance must have an 'id' attribute")
    return db.query(orm_class).filter(orm_class.id == instance_id).first()

def delete(db: Session, instance):
    db.delete(instance)
    db.commit()
    return instance

def update_remove_child(db:Session, parent:Artist, child:Song):
    parent.owned_songs.remove(child)
    db.commit()

def update(db: Session, instance: T, 
           updates: dict, allowed_updates: set[str] | None = None) -> T:

    for attr, value in updates.items():
        if hasattr(instance, attr) and (allowed_updates is None or attr in allowed_updates):
            setattr(instance, attr, value)
    db.commit()
    db.refresh(instance)
    return instance

# from contextlib import contextmanager
# @contextmanager
# def get_file():
#     with open('test.py', 'r') as file:
#         yield file
#         # contents = file.read()
#         # return contents   

# from contextlib import contextmanager
# @contextmanager
# def get_file2():
#     try:
#         file = open('test.py', 'r')
#         yield file
#         # with open('test.py', 'r') as file:
#         #     yield file
#     finally:
#         file.close()
#         #yield file


# with get_file() as file:
#     print(file.readline())
# print(file.closed)
# #print(file.readline())
        
# # f = get_file2()
# # file = next(f)
# # print(file.readline())
# # next(f)
# # print(file.readline())