
from httpx import delete
from sqlalchemy.orm.session import Session
from models.artist import Artist
from models.song import Song
from models.playlist import Playlist
from sql_orm_o2o_test import get_db
import repository.db_repository as repo


with get_db() as session: 
    session:Session

    # playlist = Playlist(name='test playlist')
    # song = repo.read_by_id(session, 5, Song)
    # if song:
    #     playlist.related_songs.append(song)
    #     session.add(playlist)
    #     session.commit()

    # playlist = session.query(Playlist).get(
    #     '06e82abe-a13a-4367-b01f-a42698825dd3'
    #     )
    # if playlist:
    #     playlist.related_songs.clear()
    #     session.commit()

    # song = repo.read_by_id(session, 5, Song)
    # session.delete(song)
    # session.commit()

    artist = repo.read_by_id(session, 5, Artist)
    session.delete(artist)
    session.commit()