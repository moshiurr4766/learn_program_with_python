"""Problem: Detect duplicates using a set."""

# Problem:
# Check whether a list contains duplicate values.

numbers = [4, 7, 2, 9, 7]

# Solution:
seen = set()
has_duplicate = False

for number in numbers:
    if number in seen:
        has_duplicate = True
        break
    seen.add(number)

print("Has duplicate:", has_duplicate)

# Logic:
# 1. Keep a set of seen values.
# 2. If a value appears again, it is a duplicate.
# 3. Stop early once a duplicate is found.

# Explanation:
# Sets make duplicate detection very fast.
