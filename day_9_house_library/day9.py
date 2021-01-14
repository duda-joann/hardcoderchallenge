import requests
from day_9_house_library.models import MyBooks, engine
from sqlalchemy.orm import sessionmaker


class HouseLibrary:
    def __init__(self, author: str)->None:
        """
        a parameter which will be used to  get data from api
        :param author:
        """
        self.author = author

    def get_api(self):
        """
        get data from api
        :return:  dictionary with results
        """
        url = 'http://data.bn.org.pl/api/bibs.json'
        params = {'author': self.author, 'limit':100}
        request = requests.get(url, params = params)
        if request.status_code != 200:
            return 'Could not connect'

        data = request.json()
        results = {}
        for number, record in enumerate(data['bibs']):
            results[number] = {
            'author': record['author'],
            'title': record['title'],
            'publisher': record['publisher'],
            'publication_year': record['publicationYear'],
            'amount': 1
            }

        return results

    @staticmethod
    def get_all_books():
        """
        get all borrowed books """
        return MyBooks.query.all()

    def borrow(self, book_id: int) -> None:
        """borrow book, saved to database to table my books"""
        results = self.get_api()

        new_book = MyBooks(
                            author=results[book_id]['author'],
                            title=results[book_id]['title'],
                            publisher=results[book_id]['publisher'],
                            publication_year=results[book_id]['publicationYear']
        )

        Session = sessionmaker(bind=engine)
        session = Session()
        session.add(new_book)
        session.commit()

        return self.get_all_books()

    def remove(self, book_id: int) -> None:
        """
        def remove book from my books, with id """
        book = MyBooks.query.filter(id = book_id).first()
        Session = sessionmaker(bind=engine)
        session = Session()
        session.delete(book)
        session.commit()

        return self.get_all_books()


def main()-> None:
    author = input('Please provide author name:')
    results = HouseLibrary(author).get_api()
    for key, value in results.items():
        print(key, value)

    rent_book = input('Please provide  number  of book: ')
    HouseLibrary.borrow(rent_book)


if __name__ == '__main__':
    main()
