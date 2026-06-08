"""Problem: Rotate a list to the right."""

# Problem:
# Move the last k elements to the front.

numbers = [1, 2, 3, 4, 5]
k = 2

# Solution:
k = k % len(numbers)
rotated = numbers[-k:] + numbers[:-k]
print("Rotated list:", rotated)

# Logic:
# 1. Normalize k so it stays inside the list length.
# 2. Take the last k items.
# 3. Put them in front of the remaining items.

# Explanation:
# Slicing makes list rotation short and readable.
