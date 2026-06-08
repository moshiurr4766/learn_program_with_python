"""Problem: Answer range sum queries using prefix sums."""

# Problem:
# Quickly find sums for multiple subranges.

numbers = [3, 1, 4, 1, 5, 9, 2]
queries = [(0, 2), (2, 5), (1, 6)]

# Solution:
prefix = [0]
for number in numbers:
    prefix.append(prefix[-1] + number)

for left, right in queries:
    range_sum = prefix[right + 1] - prefix[left]
    print(f"Sum {left}-{right}:", range_sum)

# Logic:
# 1. Build a prefix sum array.
# 2. Each range sum is a subtraction of two prefix values.
# 3. This avoids re-summing the same items repeatedly.

# Explanation:
# Prefix sums are useful when there are many sum queries.
