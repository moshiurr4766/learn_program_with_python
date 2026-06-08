"""Polymorphism example."""


class Dog:
    def speak(self):
        return "Woof!"


class Cat:
    def speak(self):
        return "Meow!"


class Cow:
    def speak(self):
        return "Moo!"


animals = [Dog(), Cat(), Cow()]

for animal in animals:
    # Same method name, but each object gives a different result.
    print(animal.speak())
