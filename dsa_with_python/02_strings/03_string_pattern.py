"""String pattern examples."""

# Example 1: frequency count
text = "programming"
frequency = {}
for char in text:
    frequency[char] = frequency.get(char, 0) + 1
print(frequency)

# Example 2: longest word
sentence = "Python is simple and powerful"
longest = max(sentence.split(), key=len)
print("Longest word:", longest)

# Example 3: substring count
source = "abababab"
pattern = "ab"
count = 0
for i in range(len(source) - len(pattern) + 1):
    if source[i:i + len(pattern)] == pattern:
        count += 1
print("Count:", count)

# Logic:
# 1. Count letters with a dictionary.
# 2. Use max with a custom key.
# 3. Slide a window across the string.

# Explanation:
# Pattern matching is a common text-processing idea.
