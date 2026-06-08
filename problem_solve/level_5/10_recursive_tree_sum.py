"""Problem: Sum all values in a binary tree."""

# Problem:
# Add every node value in a tree.


class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def tree_sum(node):
    if node is None:
        return 0
    return node.value + tree_sum(node.left) + tree_sum(node.right)


# Solution:
root = Node(5, Node(3, Node(1), Node(4)), Node(8))
print("Tree sum:", tree_sum(root))

# Logic:
# 1. Return 0 for empty nodes.
# 2. Add the current value.
# 3. Recurse into both children.

# Explanation:
# Tree recursion naturally splits the problem into smaller pieces.
