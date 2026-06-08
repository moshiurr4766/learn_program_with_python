"""Problem: Sum all even numbers in a list."""

# Problem:
# Find the sum of only the even numbers in a list.

numbers = [3, 4, 7, 10, 12, 15]

# Solution:
total = 0

for number in numbers:
    if number % 2 == 0:
        total += number

print("Sum of even numbers:", total)

# Logic:
# 1. Go through each number.
# 2. Check whether it is even.
# 3. Add only even numbers to the total.

# Explanation:
# This combines looping and condition checking.
