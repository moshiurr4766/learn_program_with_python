"""Problem: Analyze library books by category."""

# Problem:
# Count books in each category.


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, title, category):
        self.books.append({"title": title, "category": category})

    def category_report(self):
        report = {}
        for book in self.books:
            category = book["category"]
            report[category] = report.get(category, 0) + 1
        return report


# Solution:
library = Library()
library.add_book("Python 101", "Programming")
library.add_book("Clean Code", "Programming")
library.add_book("Atomic Habits", "Self Help")
print(library.category_report())

# Logic:
# 1. Store books as dictionaries.
# 2. Count each category with a report dictionary.
# 3. Return the final summary.

# Explanation:
# This is a small analytics-style class problem.
