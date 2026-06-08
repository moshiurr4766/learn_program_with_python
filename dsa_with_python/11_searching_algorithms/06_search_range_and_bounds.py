"""Search range and bounds examples."""

# Example 1: first and last position of a number
numbers = [1, 2, 2, 2, 3, 4, 5]
target = 2

first = -1
last = -1

for i, value in enumerate(numbers):
    if value == target:
        if first == -1:
            first = i
        last = i

print("Range:", (first, last))

# Example 2: lower bound
goal = 2
left = 0
right = len(numbers)
while left < right:
    mid = (left + right) // 2
    if numbers[mid] < goal:
        left = mid + 1
    else:
        right = mid
print("Lower bound:", left)

# Example 3: upper bound
goal = 2
left = 0
right = len(numbers)
while left < right:
    mid = (left + right) // 2
    if numbers[mid] <= goal:
        left = mid + 1
    else:
        right = mid
print("Upper bound:", left)

# Logic:
# 1. Range search finds the first and last match.
# 2. Lower bound is the first value not less than target.
# 3. Upper bound is the first value greater than target.

# Explanation:
# These bounds are useful in sorted-array problems.
