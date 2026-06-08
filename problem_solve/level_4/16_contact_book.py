"""Problem: Create a contact book."""

# Problem:
# Store and look up contacts.


class ContactBook:
    def __init__(self):
        self.contacts = {}

    def add_contact(self, name, phone):
        self.contacts[name] = phone

    def find_contact(self, name):
        return self.contacts.get(name, "Not found")

    def show_all(self):
        return self.contacts


# Solution:
book = ContactBook()
book.add_contact("Moshiur", "01700000001")
book.add_contact("Nadia", "01700000002")
print(book.find_contact("Nadia"))
print(book.show_all())

# Logic:
# 1. Use a dictionary for contact storage.
# 2. Add and fetch contacts with methods.
# 3. Return the full contact list when needed.

# Explanation:
# Dictionaries are ideal for lookup-heavy applications.
