"""Problem: Search a value in a matrix."""

# Problem:
# Find whether a number exists in a matrix.

matrix = [
    [1, 4, 7],
    [8, 10, 12],
    [13, 15, 18],
]
target = 10

# Solution:
found = False

for row in matrix:
    if target in row:
        found = True
        break

print("Found:", found)

# Logic:
# 1. Move through each row.
# 2. Check whether the target is inside the row.
# 3. Stop as soon as it is found.

# Explanation:
# Matrix search often starts with simple row checks.
