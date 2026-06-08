"""Function examples."""


def greet(name):
    """Return a greeting message."""
    return f"Hello, {name}!"


def add(a, b):
    return a + b


def calculate_bill(price, quantity=1, discount=0):
    total = price * quantity
    return total - discount


print(greet("Moshiur"))
print("Sum:", add(10, 5))
print("Bill:", calculate_bill(100, quantity=3, discount=20))

