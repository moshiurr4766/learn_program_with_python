"""Problem: Find common elements in two lists."""

# Problem:
# Find items that appear in both lists.

list_one = [1, 2, 3, 4, 5]
list_two = [4, 5, 6, 7, 8]

# Solution:
common = []

for item in list_one:
    if item in list_two:
        common.append(item)

print("Common elements:", common)

# Logic:
# 1. Check each item in the first list.
# 2. See whether it exists in the second list.
# 3. Collect matching values.

# Explanation:
# Membership checking helps solve overlap problems easily.
