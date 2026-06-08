"""Set examples."""

# Example 1: duplicate detection
numbers = [1, 2, 3, 2, 5]
seen = set()
duplicate = False
for number in numbers:
    if number in seen:
        duplicate = True
        break
    seen.add(number)
print("Duplicate:", duplicate)

# Example 2: set operations
a = {1, 2, 3}
b = {3, 4, 5}
print("Union:", a | b)
print("Intersection:", a & b)

# Example 3: remove duplicates
items = [1, 1, 2, 3, 3, 4]
print(list(set(items)))

# Logic:
# 1. Sets store unique values.
# 2. Membership checks are fast.
# 3. Set operations help with overlaps and differences.

# Explanation:
# Sets are the right tool for uniqueness-based problems.
