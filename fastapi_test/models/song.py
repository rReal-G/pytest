from typing import Annotated
from pydantic import BaseModel, Field
from sqlalchemy import CheckConstraint, ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship



# from .artist import Artist
from .base import Base

class Song(Base):
    __tablename__ = 'Songs'
    id:Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name:Mapped[str] = mapped_column(String(10))

    artist_id: Mapped[int] = mapped_column(ForeignKey('Artists.id'))

    #og_artist:Mapped['Artist'] = relationship(back_populates='owned_songs')


class Song_Pydantic(BaseModel):
    id:int|None
    name:str

    artist_id:int
    #og_artist:Artist_Pydantic

    class Config:
        orm_mode=True