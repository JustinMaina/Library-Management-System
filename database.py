from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Book, Member, Borrow

DATABASE_URL = 'sqlite:///library.db'

engine = create_engine(DATABASE_URL)
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()
