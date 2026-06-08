"""Problem: Build a simple calculator."""

# Problem:
# Perform basic arithmetic using two numbers.

a = 20
b = 5
operation = "+"


def calculate(x, y, op):
    if op == "+":
        return x + y
    if op == "-":
        return x - y
    if op == "*":
        return x * y
    if op == "/":
        return x / y
    return "Invalid operation"


# Solution:
result = calculate(a, b, operation)
print("Result:", result)

# Logic:
# 1. Store the numbers and the operation.
# 2. Use if statements to choose the correct calculation.
# 3. Return the answer from a function.

# Explanation:
# Functions help organize repeated logic cleanly.
