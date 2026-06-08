"""Problem: Perform set operations."""

# Problem:
# Find union, intersection, and difference.

set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}

# Solution:
print("Union:", set_a | set_b)
print("Intersection:", set_a & set_b)
print("Difference A-B:", set_a - set_b)

# Logic:
# 1. Union combines all values.
# 2. Intersection keeps common values.
# 3. Difference keeps items only in the first set.

# Explanation:
# Sets are perfect for membership-based operations.
