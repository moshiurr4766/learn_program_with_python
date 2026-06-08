"""Problem: Find the largest of three numbers."""

# Problem:
# Compare three numbers and print the largest one.

a = 15
b = 42
c = 27

# Solution:
largest = a

if b > largest:
    largest = b

if c > largest:
    largest = c

print("Largest number:", largest)

# Logic:
# 1. Assume the first number is the largest.
# 2. Compare it with the other numbers one by one.
# 3. Update the largest value when needed.

# Explanation:
# This uses simple comparison and variable updating.
