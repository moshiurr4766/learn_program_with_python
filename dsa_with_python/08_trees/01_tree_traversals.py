"""Tree traversal examples."""


class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


root = Node(1, Node(2, Node(4), Node(5)), Node(3))

# Example 1: inorder
def inorder(node):
    if node:
        inorder(node.left)
        print(node.value, end=" ")
        inorder(node.right)

print("Inorder:")
inorder(root)
print()

# Example 2: preorder
def preorder(node):
    if node:
        print(node.value, end=" ")
        preorder(node.left)
        preorder(node.right)

print("Preorder:")
preorder(root)
print()

# Example 3: postorder
def postorder(node):
    if node:
        postorder(node.left)
        postorder(node.right)
        print(node.value, end=" ")

print("Postorder:")
postorder(root)
print()

# Logic:
# 1. Traversal order changes when we visit the node.
# 2. Recursion fits tree structure naturally.
# 3. Left and right children are processed in a chosen order.

# Explanation:
# Tree traversals are the heart of binary tree work.
