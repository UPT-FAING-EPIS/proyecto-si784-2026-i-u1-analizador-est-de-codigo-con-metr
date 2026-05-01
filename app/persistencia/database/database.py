import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.persistencia.models.models import Base


DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "postgresql+psycopg2://postgres:postgres@localhost:5432/analizador_codigo",
)

engine = create_engine(DATABASE_URL, pool_pre_ping=True)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
