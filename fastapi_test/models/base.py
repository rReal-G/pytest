
from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import CheckConstraint, String
from sqlalchemy.orm import Mapped, mapped_column

class Base(DeclarativeBase):
    pass

# class Artist(Base):
#     __tablename__ = 'artists'
#     id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
#     name: Mapped[str] = mapped_column(String(10))
#     age: Mapped[int] = mapped_column()

