from database import get_db
from database.models import Review
from datetime import datetime


def public_review_db(reader_id, book_id, review_text = None):
    db = next(get_db())
    new_review = Review(reader_id=reader_id, book_id=book_id, review_text=review_text, created_at=datetime.now())
    db.add(new_review)
    db.commit()
    return new_review


def get_exact_book_review_db(book_id):
    db = next(get_db())
    exact_reviews = db.query(Review).filter_by(book_id=book_id).all()
    if exact_reviews:
        return exact_reviews
    return False


def get_reader_reviews_db(reader_id):
    db = next(get_db())
    reader_reviews = db.query(Review).filter_by(reader_id=reader_id).all()
    if reader_reviews:
        return reader_reviews
    return False


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

