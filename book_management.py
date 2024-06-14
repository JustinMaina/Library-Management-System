from database import session
from models import Book

def add_book(title, author, copies):
    new_book = Book(title=title, author=author, copies=copies)
    session.add(new_book) 
    session.commit()

def get_all_books():
    return session.query(Book).all()

def update_book_copies(book_id, new_copies):
    book = session.query(Book).filter_by(id=book_id).first()
    if book:
        book.copies = new_copies
        session.commit()

def delete_book(book_id):
    book = session.query(Book).filter_by(id=book_id).first()
    if book:
        session.delete(book)
        session.commit()
