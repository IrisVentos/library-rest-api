from typing import List, Optional
from models import Book

class BookRepository:
    """Handles all database operations for books"""
    
    def __init__(self):
        self._books_db = [
            {
                "id": 1,
                "title": "Le petit Prince",
                "author": "Antoine de Saint Exupery",
                "isbn": "978-2070612758", 
                "publication_year": 1943,
                "pages": 96, 
                "available": True,
                "description": "A philosophical and poetic tale"
            }
        ]
    
    def get_all(self) -> List[dict]:
        """Retrieve all books"""
        return self._books_db
    
    def get_by_id(self, book_id: int) -> Optional[dict]:
        """Retrieve a book by ID"""
        for book in self._books_db:
            if book["id"] == book_id:
                return book
        return None
    
    def create(self, book_data: dict) -> dict:
        """Create a new book"""
        new_id = max([book["id"] for book in self._books_db]) + 1 if self._books_db else 1
        book = {"id": new_id, **book_data}
        self._books_db.append(book)
        return book
    
    def update(self, book_id: int, book_data: dict) -> Optional[dict]:
        """Update an existing book"""
        for index, book in enumerate(self._books_db):
            if book["id"] == book_id:
                self._books_db[index] = {"id": book_id, **book_data}
                return self._books_db[index]
        return None
    
    def delete(self, book_id: int) -> bool:
        """Delete a book by ID"""
        for index, book in enumerate(self._books_db):
            if book["id"] == book_id:
                self._books_db.pop(index)
                return True
        return False
