# from fastapi import FastAPI, Depends, HTTPException
# from sqlalchemy.orm import Session
# from pydantic import BaseModel
# from .database import SessionLocal, engine
# from .models import DataEntry
# from fastapi.middleware import Middleware
# from fastapi.middleware.cors import CORSMiddleware

# # ========== Add CORS middleware ==========
# middleware = [
#     Middleware(
#         CORSMiddleware,
#         allow_origins=["http://localhost:5000"],  # Flask frontend URL
#         allow_credentials=True,
#         allow_methods=["*"],  # Allow all methods (GET, POST, PUT, DELETE, etc.)
#         allow_headers=["*"],  # Allow all headers
#     )
# ]

# app = FastAPI(middleware=middleware)

# # Create tables if not exist
# from .models import Base
# Base.metadata.create_all(bind=engine)

# # Dependency
# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()

# # Pydantic Model
# class DataEntryCreate(BaseModel):
#     user_id: int
#     name: str
#     occupation: str
#     phone: str
#     address: str
#     description: str

# @app.post("/entries/", status_code=201)
# def create_entry(entry: DataEntryCreate, db: Session = Depends(get_db)):
#     db_entry = DataEntry(**entry.dict())
#     db.add(db_entry)
#     db.commit()
#     db.refresh(db_entry)
#     return db_entry

# @app.get("/entries/", response_model=list[DataEntryCreate])
# def read_entries(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
#     entries = db.query(DataEntry).offset(skip).limit(limit).all()
#     return entries

# @app.put("/entries/{entry_id}", response_model=DataEntryCreate)
# def update_entry(entry_id: int, entry: DataEntryCreate, db: Session = Depends(get_db)):
#     db_entry = db.query(DataEntry).filter(DataEntry.id == entry_id).first()
#     if not db_entry:
#         raise HTTPException(status_code=404, detail="Entry not found")
#     for key, value in entry.dict().items():
#         setattr(db_entry, key, value)
#     db.commit()
#     db.refresh(db_entry)
#     return db_entry

# @app.delete("/entries/{entry_id}")
# def delete_entry(entry_id: int, db: Session = Depends(get_db)):
#     db_entry = db.query(DataEntry).filter(DataEntry.id == entry_id).first()
#     if not db_entry:
#         raise HTTPException(status_code=404, detail="Entry not found")
#     db.delete(db_entry)
#     db.commit()
#     return {"message": "Entry deleted"}


# from fastapi import FastAPI,Depends,HTTPException
# from dotenv import load_dotenv
# from sqlalchemy.orm import Session
# from pydantic import BaseModel
# # In main.py, change imports to:
# from .database import SessionLocal, engine
# from .models import DataEntry, Base
# from fastapi.middleware import Middleware
# from fastapi.middleware.cors import CORSMiddleware
  
# import sys
# print(sys.path)  # Should include C:\project
# from .models import DataEntry, Base

# app = FastAPI()
# load_dotenv()
# # Create tables if not exist
# from .models import Base
# Base.metadata.create_all(bind=engine)
# # print(os.getenv("PYTHONPATH"))
# # Dependency
# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()

# # Pydantic Model
# class DataEntryCreate(BaseModel):
#     user_id: int
#     name: str
#     occupation: str
#     phone: str
#     address: str
#     description: str

# @app.post("/entries/", status_code=201)
# def create_entry(entry: DataEntryCreate, db: Session = Depends(get_db)):
#     db_entry = DataEntry(**entry.dict())
#     db.add(db_entry)
#     db.commit()
#     db.refresh(db_entry)
#     return db_entry

# @app.get("/entries/", response_model=list[DataEntryCreate])
# def read_entries(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
#     entries = db.query(DataEntry).offset(skip).limit(limit).all()
#     return entries

# @app.put("/entries/{entry_id}", response_model=DataEntryCreate)
# def update_entry(entry_id: int, entry: DataEntryCreate, db: Session = Depends(get_db)):
#     db_entry = db.query(DataEntry).filter(DataEntry.id == entry_id).first()
#     if not db_entry:
#         raise HTTPException(status_code=404, detail="Entry not found")
#     for key, value in entry.dict().items():
#         setattr(db_entry, key, value)
#     db.commit()
#     db.refresh(db_entry)
#     return db_entry

# @app.delete("/entries/{entry_id}")
# def delete_entry(entry_id: int, db: Session = Depends(get_db)):
#     db_entry = db.query(DataEntry).filter(DataEntry.id == entry_id).first()
#     if not db_entry:
#         raise HTTPException(status_code=404, detail="Entry not found")
#     db.delete(db_entry)
#     db.commit()
#     return {"message": "Entry deleted"}


# from fastapi import FastAPI, Depends, HTTPException
# from dotenv import load_dotenv
# from sqlalchemy.orm import Session
# from pydantic import BaseModel

# # In main.py, change imports to:
# from backend.database import SessionLocal, engine
# from backend.models import DataEntry, Base
# from fastapi.middleware.cors import CORSMiddleware
# from fastapi.middleware import Middleware

# import sys

# print(sys.path)  # Should include C:\project

