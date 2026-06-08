"""Linked list operations."""


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def to_list(self):
        values = []
        current = self.head
        while current:
            values.append(current.data)
            current = current.next
        return values


# Example 1: insert values
linked_list = LinkedList()
linked_list.insert_end(5)
linked_list.insert_end(15)
linked_list.insert_end(25)
print(linked_list.to_list())

# Example 2: search manually
target = 15
found = False
current = linked_list.head
while current:
    if current.data == target:
        found = True
        break
    current = current.next
print("Found:", found)

# Logic:
# 1. Add nodes by walking to the tail.
# 2. Convert the list by traversing nodes.
# 3. Search by checking each node one by one.

# Explanation:
# Linked list operations are pointer-based and sequential.
