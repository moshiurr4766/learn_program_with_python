"""Problem: Count word frequency in a sentence."""

# Problem:
# Count how many times each word appears.

sentence = "python is fun and python is powerful"
words = sentence.split()
frequency = {}

# Solution:
for word in words:
    frequency[word] = frequency.get(word, 0) + 1

print("Frequency:", frequency)

# Logic:
# 1. Split the sentence into words.
# 2. Use a dictionary for counts.
# 3. Increment the count for each word.

# Explanation:
# `get()` gives a clean way to update dictionary values.
