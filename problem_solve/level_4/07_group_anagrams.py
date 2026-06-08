"""Problem: Group anagrams together."""

# Problem:
# Put words with the same letters into the same group.

words = ["eat", "tea", "tan", "ate", "nat", "bat"]

# Solution:
groups = {}

for word in words:
    key = "".join(sorted(word))
    groups.setdefault(key, []).append(word)

print("Grouped anagrams:", list(groups.values()))

# Logic:
# 1. Sort each word to make a common key.
# 2. Store words with the same key together.
# 3. Return the grouped lists.

# Explanation:
# Sorting a word gives a simple signature for anagrams.
