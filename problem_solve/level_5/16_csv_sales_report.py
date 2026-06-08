"""Problem: Summarize sales from CSV-style rows."""

# Problem:
# Compute total sales per product from row data.

rows = [
    "phone,2,500",
    "pen,10,5",
    "book,3,20",
    "phone,1,500",
]

# Solution:
sales = {}

for row in rows:
    product, quantity, price = row.split(",")
    total = int(quantity) * int(price)
    sales[product] = sales.get(product, 0) + total

print("Sales report:", sales)

# Logic:
# 1. Split each row into fields.
# 2. Multiply quantity by price.
# 3. Add the amount into a dictionary summary.

# Explanation:
# This is a simple reporting pattern from tabular data.
