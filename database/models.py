from sqlalchemy import Column, String, Integer, Float, DateTime, ForeignKey, Boolean, Date
from sqlalchemy import relationship
from database import Base


class Reader(Base):
    __tablename__ = 'readers'
    id = Column(Integer, autoincrement=True, primary_key=True)
    name = Column(String, unique=True)
    email = Column(String, nullable=False, unique=True)
    about = Column(String, nullable=True, unique=False)
    password = Column(String, nullable=False)
    reg_date = Column(DateTime)
    birthday = Column(Date, nullable=False)
    fav_genre = Column(String, nullable=True)

class Book(Base):
    __tablename__ = 'books'
    id = Column(Integer, autoincrement=True, primary_key=True)
    title = Column(String, nullable=False)
    author = Column(String, nullable=False)
    genre = Column(String, nullable=False)
    description = Column(String, nullable=True)
    photo_path = Column(String, nullable=True)
    rating = Column(Float, nullable=True, nado chtobi po umolchaniyu bilo nol)

class Genre(Base):
    __tablename__ = 'genres'
    id = Column(Integer, autoincrement=True, primary_key=True)
    genre_name = Column(String, nullable=False, unique=True)
    book_id = Column(Integer, ForeignKey('books.id'))

    book_fk = relationship(Book, lazy='subquery')




