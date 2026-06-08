"""Problem: Create a simple car rental system."""

# Problem:
# Rent and return cars using classes.


class Car:
    def __init__(self, model):
        self.model = model
        self.available = True


class RentalService:
    def __init__(self):
        self.cars = []

    def add_car(self, car):
        self.cars.append(car)

    def rent_car(self, model):
        for car in self.cars:
            if car.model == model and car.available:
                car.available = False
                return f"{model} rented"
        return f"{model} not available"

    def return_car(self, model):
        for car in self.cars:
            if car.model == model and not car.available:
                car.available = True
                return f"{model} returned"
        return f"{model} was not rented"


# Solution:
service = RentalService()
service.add_car(Car("Toyota"))
service.add_car(Car("Honda"))

print(service.rent_car("Toyota"))
print(service.return_car("Toyota"))

# Logic:
# 1. Keep a list of cars.
# 2. Mark a car unavailable when rented.
# 3. Mark it available again when returned.

# Explanation:
# This shows a small workflow with object state changes.
