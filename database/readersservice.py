from database.models import Reader
from database import get_db
from datetime import datetime


def check_reader_db(name, email):
    db = next(get_db())
    checker_name = db.query(Reader).filter_by(name=name).first()
    checker_email = db.query(Reader).filter_by(email=email).first()
    if checker_name:
        return "Юзернейм занят"
    elif checker_email:
        return "Почта занята"
    return True


def register_reader_db(name, email, password, birthday, fav_genre=None,  about=None, admin_status=False):
    db = next(get_db())
    checker = check_reader_db(name, email)
    if checker:
        new_reader = Reader(name=name, email=email, about=about, password=password, reg_date=datetime.now(),
                            birthday=birthday, fav_genre=fav_genre, admin_status=admin_status
                            )
        db.add(new_reader)
        db.commit()
        return new_reader.id
    return checker


def check_reader_password_db(login, password):
    db = next(get_db())
    user_by_email = db.query(Reader).filter_by(email=login).first()
    print(login, user_by_email)
    if user_by_email:
        if user_by_email.password == password:
            return user_by_email.id
    return 'вы ввели неправильные данные'


def profile_info_db(reader_id):
    db = next(get_db())
    reader_info = db.query(Reader).filter_by(id=reader_id).first()
    if reader_info:
        return reader_info
    return False


def change_reader_data_db(reader_id, changeable_info, new_data):
    db = next(get_db())
    reader = db.query(Reader).filter_by(id=reader_id).first()
    if reader:
        try:
            if changeable_info == "name":
                reader.name = new_data
                db.commit()
                return True
            elif changeable_info == "email":
                reader.email = new_data
                db.commit()
                return True
            elif changeable_info == "about":
                reader.about = new_data
                db.commit()
                return True
            elif changeable_info == "password":
                reader.password = new_data
                db.commit()
                return True
            elif changeable_info == "birthday":
                reader.birthday = new_data
                db.commit()
                return True
            elif changeable_info == "fav_genre":
                reader.genre = new_data
                db.commit()
                return True
        except:
            return "вы не можете поменять эту информацию"
    return False


def delete_reader_db(reader_id):
    db = next(get_db())
    reader_to_delete = db.query(Reader).filter_by(id=reader_id).first()
    if reader_to_delete:
        db.delete(reader_to_delete)
        db.commit()
        return True

    return False


def get_user_read_books_db(reader_id):
    db = next(get_db())
    reader = db.query(Reader).filter_by(id=reader_id).first()
    if any(book.read_status for book in reader.user_book_status):
        return 'Вы прочитали книгу!'
    return "пользователь не прочел ни одной книги"

# если выйдет ошибка то используй это!
# def get_user_read_books_db(reader_id):
#     db = next(get_db())
#     reader = db.query(Reader).filter_by(id=reader_id).first()
#     if reader:
#         read_books = db.query(Book).filter_by(user_book_status=reader_id, read_status=True).all()
#         if read_books:
#             return 'Вы прочитали книгу!'
#         return "Пользователь не прочел ни одной книги"
#     return "Пользователь не найден"
def get_user_reviews_db(reader_id):
    db = next(get_db())
    reader = db.query(Reader).filter_by(id=reader_id).first()
    if reader:
        return reader.review_text
    return "вы не оставили ни один отзыв"
