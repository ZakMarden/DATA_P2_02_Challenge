from lib.database_connection import DatabaseConnection
from lib.book_repository import BookRepo


# Connect to the database
connection = DatabaseConnection()
connection.connect()

# Seed with some seed data
connection.seed("seeds/book_store.sql")

# Retrieve all artists
book_repository = BookRepo(connection)

# List them out
for book in book_repository.all():
    print(book)
