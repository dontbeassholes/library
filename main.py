from fastapi import FastAPI
from database import Base, engine
from api.readers_api.readers import readers_router
from api.books_api.books import books_router


Base.metadata.create_all(bind=engine)
app = FastAPI(docs_url='/')

app.include_router(readers_router)
app.include_router(books_router)