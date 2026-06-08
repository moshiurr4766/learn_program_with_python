"""Problem: Find the top k frequent elements."""

# Problem:
# Return the most common elements in a list.

numbers = [1, 1, 1, 2, 2, 3, 4, 4, 4, 4]
k = 2

# Solution:
frequency = {}
for number in numbers:
    frequency[number] = frequency.get(number, 0) + 1

top_k = sorted(frequency.items(), key=lambda item: item[1], reverse=True)[:k]
print("Top frequent elements:", [item[0] for item in top_k])

# Logic:
# 1. Count how often each value appears.
# 2. Sort by frequency.
# 3. Take the first k items.

# Explanation:
# This combines dictionaries with sorting.
