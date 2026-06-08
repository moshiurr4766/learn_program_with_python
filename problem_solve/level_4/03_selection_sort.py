"""Problem: Sort a list using selection sort."""

# Problem:
# Arrange numbers in ascending order.

numbers = [29, 10, 14, 37, 13]


def selection_sort(items):
    arr = items[:]
    for i in range(len(arr)):
        min_index = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr


# Solution:
print("Sorted list:", selection_sort(numbers))

# Logic:
# 1. Find the smallest item in the unsorted part.
# 2. Put it at the current position.
# 3. Move forward and repeat.

# Explanation:
# Selection sort is a useful way to practice loops and swapping.
