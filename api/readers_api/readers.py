from fastapi import APIRouter, Request
from pydantic import BaseModel
from typing import List, Dict
from database.readersservice import *
import re

regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')


class Reader(BaseModel):
    name: str
    email: str
    password: str
    birthday: str
    fav_genre: str | None = None
    about: str | None = None
    admin_status: bool = False


readers_router = APIRouter(tags=["Управление читателями"], prefix="/readers")


@readers_router.post("/api/register")
async def register_reader(reader_model: Reader):
    reader_data = dict(reader_model)
    mail_validation = mail_checker(reader_model.email)
    if mail_validation:
        try:
            reg_reader = register_reader_db(**reader_data)
            return {"status": 1, "message": reg_reader}
        except Exception as e:
            return {"status": 0, "message": e}

    return {"status": 0, "message": "Invalid email"}


def mail_checker(email):
    if re.fullmatch(regex, email):
        return True
    return False


@readers_router.get("/api/reader")
async def get_reader(reader_id: int):
    exact_reader = profile_info_db(reader_id)
    if exact_reader:
        return {"status": 1, "message": exact_reader}
    return {"status": 0, "message": "Пользователь не найден"}


@readers_router.post("/api/login")
async def login_reader(login: str, password: str):
    checking = check_reader_password_db(login=login, password=password)
    if checking:
        return {"status": 1, "message": checking}
    return {"status": 0, "message": "Ошибка входа"}


@readers_router.put("/api/change_profile")
async def change_user_profile(reader_id: int, changeable_info: str, new_data: str):
    data = change_reader_data_db(reader_id=reader_id, changeable_info=changeable_info, new_data=new_data)
    if data:
        return {"status": 1, "message": "Данные успешно изменены"}
    return {"status": 0, "message": "Не удалось изменить информацию"}


@readers_router.delete("/api/delete_reader")
async def delete_reader_post(reader_id: int):
    try:
        delete_reader_db(reader_id)
        return {"status": 1, "message": "Юзер удален"}
    except:
        return {"status": 0, "message": "Не удалось удалить юзера"}
