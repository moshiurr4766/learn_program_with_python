"""Simple project: library management system."""


class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_available = True

    def __str__(self):
        status = "Available" if self.is_available else "Borrowed"
        return f"{self.title} by {self.author} - {status}"


class Member:
    def __init__(self, name):
        self.name = name
        self.borrowed_books = []

    def borrow_book(self, book):
        if not book.is_available:
            return f"{book.title} is not available."

        book.is_available = False
        self.borrowed_books.append(book)
        return f"{self.name} borrowed {book.title}."

    def return_book(self, book):
        if book not in self.borrowed_books:
            return f"{self.name} did not borrow {book.title}."

        book.is_available = True
        self.borrowed_books.remove(book)
        return f"{self.name} returned {book.title}."


class Library:
    def __init__(self, name):
        self.name = name
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def show_books(self):
        print(f"\nBooks in {self.name}:")
        for book in self.books:
            print(book)


library = Library("City Library")
book_one = Book("Python Basics", "Guido van Rossum")
book_two = Book("Clean Code", "Robert C. Martin")
member = Member("Moshiur")

library.add_book(book_one)
library.add_book(book_two)

library.show_books()
print(member.borrow_book(book_one))
library.show_books()
print(member.return_book(book_one))
library.show_books()
