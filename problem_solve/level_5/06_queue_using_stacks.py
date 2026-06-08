"""Problem: Implement a queue using two stacks."""

# Problem:
# Create queue behavior using stacks only.


class QueueUsingStacks:
    def __init__(self):
        self.input_stack = []
        self.output_stack = []

    def enqueue(self, value):
        self.input_stack.append(value)

    def dequeue(self):
        if not self.output_stack:
            while self.input_stack:
                self.output_stack.append(self.input_stack.pop())
        if not self.output_stack:
            return None
        return self.output_stack.pop()


# Solution:
queue = QueueUsingStacks()
queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)
print(queue.dequeue())
print(queue.dequeue())

# Logic:
# 1. Push new items into one stack.
# 2. Move them to the other stack only when needed.
# 3. Pop from the output stack like a real queue.

# Explanation:
# This is a good example of using one data structure to simulate another.
