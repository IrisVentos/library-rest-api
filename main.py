from fastapi import FastAPI, HTTPException, status
from typing import List
import uvicorn

from models import Book, BookCreate
from repository import BookRepository
from service import BookService

class LibraryAPI:
    """Main application class that sets up FastAPI and routes"""
    
    def __init__(self):
        self.app = FastAPI(
            title="Library API",
            description="REST API to manage a collection of books",
            version="1.0.0"
        )
        
        # Initialize dependencies
        self.repository = BookRepository()
        self.service = BookService(self.repository)
        
        # Register routes
        self._register_routes()
    
    def _register_routes(self):
        """Register all API routes"""
        
        @self.app.get("/")
        def read_root():
            """Root endpoint of the API"""
            return {
                "message": "Welcome to the Library API",
                "version": "1.0.0"
            }
        
        @self.app.get("/books", response_model=List[Book])
        def get_all_books():
            """Retrieve the complete list of books"""
            return self.service.get_all_books()
        
        @self.app.get("/books/{book_id}", response_model=Book)
        def get_book(book_id: int):
            """Retrieve a specific book by its ID"""
            book = self.service.get_book_by_id(book_id)
            if not book:
                raise HTTPException(
                    status_code=404,
                    detail=f"Book with ID {book_id} not found"
                )
            return book
        
        @self.app.post("/books", response_model=Book, status_code=status.HTTP_201_CREATED)
        def create_book(new_book: BookCreate):
            """Create a new book in the library"""
            return self.service.create_book(new_book)
        
        @self.app.put("/books/{book_id}", response_model=Book)
        def update_book(book_id: int, updated_book: BookCreate):
            """Completely update an existing book"""
            book = self.service.update_book(book_id, updated_book)
            if not book:
                raise HTTPException(
                    status_code=404,
                    detail=f"Book with ID {book_id} not found"
                )
            return book
        
        @self.app.delete("/books/{book_id}", status_code=status.HTTP_204_NO_CONTENT)
        def delete_book(book_id: int):
            """Delete a book from library"""
            if not self.service.delete_book(book_id):
                raise HTTPException(
                    status_code=404,
                    detail=f"Book with ID {book_id} not found"
                )
            return
    
    def run(self, host: str = "127.0.0.1", port: int = 8001):
        """Run the application"""
        uvicorn.run(self.app, host=host, port=port)


if __name__ == "__main__":
    library_api = LibraryAPI()
    library_api.run()

