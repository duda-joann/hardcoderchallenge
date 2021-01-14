import os

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Integer, Sequence, String, create_engine


Base = declarative_base()
base_dir = os.path.abspath(os.path.dirname(__file__))
db_path = os.path.join(base_dir, 'books.db')
engine = create_engine('sqlite:///'+db_path, echo=True)
Base.metadata.create_all(engine)

class MyBooks(Base):
    __tablename__ = 'MyBooks'
    book_id = Column(Integer, Sequence('seq_book_id'), primary_key = True)
    title = Column(String, Sequence('seq_book_title'))
    author = Column(String, Sequence('seq_book_author'))
    publisher = Column(String,  Sequence('seq_publisher'))
    publication_year = Column(String, Sequence('seq_year_published'))

    def __repr__(self):
        return f'MyBooks({self.book_id}, {self.title}, {self.author}, {self.publisher}, {self.publication_year}'


if __name__ == '__main__':
    Session = sessionmaker(bind=engine)
    session = Session()
