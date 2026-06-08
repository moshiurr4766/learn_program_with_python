"""Problem: Find the nth Fibonacci number."""

# Problem:
# Find a specific Fibonacci number.


def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1

    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b


# Solution:
n = 10
print(f"The {n}th Fibonacci number is:", fibonacci(n))

# Logic:
# 1. Handle the first two values directly.
# 2. Build the sequence using a loop.
# 3. Return the nth value.

# Explanation:
# This is more efficient than naive recursion for larger values.
