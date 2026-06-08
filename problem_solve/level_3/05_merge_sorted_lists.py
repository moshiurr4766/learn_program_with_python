"""Problem: Merge two sorted lists."""

# Problem:
# Combine two sorted lists into one sorted list.

list_one = [1, 3, 5, 7]
list_two = [2, 4, 6, 8]


def merge_sorted(a, b):
    merged = []
    i = j = 0

    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            merged.append(a[i])
            i += 1
        else:
            merged.append(b[j])
            j += 1

    merged.extend(a[i:])
    merged.extend(b[j:])
    return merged


# Solution:
print("Merged list:", merge_sorted(list_one, list_two))

# Logic:
# 1. Compare the front items of both lists.
# 2. Add the smaller one to the result.
# 3. Add leftovers when one list ends.

# Explanation:
# This is the core idea behind merge sort merging.
