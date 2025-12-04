from typing import List, Optional
from models import Book, BookCreate
from repository import BookRepository

class BookService:
    """Business logic layer for book operations"""
    
    def __init__(self, repository: BookRepository):
        self.repository = repository
    
    def get_all_books(self) -> List[dict]:
        """Get all books from repository"""
        return self.repository.get_all()
    
    def get_book_by_id(self, book_id: int) -> Optional[dict]:
        """Get a specific book by ID"""
        return self.repository.get_by_id(book_id)
    
    def create_book(self, book_data: BookCreate) -> dict:
        """Create a new book"""
        return self.repository.create(book_data.dict())
    
    def update_book(self, book_id: int, book_data: BookCreate) -> Optional[dict]:
        """Update an existing book"""
        return self.repository.update(book_id, book_data.dict())
    
    def delete_book(self, book_id: int) -> bool:
        """Delete a book"""
        return self.repository.delete(book_id)
