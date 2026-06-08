"""Problem: Find the majority element."""

# Problem:
# Find the element that appears more than half the time.

numbers = [2, 2, 1, 2, 3, 2, 2]

# Solution:
candidate = None
count = 0

for number in numbers:
    if count == 0:
        candidate = number
    if number == candidate:
        count += 1
    else:
        count -= 1

print("Majority element:", candidate)

# Logic:
# 1. Keep one candidate.
# 2. Increase count when the item matches.
# 3. Reduce count when it does not.

# Explanation:
# This is the Boyer-Moore voting idea in simple form.
