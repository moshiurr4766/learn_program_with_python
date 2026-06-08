"""Problem: Apply discounts to products."""

# Problem:
# Calculate final prices after discounts.


class Product:
    def __init__(self, name, price, discount=0):
        self.name = name
        self.price = price
        self.discount = discount

    def final_price(self):
        return self.price - (self.price * self.discount / 100)


# Solution:
products = [
    Product("Laptop", 80000, 10),
    Product("Mouse", 1500, 5),
]

for product in products:
    print(product.name, product.final_price())

# Logic:
# 1. Store name, price, and discount in a class.
# 2. Compute the discounted value in a method.
# 3. Print the final price for each product.

# Explanation:
# Classes make business rules easy to keep together.
