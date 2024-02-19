

from typing import Annotated, List
import uuid
from pydantic import BaseModel, Field
from sqlalchemy import CheckConstraint, Column, Date, ForeignKey, String, Table
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import date

#from .song import Song_Pydantic
from .base import Base

from models import song

playlist_song = Table(
    "playlist_song",
    Base.metadata,
    Column("song_id", ForeignKey("Songs.id")),
    Column("playlist_id", ForeignKey("Playlists.id")),
)

class Playlist(Base):
    __tablename__= 'Playlists'
    id: Mapped[str] = mapped_column(primary_key=True, default=str(uuid.uuid4()))
    name: Mapped[str] = mapped_column(String(10))
    created_date: Mapped[date] = mapped_column(default=date.today())

    related_songs:Mapped[List['song.Song']] = relationship(
        secondary=playlist_song,
        back_populates='related_playlists'
        #cascade='all, delete'
    )




        