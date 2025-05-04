from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from dotenv import load_dotenv
import os

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_engine(DATABASE_URL, echo=True)
SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)
Base = declarative_base()

# 데이터베이스 세션을 생성하는 함수
def get_db():
    db = SessionLocal()  # 세션 생성
    try:
        yield db  # 세션을 요청한 함수에 전달
    finally:
        db.close()  # 작업이 끝나면 세션을 닫음
