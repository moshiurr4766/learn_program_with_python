"""Problem: Build a simple inventory manager."""

# Problem:
# Track products and quantities in stock.


class InventoryManager:
    def __init__(self):
        self.items = {}

    def add_item(self, name, quantity):
        self.items[name] = self.items.get(name, 0) + quantity

    def remove_item(self, name, quantity):
        if self.items.get(name, 0) < quantity:
            return "Not enough stock."
        self.items[name] -= quantity
        return f"Removed {quantity} {name}"

    def show_items(self):
        return self.items


# Solution:
inventory = InventoryManager()
inventory.add_item("Pen", 20)
inventory.add_item("Notebook", 15)
print(inventory.remove_item("Pen", 5))
print(inventory.show_items())

# Logic:
# 1. Store stock in a dictionary.
# 2. Increase or decrease quantities through methods.
# 3. Return the current inventory state.

# Explanation:
# This is a practical OOP problem for data tracking.
