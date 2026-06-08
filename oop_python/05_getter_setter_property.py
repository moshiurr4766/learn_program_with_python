"""Property getter and setter example."""


class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price  # This calls the setter below.

    @property
    def price(self):
        # Getter method runs when we read product.price.
        return self._price

    @price.setter
    def price(self, value):
        # Setter method runs when we assign product.price = value.
        if value < 0:
            raise ValueError("Price cannot be negative.")
        self._price = value


product = Product("Keyboard", 1200)
print(product.price)

product.price = 1500
print(product.price)
