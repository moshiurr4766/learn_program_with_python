"""Problem: Print tree values level by level."""

# Problem:
# Traverse a binary tree using level order.

from collections import deque


class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def level_order(root):
    if not root:
        return []
    result = []
    queue = deque([root])

    while queue:
        node = queue.popleft()
        result.append(node.value)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return result


# Solution:
root = Node(1, Node(2, Node(4), Node(5)), Node(3))
print("Level order:", level_order(root))

# Logic:
# 1. Use a queue for breadth-first traversal.
# 2. Visit each node in arrival order.
# 3. Add child nodes to the queue.

# Explanation:
# Level order traversal is a standard queue-based tree pattern.
