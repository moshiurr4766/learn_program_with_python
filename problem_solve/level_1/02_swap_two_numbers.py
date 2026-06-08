"""Problem: Swap two numbers."""

# Problem:
# Exchange the values of two variables.

a = 5
b = 10

# Solution:
a, b = b, a
print("a =", a)
print("b =", b)

# Logic:
# 1. Use tuple unpacking.
# 2. The right side is evaluated first.
# 3. Values are swapped without a temporary variable.

# Explanation:
# Python makes swapping simple and readable.
