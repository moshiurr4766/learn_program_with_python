"""Problem: Flatten a nested list."""

# Problem:
# Convert a nested list into a single flat list.

nested_list = [1, [2, 3], [4, [5, 6]], 7]

# Solution:
flat_list = []


def flatten(items):
    for item in items:
        if isinstance(item, list):
            flatten(item)
        else:
            flat_list.append(item)


flatten(nested_list)
print("Flat list:", flat_list)

# Logic:
# 1. Go through each item.
# 2. If the item is a list, process it again.
# 3. Otherwise, add it to the result list.

# Explanation:
# This is a simple recursive flattening approach.
