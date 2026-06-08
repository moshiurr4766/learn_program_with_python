"""Tree operations."""


class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def tree_sum(node):
    if not node:
        return 0
    return node.value + tree_sum(node.left) + tree_sum(node.right)


def tree_height(node):
    if not node:
        return 0
    return 1 + max(tree_height(node.left), tree_height(node.right))


root = Node(10, Node(5, Node(2), Node(7)), Node(15))

print("Sum:", tree_sum(root))
print("Height:", tree_height(root))

# Logic:
# 1. Recursively process each subtree.
# 2. Sum values or measure height.
# 3. Combine the results at the parent node.

# Explanation:
# Tree operations usually recurse over smaller tree parts.
