"""Problem: Print a row of Pascal's triangle."""

# Problem:
# Generate the nth row of Pascal's triangle.

row_number = 5


def pascal_row(n):
    row = [1]
    for i in range(1, n):
        row.append(row[i - 1] * (n - i) // i)
    return row


# Solution:
print("Row:", pascal_row(row_number))

# Logic:
# 1. Start each row with 1.
# 2. Build new values from the previous one.
# 3. Use the combinational formula pattern.

# Explanation:
# Pascal rows can be generated without building the full triangle.
