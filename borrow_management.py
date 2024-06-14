from datetime import date
from database import session
from models import Borrow, Book

def borrow_book(book_id, member_id):
    book = session.query(Book).filter_by(id=book_id).first()
    if book and book.copies > 0:
        new_borrow = Borrow(book_id=book_id, member_id=member_id, borrow_date=date.today())
        book.copies -= 1
        session.add(new_borrow)
        session.commit()
    else:
        print("Book not available")

def return_book(borrow_id):
    borrow = session.query(Borrow).filter_by(id=borrow_id).first()
    if borrow and borrow.return_date is None:
        borrow.return_date = date.today()
        book = session.query(Book).filter_by(id=borrow.book_id).first()
        book.copies += 1
        session.commit()
