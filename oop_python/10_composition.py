"""Composition example."""


class Engine:
    def start(self):
        return "Engine started."


class Car:
    def __init__(self, brand):
        self.brand = brand
        self.engine = Engine()  # Car has an Engine object.

    def drive(self):
        return f"{self.brand}: {self.engine.start()} Driving now."


car = Car("Toyota")

print(car.drive())
