"""Problem: Merge overlapping intervals."""

# Problem:
# Combine intervals that overlap.

intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]

# Solution:
intervals.sort()
merged = [intervals[0]]

for current in intervals[1:]:
    last = merged[-1]
    if current[0] <= last[1]:
        last[1] = max(last[1], current[1])
    else:
        merged.append(current)

print("Merged intervals:", merged)

# Logic:
# 1. Sort intervals by start value.
# 2. Compare each interval with the last merged one.
# 3. Merge if they overlap.

# Explanation:
# Sorting first makes overlapping checks much easier.
