"""Graph traversal examples."""

from collections import deque

graph = {
    "A": ["B", "C"],
    "B": ["D"],
    "C": ["E"],
    "D": [],
    "E": []
}

# Example 1: DFS
def dfs(node, visited, order):
    visited.add(node)
    order.append(node)
    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs(neighbor, visited, order)

dfs_order = []
dfs("A", set(), dfs_order)
print("DFS:", dfs_order)

# Example 2: BFS
queue = deque(["A"])
visited = {"A"}
bfs_order = []
while queue:
    node = queue.popleft()
    bfs_order.append(node)
    for neighbor in graph[node]:
        if neighbor not in visited:
            visited.add(neighbor)
            queue.append(neighbor)
print("BFS:", bfs_order)

# Logic:
# 1. DFS uses recursion or a stack.
# 2. BFS uses a queue.
# 3. Visited tracking prevents repeats.

# Explanation:
# Graph traversal is a base idea for many graph problems.
