from lib.book import Book

'''
contructs with id, title, author_name
'''

def test_contructs_with_fields():
    book = Book(1, "Test", "Test Author")
    assert book.id == 1
    assert book.title == "Test"
    assert book.author_name == "Test Author"

def test_equality():
    book_1 = Book(1, "Test", "Test Author")
    book_2 = Book(1, "Test", "Test Author")
    assert book_1 == book_2

def test_formatting():
    book = Book(1, "Test", "Test Author")
    assert str(book) == "Book(1, Test, Test Author)"