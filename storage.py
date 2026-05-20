import json
import os
from models import Book

FILE_NAME = 'books.json'

def load_books():
    if not os.path.exists(FILE_NAME):
        return []
    with open(FILE_NAME, 'r', encoding='utf-8') as f:
        data = json.load(f)
    return [Book.from_dict(item) for item in data]

def save_books(books):
    with open(FILE_NAME, 'w', encoding='utf-8') as f:
        json.dump([book.to_dict() for book in books], f, ensure_ascii=False, indent=4)

def add_book(book):
    books = load_books()
    # Проверка дубликатов по автору и названию
    for b in books:
        if b.author == book.author and b.title == book.title:
            print("Такая книга уже есть.")
            return False
    books.append(book)
    save_books(books)
    return True

def list_books():
    return load_books()

def delete_book(author, title):
    books = load_books()
    new_books = [b for b in books if not (b.author == author and b.title == title)]
    if len(books) == len(new_books):
        print("Книга не найдена.")
        return False
    save_books(new_books)
    return True
