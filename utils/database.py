from typing import List, Dict, Union

from .database_connection import DatabaseConnection

"""
Concerned with retrieving and storing books from a SQLite database.
"""

Book = Dict[str, Union[str, int]]


def create_book_table() -> None:
    """Connects to the SQLite database and creates the table."""
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()

        cursor.execute('CREATE TABLE IF NOT EXISTS books(name text primary key, author text , read integer)')


def add_book(name: str, author: str) -> None:
    """Adds a book to the database."""
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()

        cursor.execute('INSERT INTO books VALUES(?, ?, 0)', (name, author))


def get_all_books() -> List[Book]:
    """Retrieves all books from the database."""
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()

        cursor.execute('SELECT * FROM books')
        books = [{'name': row[0], 'author': row[1], 'read': row[2]} for row in cursor.fetchall()]
    return books


def read_book(name: str) -> None:
    """Marks a book as read."""
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()

        cursor.execute('UPDATE books SET read=1 WHERE name=?', (name,))


def delete_book(name: str) -> None:
    """Deletes a book from the database."""
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()

        cursor.execute('DELETE FROM books WHERE name=?', (name,))





