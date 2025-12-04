# Library API

A REST API to manage a collection of books, built with FastAPI and following OOP principles.

To add, delete or update data, can use formatting via Postman interface (curl payload) for the command lines
You can open two terminals, one to launch the main and start the API, one to do any command you want

## Features
- CRUD operations for books
- Layered architecture (Repository, Service, API)
- In-memory database

## Installation
\`\`\`bash
pip install fastapi uvicorn pydantic
\`\`\`

## Run
\`\`\`bash
python main.py
\`\`\`

## API Endpoints
- GET /books - List all books
- GET /books/{id} - Get specific book
- POST /books - Create new book
- PUT /books/{id} - Update book
- DELETE /books/{id} - Delete book
