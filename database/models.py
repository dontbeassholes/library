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


class Genre(Base):
    __tablename__ = 'genres'
    id = Column(Integer, autoincrement=True, primary_key=True)
    genre_name = Column(String, nullable=False, unique=True)


class Book(Base):
    __tablename__ = 'books'
    id = Column(Integer, autoincrement=True, primary_key=True)
    title = Column(String, nullable=False)
    author = Column(String, nullable=False)
    genre = Column(String, ForeignKey('genres.genre_name'), nullable=False)
    description = Column(String, nullable=True)
    photo_path = Column(String, nullable=True)
    rating = Column(Float, nullable=True)
    read_status = Column(Boolean, default=False)
    user_book_status = Column(Integer, ForeignKey('readers.id'))

    genre_fk = relationship(Genre, lazy='subquery')
    reader_fk = relationship(Reader, lazy='subquery')



class Review(Base):
    __tablename__ = 'review'
    id = Column(Integer, autoincrement=True, primary_key=True)
    reader_id = Column(Integer, ForeignKey('readers.id'))
    book_id = Column(Integer, ForeignKey('books.id'))
    rating = Column(Integer, ForeignKey('books.rating'))
    review_text = Column(String, nullable=True)

    reader_fk = relationship(Book, lazy='subquery')
    book_fk = relationship(Book, lazy='subquery')
    rating_fk = relationship(Book, lazy='subquery')




