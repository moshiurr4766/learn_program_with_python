"""Hash map examples."""

# Example 1: frequency count
text = "banana"
count = {}
for char in text:
    count[char] = count.get(char, 0) + 1
print(count)

# Example 2: first non-repeating character
for char in text:
    if count[char] == 1:
        print("First unique:", char)
        break

# Example 3: grouping words by length
words = ["cat", "dog", "lion", "ant"]
groups = {}
for word in words:
    groups.setdefault(len(word), []).append(word)
print(groups)

# Logic:
# 1. Dictionaries store key-value pairs.
# 2. They work well for counting and lookup.
# 3. Grouping is a common hash map pattern.

# Explanation:
# Hash maps solve many frequency and grouping tasks.
