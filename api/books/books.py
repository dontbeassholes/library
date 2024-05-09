from fastapi import Request, Body, UploadFile, APIRouter
from database.booksservice import *
from urllib import request

books_router = APIRouter(prefix="/books",
                         tags=["Управление книгами"])


@books_router.post("/api/add_book")
async def add_book(reader_id: int, title: str, author: str, genre: str, description: str = None,
                   photo_to_path: str = None, rating: int = 0):
    new_book = create_book_db(reader_id=reader_id, title=title, author=author, genre=genre, description=description,
                              photo_to_path=photo_to_path, rating=rating)
    if new_book:
        return {"status": 1, "message": "книга успешно добавлена"}
    return {"status": 0, "message": "не удалось добавить книгу"}


@books_router.get("/{book_id}")
async def get_book_by_id(book_id: int):
    book = get_book_by_id_db(book_id)
    if book:
        return {"status": 1, "message": book}
    return {"status": 0, "message": "Книга не найдена"}


@books_router.get("/api/books")
async def get_all_books():
    books = get_all_books_db()
    return books


@books_router.put("/{book_id}")
async def update_book_info(book_id: int, reader_id: int, changeable_info: str, new_data: str):
    updated = update_book_db(reader_id=reader_id, book_id=book_id, changeable_info=changeable_info, new_data=new_data)
    if updated:
        return {"status": 1, "message": "Данные успешно изменены"}
    return {"status": 0, "message": "Не удалось изменить информацию"}


@books_router.delete("/{book_id}")
async def delete_book(reader_id: int, book_id: int):
    deleted = delete_book_db(reader_id=reader_id, book_id=book_id)
    if deleted:
        return {"status": 1, "message": "Книга успешно удалена"}
    else:
        return {"status": 0, "message": "Не удалось удалить книгу"}
