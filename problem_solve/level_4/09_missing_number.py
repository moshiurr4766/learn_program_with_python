"""Problem: Find the missing number in a sequence."""

# Problem:
# A list contains numbers from 1 to n with one missing.

numbers = [1, 2, 4, 5, 6]
expected_n = 6

# Solution:
expected_sum = expected_n * (expected_n + 1) // 2
actual_sum = sum(numbers)
missing = expected_sum - actual_sum

print("Missing number:", missing)

# Logic:
# 1. Find the expected sum from 1 to n.
# 2. Subtract the actual sum.
# 3. The difference is the missing number.

# Explanation:
# This is a fast arithmetic trick for sequence problems.
