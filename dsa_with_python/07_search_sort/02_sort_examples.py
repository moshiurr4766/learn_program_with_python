"""Sort examples."""

# Example 1: bubble sort
numbers = [5, 1, 4, 2, 8]
arr = numbers[:]
for i in range(len(arr)):
    for j in range(0, len(arr) - i - 1):
        if arr[j] > arr[j + 1]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]
print("Bubble:", arr)

# Example 2: insertion sort
arr = numbers[:]
for i in range(1, len(arr)):
    key = arr[i]
    j = i - 1
    while j >= 0 and arr[j] > key:
        arr[j + 1] = arr[j]
        j -= 1
    arr[j + 1] = key
print("Insertion:", arr)

# Example 3: selection sort
arr = numbers[:]
for i in range(len(arr)):
    min_index = i
    for j in range(i + 1, len(arr)):
        if arr[j] < arr[min_index]:
            min_index = j
    arr[i], arr[min_index] = arr[min_index], arr[i]
print("Selection:", arr)

# Logic:
# 1. Sorting arranges data into order.
# 2. Each algorithm uses a different swap strategy.
# 3. Copy the original list to keep examples independent.

# Explanation:
# Sorting is a foundational algorithm topic.
