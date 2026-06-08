"""Magic method example."""


class Book:
    def __init__(self, title, pages):
        self.title = title
        self.pages = pages

    def __str__(self):
        # Used by print(object).
        return f"{self.title} has {self.pages} pages."

    def __len__(self):
        # Used by len(object).
        return self.pages

    def __add__(self, other):
        # Used by object_one + object_two.
        return self.pages + other.pages


book_one = Book("Python Basics", 120)
book_two = Book("OOP Python", 90)

print(book_one)
print(len(book_one))
print(book_one + book_two)
