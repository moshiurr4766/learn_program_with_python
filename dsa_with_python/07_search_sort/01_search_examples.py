"""Search examples."""

# Example 1: linear search
numbers = [8, 3, 7, 1, 9]
target = 7
index = -1
for i, value in enumerate(numbers):
    if value == target:
        index = i
        break
print("Linear search index:", index)

# Example 2: binary search
sorted_numbers = [1, 3, 5, 7, 9, 11]
target = 9
left, right = 0, len(sorted_numbers) - 1
found = -1
while left <= right:
    mid = (left + right) // 2
    if sorted_numbers[mid] == target:
        found = mid
        break
    if sorted_numbers[mid] < target:
        left = mid + 1
    else:
        right = mid - 1
print("Binary search index:", found)

# Example 3: search in 2D matrix
matrix = [[1, 2], [3, 4], [5, 6]]
print(any(4 in row for row in matrix))

# Logic:
# 1. Search may be direct or divide-and-conquer.
# 2. Binary search needs sorted data.
# 3. Matrix search often loops row by row.

# Explanation:
# Search algorithms differ mainly in how much data they skip.
