from backend.database import Base
from sqlalchemy import Column, Integer, String

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True)
    email = Column(String, unique=True)
    password = Column(String)

class DataEntry(Base):
    __tablename__ = 'data_entries'

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer)
    name = Column(String)
    occupation = Column(String)
    phone = Column(String)
    address = Column(String)
    description = Column(String)