from fastapi import Request, Body, UploadFile, APIRouter
from database.booksservice import *
from urllib import request

books_router = APIRouter(prefix="/books",
                         tags=["Управление книгами"])


@books_router.post("/api/add_book")
async def add_book(title: str, author: str, genre: str, description: str = None, photo_to_path: str = None, rating: int = 0):
    new_book = create_book_db(title=title, author=author, genre=genre, description=description,
                              photo_to_path=photo_to_path, rating=rating)
    if new_book:
        return {"status": 1, "message": "книга успешно добавлена"}
    return {"status": 0, "message": "не удалось добавить книгу"}

#прописать гет бук и гет все ьукс


@books_router.put("/api/books")
async def change_book(book_id: int, changeable_info: str, new_data: str):
    data = update_book_db(book_id=book_id, changeable_info=changeable_info, new_data=new_data)
    if data:
        return {"status": 1, "message": "Данные успешно изменен"}
    return {"status": 0, "message": "Не удалось изменить информацию"}


@books_router.delete("/api/books")
async def delete_book(reader_id: int):
    try:
        delete_book_db(reader_id)
        return {"status": 1, "message": "Книга успешно удалена"}
    except:
        return {"status": 0, "message": "Не удалось удалить книгу"}
