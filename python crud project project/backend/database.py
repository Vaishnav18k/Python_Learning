from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

# Correct way to use environment variables
SQLALCHEMY_DATABASE_URL = os.getenv("postgresql://postgres:root123@127.0.0.1:5432/postgres", "postgresql://postgres:root123@127.0.0.1:5432/postgres")
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()