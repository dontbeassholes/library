from database.models import Reader
from database import get_db
from datetime import datetime

def register_reader_db(name, email, about=None, password, reg_date, birthday, fav_genre=None):
    pass


def check_reader_db(name, email):
    pass


def check_reader_password_db(login, password):
    pass


def profile_info_db(user_id):
    pass


def change_reader_data_db(user_id, changeable_info, new_data)
    pass

