import json
from pydantic import BaseModel, ValidationError
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models.artist import Artist, Artist_Pydantic

engine = create_engine(
    "sqlite:///database.db",
     echo=True)

session_maker = sessionmaker(engine)

with session_maker() as session:
    #artist = Artist(name='topG', age=99)
    try:
        pydantic_input = Artist_Pydantic(name='top G hehe', age=100)
    except ValidationError as v:
        print(v)
        print('hehe validation error')
    else:
        artist = Artist(name=pydantic_input.name, age=pydantic_input.age)
        session.add(artist)
        session.commit()
        #session.refresh(artist)
        artist_pydantic = Artist_Pydantic.model_validate(artist, 
                                                        from_attributes=True)
        print(artist_pydantic.model_dump_json())