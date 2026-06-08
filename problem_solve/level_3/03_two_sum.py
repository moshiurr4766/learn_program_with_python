"""Problem: Find two numbers that add up to a target."""

# Problem:
# Return the indices of two numbers whose sum equals the target.

numbers = [2, 7, 11, 15]
target = 9


def two_sum(nums, goal):
    seen = {}
    for index, number in enumerate(nums):
        required = goal - number
        if required in seen:
            return [seen[required], index]
        seen[number] = index
    return []


# Solution:
print("Indices:", two_sum(numbers, target))

# Logic:
# 1. Store numbers already seen in a dictionary.
# 2. Check whether the needed partner already exists.
# 3. Return the two indices when found.

# Explanation:
# This is an efficient dictionary-based lookup problem.
