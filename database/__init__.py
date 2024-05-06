from sqlalchemy import create_engine
from sqlalchemy import sessionmaker, declarative_base

SQLALCHEMY_DATABASE_URL = 'sqllite:///data.db'
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    except Exception:
        db.rollback()
        raise
    finally:
        db.close()


