"""Problem: Print matrix elements in spiral order."""

# Problem:
# Read a matrix in spiral order.

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]

# Solution:
top = 0
bottom = len(matrix) - 1
left = 0
right = len(matrix[0]) - 1
spiral = []

while top <= bottom and left <= right:
    for i in range(left, right + 1):
        spiral.append(matrix[top][i])
    top += 1

    for i in range(top, bottom + 1):
        spiral.append(matrix[i][right])
    right -= 1

    if top <= bottom:
        for i in range(right, left - 1, -1):
            spiral.append(matrix[bottom][i])
        bottom -= 1

    if left <= right:
        for i in range(bottom, top - 1, -1):
            spiral.append(matrix[i][left])
        left += 1

print("Spiral order:", spiral)

# Logic:
# 1. Track the top, bottom, left, and right borders.
# 2. Move around the edges one layer at a time.
# 3. Shrink the borders after each pass.

# Explanation:
# Spiral traversal is a common matrix problem.
