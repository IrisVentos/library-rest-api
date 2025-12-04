from pydantic import BaseModel
from typing import Optional

class Book(BaseModel): 
    id: int
    title: str 
    author: str
    isbn: str 
    publication_year: int
    pages: int 
    available: bool = True
    description: Optional[str] = None

class BookCreate(BaseModel):
    title: str
    author: str
    isbn: str
    publication_year: int
    pages: int 
    available: bool = True
    description: Optional[str] = None