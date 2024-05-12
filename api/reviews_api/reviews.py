from fastapi import APIRouter, HTTPException
from datetime import datetime
from database.reviewsservice import *

reviews_router = APIRouter(prefix='/reviews_api', tags=['Управление рецензиями'])


@reviews_router.post("/api/add_review")
async def add_review(reader_id: int, book_id: int, review_text: str = None):
    new_review = public_review_db(reader_id=reader_id, book_id=book_id, review_text=review_text)
    if new_review:
        return {"status": 1, "message": "Рецензия успешно добавлена"}
    raise HTTPException(status_code=404, detail="не удалось добавить книгу")


@reviews_router.get("/api/book_reviews")
async def get_book_reviews(book_id: int):
    exact_reviews = get_exact_book_review_db(book_id)
    if exact_reviews:
        return {"status": 1, "message": exact_reviews}
    raise HTTPException(status_code=404, detail="Рецензии на книгу не найдены")


@reviews_router.get("/api/reader_reviews")
async def get_reader_reviews(reader_id: int):
    reader_reviews = get_reader_reviews_db(reader_id)
    if reader_reviews:
        return {"status": 1, "message": reader_reviews}
    raise HTTPException(status_code=404, detail="Рецензии пользователя не найдены")


@reviews_router.put("api/edit_review")
async def edit_review(review_id: int, new_text: str):
    if review_id and new_text:
        change_review_text_db(review_id=review_id, new_text=new_text)
        return {"status": 1, "message": "Рецензия успешно изменена"}
    raise HTTPException(status_code=404, detail="Рецензия не найдена или не удалось изменить текст")


@reviews_router.delete("api/delete_review")
async def delete_review(review_id: int):
    try:
        delete_exact_review_db(review_id)
        return {"status": 1, "message": "Рецензия успешно удалена"}
    except:
        raise HTTPException(status_code=404, detail="Рецензия не найдена или не удалось удалить")





