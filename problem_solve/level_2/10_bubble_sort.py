"""Problem: Sort a list using bubble sort."""

# Problem:
# Sort numbers in ascending order without using sort().

numbers = [5, 1, 4, 2, 8]
n = len(numbers)

# Solution:
for i in range(n):
    for j in range(0, n - i - 1):
        if numbers[j] > numbers[j + 1]:
            numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]

print("Sorted list:", numbers)

# Logic:
# 1. Compare neighboring values.
# 2. Swap them if they are in the wrong order.
# 3. Repeat until the list is sorted.

# Explanation:
# Bubble sort is a classic way to practice nested loops.
