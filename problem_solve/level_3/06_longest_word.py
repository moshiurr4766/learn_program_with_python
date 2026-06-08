"""Problem: Find the longest word in a sentence."""

# Problem:
# Pick the longest word from a sentence.

sentence = "Python programming is fun and powerful"
words = sentence.split()

# Solution:
longest = max(words, key=len)
print("Longest word:", longest)

# Logic:
# 1. Split the sentence into words.
# 2. Use length as the comparison key.
# 3. Keep the word with the greatest length.

# Explanation:
# `max()` with `key=len` is a clean pattern for string tasks.
