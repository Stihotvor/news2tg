import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

POSTGRES_USER = os.getenv('POSTGRES_USER', 'newsbot')
POSTGRES_PASSWORD = os.getenv('POSTGRES_PASSWORD', 'newsbot')
POSTGRES_DB = os.getenv('POSTGRES_DB', 'newsbot')
POSTGRES_HOST = os.getenv('POSTGRES_HOST', 'localhost')
POSTGRES_PORT = os.getenv('POSTGRES_PORT', '5432')

DATABASE_URL = f"postgresql+psycopg2://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"

engine = create_engine(DATABASE_URL, echo=True, future=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Sample Article model
from sqlalchemy import Column, Integer, String, Text, DateTime
import datetime

class Article(Base):
    __tablename__ = 'articles'
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(512), nullable=False)
    summary = Column(Text, nullable=True)
    source_url = Column(String(1024), nullable=False)
    published_at = Column(DateTime, default=datetime.datetime.utcnow)
    language = Column(String(16), default='en')
    status = Column(String(32), default='new')
