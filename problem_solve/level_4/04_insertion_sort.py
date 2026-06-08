"""Problem: Sort a list using insertion sort."""

# Problem:
# Build a sorted list one item at a time.

numbers = [9, 5, 1, 4, 3]


def insertion_sort(items):
    arr = items[:]
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


# Solution:
print("Sorted list:", insertion_sort(numbers))

# Logic:
# 1. Take one item as the key.
# 2. Shift larger values to the right.
# 3. Insert the key into the correct place.

# Explanation:
# Insertion sort is easy to understand and good for small lists.
