"""Two pointer array examples."""

# Example 1: pair sum in sorted list
numbers = [1, 2, 4, 6, 8, 11]
target = 10
left = 0
right = len(numbers) - 1
pair = None

while left < right:
    current = numbers[left] + numbers[right]
    if current == target:
        pair = (numbers[left], numbers[right])
        break
    if current < target:
        left += 1
    else:
        right -= 1
print("Pair:", pair)

# Example 2: remove duplicates from sorted list
sorted_numbers = [1, 1, 2, 2, 3, 4, 4]
unique = []
for number in sorted_numbers:
    if not unique or unique[-1] != number:
        unique.append(number)
print("Unique:", unique)

# Logic:
# 1. Use two positions to scan from edges or through a sorted list.
# 2. Move pointers based on the condition.
# 3. This reduces repeated work.

# Explanation:
# Two pointers are common in sorted-array problems.
