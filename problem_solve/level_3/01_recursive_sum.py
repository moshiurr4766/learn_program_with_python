"""Problem: Calculate the sum of a list using recursion."""

# Problem:
# Find the sum of all numbers in a list without using sum().

numbers = [1, 2, 3, 4, 5]


def recursive_sum(items):
    if not items:
        return 0
    return items[0] + recursive_sum(items[1:])


# Solution:
print("Sum:", recursive_sum(numbers))

# Logic:
# 1. The empty list returns 0.
# 2. Add the first item to the sum of the rest.
# 3. Repeat until the list becomes empty.

# Explanation:
# Recursion solves the problem by reducing it step by step.
