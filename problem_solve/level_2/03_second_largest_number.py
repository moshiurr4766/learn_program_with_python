"""Problem: Find the second largest number."""

# Problem:
# Find the second largest number in a list.

numbers = [12, 45, 7, 33, 45, 28]

# Solution:
unique_numbers = list(set(numbers))
unique_numbers.sort(reverse=True)
second_largest = unique_numbers[1]

print("Second largest number:", second_largest)

# Logic:
# 1. Remove duplicates.
# 2. Sort the numbers in descending order.
# 3. Pick the second item.

# Explanation:
# This is a simple way to solve the problem clearly.
