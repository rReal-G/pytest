
from typing import Annotated, List
from pydantic import BaseModel, Field
from sqlalchemy import CheckConstraint, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

#from .song import Song_Pydantic



from .base import Base

from models import song

class Artist_Pydantic(BaseModel):
    id:int|None = None
    name:str
    age:Annotated[int, Field(le=99)]

    #from .song import Song_Pydantic
    #owned_songs:List[Song_Pydantic] = Field(default_factory=list) 
    owned_songs:List['song.Song_Pydantic'] = Field(default_factory=list) 


    class Config:
        orm_mode=True

    
class Artist(Base):
    __tablename__= 'Artists'
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(10))
    age: Mapped[int] = mapped_column()

    owned_songs:Mapped[List['song.Song']] = relationship()


        