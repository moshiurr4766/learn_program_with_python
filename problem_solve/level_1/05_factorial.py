"""Problem: Find the factorial of a number."""

# Problem:
# Calculate factorial of a number like 5! = 5 * 4 * 3 * 2 * 1.

number = 5

# Solution:
factorial = 1

for i in range(1, number + 1):
    factorial *= i

print("Factorial:", factorial)

# Logic:
# 1. Start with 1.
# 2. Multiply by every number from 1 to n.
# 3. Store the running result in factorial.

# Explanation:
# Factorial is a product of all positive integers up to n.
