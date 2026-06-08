"""Stack examples."""

# Example 1: push and pop
stack = []
stack.append(10)
stack.append(20)
stack.append(30)
print(stack.pop())
print(stack)

# Example 2: balanced parentheses
text = "({[]})"
pairs = {")": "(", "]": "[", "}": "{"}
temp = []
valid = True
for char in text:
    if char in "([{":
        temp.append(char)
    else:
        if not temp or temp.pop() != pairs[char]:
            valid = False
            break
print("Balanced:", valid and not temp)

# Example 3: reverse string
word = "python"
print("".join(reversed(word)))

# Logic:
# 1. Stack follows last-in, first-out behavior.
# 2. Matching brackets is a classic stack use case.
# 3. Reversal is easy with stack behavior.

# Explanation:
# Stacks are simple but very powerful.
