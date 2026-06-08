"""Problem: Check whether brackets are balanced."""

# Problem:
# Validate a string containing brackets.

text = "({[]})"
stack = []
pairs = {")": "(", "]": "[", "}": "{"}
is_valid = True

# Solution:
for char in text:
    if char in "([{":
        stack.append(char)
    elif char in ")]}":
        if not stack or stack.pop() != pairs[char]:
            is_valid = False
            break

if is_valid and not stack:
    print("Balanced brackets")
else:
    print("Not balanced")

# Logic:
# 1. Push opening brackets onto a stack.
# 2. Match each closing bracket with the last opening one.
# 3. Fail if the order does not match.

# Explanation:
# This is a classic stack problem.
