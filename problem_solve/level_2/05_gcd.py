"""Problem: Find the GCD of two numbers."""

# Problem:
# Find the greatest common divisor.

a = 48
b = 18

# Solution:
while b != 0:
    a, b = b, a % b

print("GCD:", a)

# Logic:
# 1. Use Euclid's algorithm.
# 2. Replace the larger number with the remainder.
# 3. Repeat until the remainder becomes 0.

# Explanation:
# This is one of the fastest ways to find the GCD.
