"""Problem: Build a stack that can return the minimum value."""

# Problem:
# Support push, pop, and minimum lookup in constant time.


class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, value):
        self.stack.append(value)
        if not self.min_stack or value <= self.min_stack[-1]:
            self.min_stack.append(value)

    def pop(self):
        if not self.stack:
            return None
        value = self.stack.pop()
        if value == self.min_stack[-1]:
            self.min_stack.pop()
        return value

    def get_min(self):
        return self.min_stack[-1] if self.min_stack else None


# Solution:
stack = MinStack()
stack.push(5)
stack.push(2)
stack.push(8)
print("Min:", stack.get_min())
stack.pop()
print("Min after pop:", stack.get_min())

# Logic:
# 1. Keep a normal stack.
# 2. Keep another stack for minimum values.
# 3. Use the second stack to read the minimum quickly.

# Explanation:
# Extra storage can make minimum lookup very fast.
