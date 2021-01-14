"""#HOUSE #LIBRARY
Napisz program, który importuje katalog z dowolnej biblioteki (np. API Biblioteki Narodowej http://data.bn.org.pl/ -
przykład użycia: http://data.bn.org.pl/api/bibs.json?author=Andrzej+Sapkowski&amp;kind=ksi%C4%85%C5%BCka).
 Użytkownik może podać autora i program pokaże mu, jakie książki tego autora są w zbiorach biblioteki.
Następnie daj użytkownikowi możliwość “wypożyczania” i “zwracania” książek - posiadane pozycje są składowane
w pliku zawierającym pewien identyfikujący zbiór danych, np. tytuł, autor, wydawnictwo, rok wydania
 (możesz też użyć lokalnej bazy danych), w przypadku “wypożyczenia” książki są do niego dodawane,
 a w przypadku “zwracania” usuwane.
Propozycja rozszerzenia: W prostym przypadku lokalne “wypożyczanie” nie ma wpływu na katalog biblioteki,
 czyli w teorii można wypożyczyć książkę nieskończoną liczbę razy. Zabezpiecz program w taki sposób,
  aby podczas pobierania danych rozpoznawał też pozycje “wypożyczone” lokalnie i
  nie pokazywał ich już jako wyniki wyszukiwania."""

import requests
from day_9_house_library.models import MyBooks, engine
from sqlalchemy.orm import sessionmaker


class HouseLibrary:
    def __init__(self, author:str)->None:
        self.author = author

    def get_api(self):
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
        return MyBooks.query.all()

    def borrow(self, book_id: int) -> None:
        results = self.get_api()

        new_book = MyBooks(
                            author = results[book_id]['author'],
                            title = results[book_id]['title'],
                            publisher = results[book_id]['publisher'],
                            publication_year = results[book_id]['publicationYear']
        )

        Session = sessionmaker(bind=engine)
        session = Session()
        session.add(new_book)
        session.commit()

        return self.get_all_books()

    def remove(self, book_id) -> None:
        book = MyBooks.query.filter(id = book_id).first()
        Session = sessionmaker(bind=engine)
        session = Session()
        session.delete(book)
        session.commit()

        return self.get_all_books()


def main():
    author = input('Please provide author name:')
    results = HouseLibrary(author).get_api()
    for key, value in results.items():
        print(key, value)

    rent_book = input('Please provide  number  of book: ')
    HouseLibrary.borrow(rent_book)


if __name__ == '__main__':
    main()
