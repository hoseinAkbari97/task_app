from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = "mysql+mysqlconnector://root:123@localhost:3306/tasks"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
def get_database_session():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()