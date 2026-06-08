"""Problem: Find the k largest numbers."""

# Problem:
# Return the largest k values from a list.

import heapq

numbers = [7, 1, 9, 3, 12, 6, 10]
k = 3

# Solution:
largest = heapq.nlargest(k, numbers)
print("Largest values:", largest)

# Logic:
# 1. Use a heap-based helper.
# 2. Ask for the top k items.
# 3. Return them in descending order.

# Explanation:
# Heap tools are efficient for repeated top-k style queries.
