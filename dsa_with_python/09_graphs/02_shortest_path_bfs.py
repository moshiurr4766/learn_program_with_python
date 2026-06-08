"""Shortest path example using BFS."""

from collections import deque

graph = {
    "A": ["B", "C"],
    "B": ["D"],
    "C": ["D", "E"],
    "D": ["F"],
    "E": ["F"],
    "F": []
}


def shortest_path(start, goal):
    queue = deque([(start, [start])])
    visited = {start}
    while queue:
        node, path = queue.popleft()
        if node == goal:
            return path
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, path + [neighbor]))
    return None


print(shortest_path("A", "F"))

# Logic:
# 1. Store the current node and the path to it.
# 2. Expand neighbors level by level.
# 3. Return the first path that reaches the goal.

# Explanation:
# BFS finds shortest paths in unweighted graphs.
