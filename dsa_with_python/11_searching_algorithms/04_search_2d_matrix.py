"""Search in a 2D matrix."""

# Example 1: top-right search
matrix = [
    [1, 4, 7],
    [2, 5, 8],
    [3, 6, 9],
]
target = 5

row = 0
col = len(matrix[0]) - 1
found = False

while row < len(matrix) and col >= 0:
    value = matrix[row][col]
    if value == target:
        found = True
        break
    if value > target:
        col -= 1
    else:
        row += 1

print("Found:", found)

# Example 2: flat search
exists = any(target in row_values for row_values in matrix)
print("Exists by flat scan:", exists)

# Example 3: row by row search
position = None
for r, row_values in enumerate(matrix):
    if target in row_values:
        position = (r, row_values.index(target))
        break
print("Position:", position)

# Logic:
# 1. Start from the top-right corner.
# 2. Move left if the value is too large.
# 3. Move down if the value is too small.

# Explanation:
# This method works well when rows and columns are sorted.
