"""Problem: Print a number pattern."""

# Problem:
# Print a growing triangle of numbers.

n = 5

# Solution:
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()

# Logic:
# 1. Use the outer loop for rows.
# 2. Use the inner loop for numbers in each row.
# 3. Print a new line after each row.

# Explanation:
# Nested loops are common in pattern problems.
