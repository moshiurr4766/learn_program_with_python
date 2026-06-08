"""Problem: Calculate area of different shapes."""

# Problem:
# Use one interface for multiple shape area calculations.

import math


class Shape:
    def area(self):
        return 0


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


# Solution:
shapes = [Circle(3), Rectangle(4, 5)]
for shape in shapes:
    print(round(shape.area(), 2))

# Logic:
# 1. Create a common base shape.
# 2. Override area() in each child class.
# 3. Call the same method on different objects.

# Explanation:
# This is a neat example of polymorphism.
