from main import Book

def test_book_title():
    harry_potter = Book("Harry Potter ed il calice di fuoco", "autore", 45)
    assert harry_potter.title == "Harry Potter ed il calice di fuoco"