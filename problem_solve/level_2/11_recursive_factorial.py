"""Problem: Find factorial using recursion."""

# Problem:
# Calculate factorial with a recursive function.


def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)


# Solution:
number = 5
print("Factorial:", factorial(number))

# Logic:
# 1. A small number is the base case.
# 2. A bigger number calls the same function again.
# 3. The result is built step by step.

# Explanation:
# Recursion means a function calling itself.
