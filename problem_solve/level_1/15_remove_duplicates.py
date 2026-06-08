"""Problem: Remove duplicates from a list."""

# Problem:
# Create a new list without repeated values.

numbers = [1, 2, 2, 3, 4, 4, 5]
unique_numbers = []

# Solution:
for number in numbers:
    if number not in unique_numbers:
        unique_numbers.append(number)

print("Unique list:", unique_numbers)

# Logic:
# 1. Keep an empty result list.
# 2. Add only values that are not already present.
# 3. Skip repeated items.

# Explanation:
# This preserves the original order of first appearance.
