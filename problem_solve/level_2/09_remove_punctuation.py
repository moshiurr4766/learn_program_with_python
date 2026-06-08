"""Problem: Remove punctuation from a string."""

# Problem:
# Remove punctuation marks and keep only letters, numbers, and spaces.

text = "Hello, Python! Are you ready?"
clean_text = ""

# Solution:
for char in text:
    if char.isalnum() or char.isspace():
        clean_text += char

print(clean_text)

# Logic:
# 1. Look at each character.
# 2. Keep letters, digits, and spaces.
# 3. Skip punctuation marks.

# Explanation:
# Character checks are useful for text cleaning.
