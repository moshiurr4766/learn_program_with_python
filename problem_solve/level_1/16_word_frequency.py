"""Problem: Count word frequency."""

# Problem:
# Find how many times each word appears in a sentence.

sentence = "python is easy and python is powerful"
words = sentence.split()
frequency = {}

# Solution:
for word in words:
    if word in frequency:
        frequency[word] += 1
    else:
        frequency[word] = 1

print("Word frequency:", frequency)

# Logic:
# 1. Split the sentence into words.
# 2. Use a dictionary to count each word.
# 3. Update the count every time the word appears.

# Explanation:
# Dictionaries are perfect for frequency counting.
