"""Problem: Find an item using binary search."""

# Problem:
# Search a sorted list efficiently.

numbers = [2, 4, 6, 8, 10, 12, 14]
target = 10


def binary_search(items, goal):
    left = 0
    right = len(items) - 1

    while left <= right:
        mid = (left + right) // 2
        if items[mid] == goal:
            return mid
        if items[mid] < goal:
            left = mid + 1
        else:
            right = mid - 1
    return -1


# Solution:
print("Index:", binary_search(numbers, target))

# Logic:
# 1. Check the middle element.
# 2. Keep only the half that can still contain the target.
# 3. Repeat until found or empty.

# Explanation:
# Binary search is much faster on sorted data.
