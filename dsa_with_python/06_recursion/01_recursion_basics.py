"""Recursion basics."""

# Example 1: factorial
def factorial(n):
    if n in (0, 1):
        return 1
    return n * factorial(n - 1)

print("Factorial:", factorial(5))

# Example 2: sum of natural numbers
def total(n):
    if n == 0:
        return 0
    return n + total(n - 1)

print("Sum:", total(5))

# Example 3: reverse a string recursively
def reverse_text(text):
    if len(text) <= 1:
        return text
    return reverse_text(text[1:]) + text[0]

print(reverse_text("code"))

# Logic:
# 1. A recursion needs a base case.
# 2. The function calls itself on a smaller input.
# 3. Results build back up as the calls return.

# Explanation:
# Recursion is useful when a problem breaks into similar subproblems.
