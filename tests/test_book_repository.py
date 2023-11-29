from lib.book_repository import BookRepo
from lib.book import Book


'''
when we call all, get back a list of all instances of book
'''

def test_all(db_connection):
    db_connection.seed("seeds/book_store.sql")
    repository = BookRepo(db_connection)
    result = repository.all()
    assert result == [
        Book(1, "Nineteen Eighty-Four", "George Orwell"),
        Book(2, "Mrs Dalloway", "Virginia Woolf"),
        Book(3, "Emma", "Jane Austen"),
        Book(4, "Dracula", "Bram Stoker"),
        Book(5, "The Age of Innocence", "Edith Wharton")
    ]