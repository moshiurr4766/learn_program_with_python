"""Problem: Find an item using linear search."""

# Problem:
# Search for a target value in a list.

numbers = [14, 22, 7, 19, 31]
target = 19


def linear_search(items, goal):
    for index, value in enumerate(items):
        if value == goal:
            return index
    return -1


# Solution:
print("Index:", linear_search(numbers, target))

# Logic:
# 1. Check each item one by one.
# 2. Stop when the target is found.
# 3. Return -1 if it does not exist.

# Explanation:
# Linear search is simple and works on any list.
