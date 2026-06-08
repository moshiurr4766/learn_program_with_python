"""Problem: Find the maximum subarray sum."""

# Problem:
# Find the largest sum of any contiguous subarray.

numbers = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

# Solution:
current_sum = numbers[0]
best_sum = numbers[0]

for number in numbers[1:]:
    current_sum = max(number, current_sum + number)
    best_sum = max(best_sum, current_sum)

print("Maximum subarray sum:", best_sum)

# Logic:
# 1. Track the best sum ending at the current position.
# 2. Decide whether to extend or restart the subarray.
# 3. Keep the global best value.

# Explanation:
# Kadane's algorithm is a classic dynamic programming pattern.
