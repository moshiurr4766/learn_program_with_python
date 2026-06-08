"""Queue examples."""

from collections import deque

# Example 1: enqueue and dequeue
queue = deque()
queue.append("A")
queue.append("B")
queue.append("C")
print(queue.popleft())
print(queue)

# Example 2: BFS-style processing
items = deque([1, 2, 3])
order = []
while items:
    order.append(items.popleft())
print("Order:", order)

# Example 3: queue from two stacks idea
incoming = [1, 2, 3]
outgoing = []
while incoming:
    outgoing.append(incoming.pop())
print("Dequeued:", outgoing.pop())

# Logic:
# 1. Queue follows first-in, first-out behavior.
# 2. deque gives efficient front removal.
# 3. Many traversal problems naturally use a queue.

# Explanation:
# Queues are central to level-order traversal and scheduling.
