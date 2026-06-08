"""Linear search with multiple easy examples."""

# Example 1: find the index of a value
numbers = [8, 3, 7, 1, 9]
target = 7
index = -1

for i, value in enumerate(numbers):
    if value == target:
        index = i
        break

print("Index:", index)

# Example 2: find all matching positions
items = [5, 2, 5, 8, 5, 1]
matches = []

for i, value in enumerate(items):
    if value == 5:
        matches.append(i)

print("All matches:", matches)

# Example 3: check whether item exists
names = ["Moshiur", "Nadia", "Rahim"]
found = False

for name in names:
    if name == "Nadia":
        found = True
        break

print("Found:", found)

# Logic:
# 1. Start from the first element.
# 2. Compare each item one by one.
# 3. Stop when you find the target or finish the list.

# Explanation:
# Linear search is the easiest search method to write.