# # ========== ADD CORS MIDDLEWARE HERE ==========
# middleware = [
#     Middleware(
#         CORSMiddleware,
#         allow_origins=["http://localhost:5000",
#           "http://127.0.0.1:5000"
#            ],  # Allow requests from Flask frontend
#         allow_credentials=True,
#         allow_methods=["*"],  # Allow all methods (GET, POST, PUT, DELETE)
#         allow_headers=["*"], 
#         # Allow all headers
#     )
# ]

# app = FastAPI(middleware=middleware)  # Apply middleware here
# # ========== END OF CORS CONFIG ==========

# load_dotenv()

# # Create tables if not exist
# from .models import Base
# Base.metadata.create_all(bind=engine)

# # Dependency
# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()

# # Pydantic Model
# class DataEntryCreate(BaseModel):
#     user_id: int
#     name: str
#     occupation: str
#     phone: str
#     address: str
#     description: str

# @app.post("/entries/", status_code=201)
# def create_entry(entry: DataEntryCreate, db: Session = Depends(get_db)):
#     db_entry = DataEntry(**entry.dict())
#     db.add(db_entry)
#     db.commit()
#     db.refresh(db_entry)
#     return db_entry

# @app.get("/entries/", response_model=list[DataEntryCreate])
# def read_entries(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
#     entries = db.query(DataEntry).offset(skip).limit(limit).all()
#     return entries

# @app.put("/entries/{entry_id}", response_model=DataEntryCreate)
# def update_entry(entry_id: int, entry: DataEntryCreate, db: Session = Depends(get_db)):
#     db_entry = db.query(DataEntry).filter(DataEntry.id == entry_id).first()
#     if not db_entry:
#         raise HTTPException(status_code=404, detail="Entry not found")
#     for key, value in entry.dict().items():
#         setattr(db_entry, key, value)
#     db.commit()
#     db.refresh(db_entry)
#     return db_entry

# @app.delete("/entries/{entry_id}")
# def delete_entry(entry_id: int, db: Session = Depends(get_db)):
#     db_entry = db.query(DataEntry).filter(DataEntry.id == entry_id).first()
#     if not db_entry:
#         raise HTTPException(status_code=404, detail="Entry not found")
#     db.delete(db_entry)
#     db.commit()
#     return {"message": "Entry deleted"}



# first step
# to run this with python crud project uvicorn backend.main:app --reload and run flask app

from fastapi import FastAPI, Depends, HTTPException
from dotenv import load_dotenv
from sqlalchemy.orm import Session
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware import Middleware

# In main.py, change imports to:
from backend.database import SessionLocal, engine
from backend.models import DataEntry, Base

import sys

print(sys.path)  # Should include C:\project

# ========== ADD CORS MIDDLEWARE HERE ==========
middleware = [
    Middleware(
        CORSMiddleware,
        allow_origins=["http://localhost:5000", "http://127.0.0.1:5000"],  # Allow requests from frontend
        allow_credentials=True,
        allow_methods=["*"],  # Allow all methods (GET, POST, PUT, DELETE)
        allow_headers=["*"],  # Allow all headers
    )
]

app = FastAPI(middleware=middleware)  # Apply middleware here
# ========== END OF CORS CONFIG ==========

load_dotenv()

# Create tables if not exist
Base.metadata.create_all(bind=engine)

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Pydantic Model
class DataEntryCreate(BaseModel):
    user_id: int
    name: str
    occupation: str
    phone: str
    address: str
    description: str

    class Config:
        orm_mode = True  # Enable ORM mode for SQLAlchemy compatibility

@app.post("/entries/", status_code=201)
def create_entry(entry: DataEntryCreate, db: Session = Depends(get_db)):
    db_entry = DataEntry(**entry.dict())
    db.add(db_entry)
    db.commit()
    db.refresh(db_entry)
    return db_entry

@app.get("/entries/", response_model=list[DataEntryCreate])
def read_entries(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    entries = db.query(DataEntry).offset(skip).limit(limit).all()
    return entries

@app.get("/entries/{user_id}", response_model=DataEntryCreate)
def get_entry_by_user_id(user_id: int, db: Session = Depends(get_db)):
    db_entry = db.query(DataEntry).filter(DataEntry.user_id == user_id).first()
    if not db_entry:
        raise HTTPException(status_code=404, detail="Entry not found")
    return db_entry

@app.put("/entries/{entry_id}", response_model=DataEntryCreate)
def update_entry(entry_id: int, entry: DataEntryCreate, db: Session = Depends(get_db)):
    db_entry = db.query(DataEntry).filter(DataEntry.id == entry_id).first()
    if not db_entry:
        raise HTTPException(status_code=404, detail="Entry not found")
    for key, value in entry.dict().items():
        setattr(db_entry, key, value)
    db.commit()
    db.refresh(db_entry)
    return db_entry

@app.delete("/entries/{entry_id}")
def delete_entry(entry_id: int, db: Session = Depends(get_db)):
    db_entry = db.query(DataEntry).filter(DataEntry.id == entry_id).first()
    if not db_entry:
        raise HTTPException(status_code=404, detail="Entry not found")
    db.delete(db_entry)
    db.commit()
    return {"message": "Entry deleted"}