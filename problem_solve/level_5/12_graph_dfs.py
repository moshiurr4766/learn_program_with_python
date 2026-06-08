"""Problem: Traverse a graph using DFS."""

# Problem:
# Visit graph nodes depth-first.

graph = {
    "A": ["B", "C"],
    "B": ["D"],
    "C": ["E"],
    "D": [],
    "E": []
}


def dfs(node, visited):
    visited.add(node)
    order.append(node)
    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs(neighbor, visited)


# Solution:
visited = set()
order = []
dfs("A", visited)
print("DFS order:", order)

# Logic:
# 1. Mark the current node visited.
# 2. Recurse into each unvisited neighbor.
# 3. Collect the traversal order.

# Explanation:
# DFS goes deep before it comes back up.
