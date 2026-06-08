"""Palindrome and anagram examples."""

# Example 1: palindrome check
text = "madam"
print("Palindrome:", text == text[::-1])

# Example 2: sentence palindrome ignoring spaces
sentence = "never odd or even"
clean = "".join(char.lower() for char in sentence if char.isalnum())
print("Sentence palindrome:", clean == clean[::-1])

# Example 3: anagram check
one = "listen"
two = "silent"
print("Anagram:", sorted(one) == sorted(two))

# Logic:
# 1. Clean text when needed.
# 2. Compare with reverse for palindrome.
# 3. Sort characters for anagram checks.

# Explanation:
# These problems train careful string comparison.
