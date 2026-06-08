"""String basics with multiple examples."""

# Example 1: indexing and slicing
text = "Python"
print(text[0])
print(text[1:4])
print(text[::-1])

# Example 2: split and join
sentence = "data structures and algorithms"
words = sentence.split()
print(words)
print("-".join(words))

# Example 3: replace and count
message = "hello world hello"
print(message.count("hello"))
print(message.replace("world", "python"))

# Logic:
# 1. Strings support slicing and indexing.
# 2. Split breaks text into parts, join combines them.
# 3. String methods solve many text problems.

# Explanation:
# Text manipulation is a core skill in DSA.
