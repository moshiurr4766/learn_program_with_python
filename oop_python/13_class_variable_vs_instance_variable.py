"""Class variable vs instance variable."""


class Counter:
    total_objects = 0  # Class variable, shared by all objects.

    def __init__(self, name):
        self.name = name  # Instance variable, unique for each object.
        Counter.total_objects += 1


first = Counter("First")
second = Counter("Second")

print(first.name)
print(second.name)
print(Counter.total_objects)
