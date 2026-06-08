"""Problem: Print Fibonacci series."""

# Problem:
# Print the first 7 Fibonacci numbers.
# Fibonacci series starts with 0 and 1.

count = 7
a = 0
b = 1

# Solution:
print("Fibonacci series:")

for _ in range(count):
    print(a, end=" ")
    a, b = b, a + b

print()

# Logic:
# 1. Start with 0 and 1.
# 2. Print the current value.
# 3. Update the next pair using a, b = b, a + b.

# Explanation:
# Each number is the sum of the previous two numbers.
