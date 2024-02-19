from contextlib import contextmanager
import json
from pydantic import BaseModel, ValidationError
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.song import Song, Song_Pydantic
from sqlalchemy.orm.session import Session
import repository.db_repository as repo
from models.artist import Artist, Artist_Pydantic


engine = create_engine(
    "sqlite:///database.db",
     echo=True)

session_maker = sessionmaker(engine)

@contextmanager
def get_db():
    with session_maker() as session:
        yield session  


def one_to_many_crud(get_db):
    artist = Artist(name='topg', age=69)
    with get_db() as session:
        session:Session
        # song = Song(name='soname')
        # artist.owned_songs.append(song)
        # new_artist = repo.create(session, artist)
        # pydantic_artist = Artist_Pydantic.model_validate(new_artist, from_attributes=True)
        # print(pydantic_artist.model_dump_json())

        # artist = repo.read_by_id(session, 1, Artist)
        # repo.delete(session, artist)

        # song = repo.read_by_id(session, 4, Song)
        # repo.delete(session, song)

        # #artist = repo.read_by_id(session, 4, Artist)
        # song = repo.read_by_id(session, 4, Song)
        # song.og_artist = None 
        # session.commit()

one_to_many_crud(get_db)


