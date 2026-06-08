"""Problem: Sort characters by frequency."""

# Problem:
# Rearrange characters so the most frequent come first.

text = "treehouse"

# Solution:
frequency = {}

for char in text:
    frequency[char] = frequency.get(char, 0) + 1

sorted_chars = sorted(frequency.items(), key=lambda item: item[1], reverse=True)
result = "".join(char * count for char, count in sorted_chars)

print("Frequency sorted string:", result)

# Logic:
# 1. Count each character.
# 2. Sort by count in descending order.
# 3. Rebuild the string from the sorted pairs.

# Explanation:
# Dictionaries plus sorting solve this neatly.
