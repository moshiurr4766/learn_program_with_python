"""Problem: Traverse a graph using BFS."""

# Problem:
# Visit graph nodes breadth-first.

from collections import deque

graph = {
    "A": ["B", "C"],
    "B": ["D"],
    "C": ["E"],
    "D": [],
    "E": []
}

# Solution:
queue = deque(["A"])
visited = {"A"}
order = []

while queue:
    node = queue.popleft()
    order.append(node)
    for neighbor in graph[node]:
        if neighbor not in visited:
            visited.add(neighbor)
            queue.append(neighbor)

print("BFS order:", order)

# Logic:
# 1. Use a queue for the frontier.
# 2. Visit nodes level by level.
# 3. Mark nodes so they are not repeated.

# Explanation:
# BFS is great for shortest-step style exploration.
