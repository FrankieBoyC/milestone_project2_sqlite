from utils import database
import os


USER_CHOICE = """
Enter:
- 'a' to add a new book
- 'l' to list all books
- 'r' to mark a book as read
- 'd' to delete a book
- 'q' to quit

Your Choice: """


def menu():
    database.create_book_table()
    user_input = input(USER_CHOICE)
    while user_input != 'q':
        if user_input == 'a':
            prompt_add_book()
        elif user_input == 'l':
            list_books()
        elif user_input == 'r':
            prompt_read_book()
        elif user_input == 'd':
            prompt_delete_book()
        else:
            print("Not a valid command")

        user_input = input(USER_CHOICE)


def prompt_add_book():
    name = input("Enter book name: ")
    author = input("Enter book author: ")

    database.add_book(name, author)


def list_books():
    for book in database.get_all_books():
        read = 'YES' if book['read'] else 'NO'
        print(f"{book['name']} by {book['author']} - Read: {read}")


def prompt_read_book():
    name = input("Enter book name: ")
    database.read_book(name)


def prompt_delete_book():
    name = input("Enter book name to be deleted: ")
    database.delete_book(name)


menu()
