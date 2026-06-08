"""Problem: Count words from text content."""

# Problem:
# Count words in a block of text.

content = """
Python is simple.
Python is powerful.
Python is readable.
"""

# Solution:
words = content.lower().split()
counts = {}

for word in words:
    cleaned = word.strip(".,!?:;")
    counts[cleaned] = counts.get(cleaned, 0) + 1

print("Word counts:", counts)

# Logic:
# 1. Convert text to lowercase.
# 2. Split it into words.
# 3. Clean punctuation and count each word.

# Explanation:
# This models the logic used in basic file text analysis.
