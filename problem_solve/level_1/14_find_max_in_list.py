"""Problem: Find the largest number in a list."""

# Problem:
# Find the maximum value in a list without using max().

numbers = [4, 18, 7, 29, 11]

# Solution:
largest = numbers[0]

for number in numbers:
    if number > largest:
        largest = number

print("Largest number:", largest)

# Logic:
# 1. Assume the first item is the largest.
# 2. Compare every item with the current largest.
# 3. Replace it when a bigger value appears.

# Explanation:
# This is a common scanning technique.
