
from typing import Annotated
from pydantic import BaseModel, Field
from sqlalchemy import CheckConstraint, String
from sqlalchemy.orm import Mapped, mapped_column

from .base import Base





class Artist(Base):
    __tablename__ = 'artists'
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(10))
    age: Mapped[int] = mapped_column()


class Artist_Pydantic(BaseModel):
    id:int|None = None
    name:str
    age:Annotated[int, Field(le=99)]
    class Config:
        orm_mode=True