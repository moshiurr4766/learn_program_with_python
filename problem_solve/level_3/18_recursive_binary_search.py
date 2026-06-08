"""Problem: Search a value using recursive binary search."""

# Problem:
# Find a target in a sorted list using recursion.

numbers = [1, 3, 5, 7, 9, 11, 13]
target = 9


def binary_search(arr, left, right, goal):
    if left > right:
        return -1

    mid = (left + right) // 2

    if arr[mid] == goal:
        return mid
    if arr[mid] > goal:
        return binary_search(arr, left, mid - 1, goal)
    return binary_search(arr, mid + 1, right, goal)


# Solution:
print("Index:", binary_search(numbers, 0, len(numbers) - 1, target))

# Logic:
# 1. Pick the middle value.
# 2. Compare it with the target.
# 3. Search only the left or right half.

# Explanation:
# Binary search is efficient because it cuts the search space in half each time.
