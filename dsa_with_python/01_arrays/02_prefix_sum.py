"""Prefix sum examples."""

# Example 1: build prefix sums
numbers = [3, 1, 4, 1, 5]
prefix = [0]
for number in numbers:
    prefix.append(prefix[-1] + number)
print("Prefix:", prefix)

# Example 2: range sum query
left, right = 1, 3
range_sum = prefix[right + 1] - prefix[left]
print("Range sum 1..3:", range_sum)

# Example 3: count subarray sum pattern
target = 5
count = 0
for i in range(len(numbers)):
    for j in range(i, len(numbers)):
        if sum(numbers[i:j + 1]) == target:
            count += 1
print("Subarrays with sum 5:", count)

# Logic:
# 1. Prefix sums speed up repeated range queries.
# 2. A range sum is difference of two prefix values.
# 3. Brute-force subarray checks help show the problem clearly.

# Explanation:
# Prefix sums are useful when many sum queries are needed.
