"""Search patterns in strings."""

# Example 1: find a substring
text = "python is powerful and python is easy"
print("python" in text)

# Example 2: find first occurrence
index = text.find("python")
print("First index:", index)

# Example 3: manual pattern search
pattern = "easy"
found = False
for i in range(len(text) - len(pattern) + 1):
    if text[i:i + len(pattern)] == pattern:
        found = True
        break
print("Manual search:", found)

# Logic:
# 1. Strings can be searched directly with `in`.
# 2. `find()` returns the first index.
# 3. Manual slicing shows the real search process.

# Explanation:
# String searching is a simple gateway to pattern matching.
