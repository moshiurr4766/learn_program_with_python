"""Problem: Check whether one string is a subsequence of another."""

# Problem:
# Decide if all characters of one string appear in order inside another.

text = "subsequence"
pattern = "sue"

# Solution:
index = 0

for char in text:
    if index < len(pattern) and char == pattern[index]:
        index += 1

print("Is subsequence:", index == len(pattern))

# Logic:
# 1. Scan the larger string once.
# 2. Move through the pattern only when characters match.
# 3. If all pattern characters are matched, it is a subsequence.

# Explanation:
# This is a common two-index string pattern.
