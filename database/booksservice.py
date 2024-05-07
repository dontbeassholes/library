from database.models import Book, Review
from database import get_db
from datetime import datetime

def create_book_db(title, author, genre, description=None, photo_to_path=None, rating=0):
    db = next(get_db())
    new_book = Book(title=title, author=author, genre=genre, description=description, photo_to_path=photo_to_path, rating=rating)
    db.add(new_book)
    db.commit()
    return True

def get_book_db(book_id):
    db = next(get_db())
# тут надо чето дописать

def update_book_db(book_id, changeable_info, new_data):
    db = next(get_db())
    book = db.query(Book).filter_by(id=book_id).first()
    if book:
        try:
            if changeable_info == "title":
                book.title = new_data
                db.commit()
                return True
            elif changeable_info == "author":
                book.author = new_data
                db.commit()
                return True
            elif changeable_info == "genre":
                book.genre = new_data
                db.commit()
                return True
            elif changeable_info == "genre":
                book.genre = new_data
                db.commit()
                return True
            elif changeable_info == "description":
                book.description = new_data
                db.commit()
                return True
            elif changeable_info == "photo_to_path":
                book.photo_to_path = new_data
                db.commit()
                return True
        except:
            return "вы не можете поменять информацию сейчас"
    return False


def delete_book_db(book_id):
    db = next(get_db())
    book_to_delete = db.query(Book).filter_by(id=book_id).first()
    if book_to_delete:
        db.delete(book_to_delete)
        db.commit()
        return True
    return False


def get_all_books():
    db = next(get_db())
    all_books = db.query(Book).all()
    return [i for i in all_books]


def get_book_reviews


def get_book_average_rating