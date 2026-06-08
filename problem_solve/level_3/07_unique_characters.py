"""Problem: Find unique characters in a string."""

# Problem:
# Show characters that appear only once.

text = "programming"

# Solution:
unique_chars = []

for char in text:
    if text.count(char) == 1:
        unique_chars.append(char)

print("Unique characters:", unique_chars)

# Logic:
# 1. Check each character.
# 2. Count how many times it appears.
# 3. Keep only the characters that appear once.

# Explanation:
# This is a simple frequency-style character problem.
