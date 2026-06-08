"""Problem: Find a pair with a given sum using two pointers."""

# Problem:
# In a sorted list, find whether two numbers add up to the target.

numbers = [1, 2, 4, 6, 8, 11, 15]
target = 14


def pair_sum(items, goal):
    left = 0
    right = len(items) - 1

    while left < right:
        current = items[left] + items[right]
        if current == goal:
            return (items[left], items[right])
        if current < goal:
            left += 1
        else:
            right -= 1
    return None


# Solution:
print("Pair:", pair_sum(numbers, target))

# Logic:
# 1. Start from both ends of the sorted list.
# 2. Move the left pointer up if the sum is too small.
# 3. Move the right pointer down if the sum is too large.

# Explanation:
# Two pointers work well when the data is sorted.
