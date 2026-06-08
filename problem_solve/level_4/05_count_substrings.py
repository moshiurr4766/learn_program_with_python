"""Problem: Count occurrences of a substring."""

# Problem:
# Count how many times a small string appears in a bigger string.

text = "abababab"
pattern = "ab"


def count_substrings(sentence, word):
    count = 0
    for i in range(len(sentence) - len(word) + 1):
        if sentence[i:i + len(word)] == word:
            count += 1
    return count


# Solution:
print("Count:", count_substrings(text, pattern))

# Logic:
# 1. Look at every possible slice.
# 2. Compare the slice with the pattern.
# 3. Increase count when they match.

# Explanation:
# Sliding window style checks are common in string problems.
