"""Problem: Check whether a binary tree is balanced."""

# Problem:
# Decide if a tree is height-balanced.


class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def height(node):
    if node is None:
        return 0
    left_height = height(node.left)
    right_height = height(node.right)
    return 1 + max(left_height, right_height)


def is_balanced(node):
    if node is None:
        return True
    left_height = height(node.left)
    right_height = height(node.right)
    if abs(left_height - right_height) > 1:
        return False
    return is_balanced(node.left) and is_balanced(node.right)


# Solution:
root = Node(1, Node(2, Node(3)), Node(4))
print("Balanced:", is_balanced(root))

# Logic:
# 1. Find the height of each subtree.
# 2. Compare the height difference.
# 3. Repeat for all nodes.

# Explanation:
# Trees are easier to reason about when split into small recursive checks.
