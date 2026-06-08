"""Search in a rotated sorted array."""

# Example 1: search in rotated array
numbers = [6, 7, 8, 1, 2, 3, 4, 5]
target = 2

left = 0
right = len(numbers) - 1
index = -1

while left <= right:
    mid = (left + right) // 2
    if numbers[mid] == target:
        index = mid
        break

    if numbers[left] <= numbers[mid]:
        if numbers[left] <= target < numbers[mid]:
            right = mid - 1
        else:
            left = mid + 1
    else:
        if numbers[mid] < target <= numbers[right]:
            left = mid + 1
        else:
            right = mid - 1

print("Index:", index)

# Example 2: find pivot
pivot = 0
for i in range(1, len(numbers)):
    if numbers[i] < numbers[i - 1]:
        pivot = i
        break
print("Pivot:", pivot)

# Example 3: actual sorted view
sorted_view = numbers[pivot:] + numbers[:pivot]
print("Sorted view:", sorted_view)

# Logic:
# 1. One half of the array is always sorted.
# 2. Use that sorted half to decide which side to keep.
# 3. Repeat until the target is found.

# Explanation:
# Rotated arrays need a smarter version of binary search.
