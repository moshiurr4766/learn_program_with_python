"""Linked list basics."""


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# Example 1: create nodes
first = Node(10)
second = Node(20)
third = Node(30)
first.next = second
second.next = third

# Example 2: traverse
current = first
while current:
    print(current.data)
    current = current.next

# Example 3: count nodes
current = first
count = 0
while current:
    count += 1
    current = current.next
print("Node count:", count)

# Logic:
# 1. Each node stores data and a link.
# 2. Start from the head node.
# 3. Follow next links until None.

# Explanation:
# Linked lists build on node connections instead of indexes.
