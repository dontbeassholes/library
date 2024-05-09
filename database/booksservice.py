from database.models import Book, Genre, Review, Reader
from database import get_db
from datetime import datetime


def create_book_db(reader_id, title, author, genre, description=None, photo_to_path=None, rating=0):
    db = next(get_db())
    status_checker = db.query(Reader).filter_by(id=reader_id).first()
    if status_checker.admin_status:
        new_book = Book(title=title, author=author, genre=genre, description=description, photo_to_path=photo_to_path,
                        rating=rating)
        db.add(new_book)
        db.commit()
        return True


def get_book_db(book_id):
    db = next(get_db())
    book_to_get = db.query(Book).filter_by(id=book_id).first()
    if book_to_get:
        return book_to_get
    return False


def get_all_books():
    db = next(get_db())
    all_books = db.query(Book).all()
    return [i for i in all_books]


def update_book_db(reader_id, book_id, changeable_info, new_data):
    db = next(get_db())
    status_checker = db.query(Reader).filter_by(id=reader_id).first()
    if status_checker.admin_status:
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


def delete_book_db(reader_id, book_id):
    db = next(get_db())
    status_checker = db.query(Reader).filter_by(id=reader_id).first()
    if status_checker.admin_status:
        book_to_delete = db.query(Book).filter_by(id=book_id).first()
        if book_to_delete:
            db.delete(book_to_delete)
            db.commit()
            return True
        return False


def add_genre(reader_id, genre_name):
    db = next(get_db())
    status_checker = db.query(Reader).filter_by(id=reader_id).first()
    if status_checker.admin_status:
        new_genre = Genre(genre_name=genre_name)
        db.add(new_genre)
        db.commit()
        return True


def get_exact_genre_db(genre_name):
    db = next(get_db())
    exact_genre = db.query(Genre).filter_by(genre_name=genre_name).first()
    return exact_genre


def get_some_genre_db(size, genre_name):
    db = next(get_db())
    books = db.query(Book).filter_by(genre=genre_name).limit(size).all()
    return books


def public_review_db(reader_id, book_id, review_text):
    db = next(get_db())
    new_review = Review(reader_id=reader_id, book_id=book_id, review_text=review_text, created_at=datetime.now())
    db.add(new_review)
    db.commit()
    return True


def get_exact_book_review_db(book_id):
    db = next(get_db())
    exact_reviews = db.query(Review).filter_by(book_id=book_id).all()
    return exact_reviews


def change_review_text_db(review_id, new_text):
    db = next(get_db())
    review_to_edit = db.query(Review).filter_by(id=review_id).first()
    if review_to_edit:
        review_to_edit.review_text = new_text
        db.commit()
        return True
    return False


def delete_exact_review_db(review_id):
    db = next(get_db())
    review_to_delete = db.query(Review).filter_by(id=review_id).first()
    if review_to_delete:
        db.delete(review_to_delete)
        db.commit()
        return True
    return False


# def get_book_average_rating