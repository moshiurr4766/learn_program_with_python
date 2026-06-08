"""Problem: Find the transpose of a matrix."""

# Problem:
# Swap rows and columns in a matrix.

matrix = [
    [1, 2, 3],
    [4, 5, 6],
]

# Solution:
transpose = []

for col in range(len(matrix[0])):
    new_row = []
    for row in matrix:
        new_row.append(row[col])
    transpose.append(new_row)

print("Transpose:", transpose)

# Logic:
# 1. Move column by column.
# 2. Collect each column into a new row.
# 3. Build the new matrix.

# Explanation:
# Transpose switches the direction of data.
