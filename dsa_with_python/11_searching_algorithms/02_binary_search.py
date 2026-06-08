"""Binary search with multiple easy examples."""

# Example 1: iterative binary search
numbers = [1, 3, 5, 7, 9, 11, 13]
target = 9

left = 0
right = len(numbers) - 1
index = -1

while left <= right:
    mid = (left + right) // 2
    if numbers[mid] == target:
        index = mid
        break
    if numbers[mid] < target:
        left = mid + 1
    else:
        right = mid - 1

print("Index:", index)

# Example 2: recursive binary search
def binary_search(arr, left, right, goal):
    if left > right:
        return -1
    mid = (left + right) // 2
    if arr[mid] == goal:
        return mid
    if arr[mid] < goal:
        return binary_search(arr, mid + 1, right, goal)
    return binary_search(arr, left, mid - 1, goal)


print("Recursive:", binary_search(numbers, 0, len(numbers) - 1, 11))

# Example 3: binary search on insertion position
goal = 8
left = 0
right = len(numbers)

while left < right:
    mid = (left + right) // 2
    if numbers[mid] < goal:
        left = mid + 1
    else:
        right = mid

print("Insert position:", left)

# Logic:
# 1. Work only on sorted data.
# 2. Compare the middle item with the target.
# 3. Discard half of the list each step.

# Explanation:
# Binary search is fast because it keeps cutting the search space in half.
