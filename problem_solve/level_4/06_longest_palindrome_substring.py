"""Problem: Find the longest palindromic substring."""

# Problem:
# Find the longest substring that reads the same backward.

text = "babad"


def expand(text, left, right):
    while left >= 0 and right < len(text) and text[left] == text[right]:
        left -= 1
        right += 1
    return text[left + 1:right]


def longest_palindrome(text):
    best = ""
    for i in range(len(text)):
        odd = expand(text, i, i)
        even = expand(text, i, i + 1)
        best = max(best, odd, even, key=len)
    return best


# Solution:
print("Longest palindrome:", longest_palindrome(text))

# Logic:
# 1. Treat each position as the center.
# 2. Expand outward while characters match.
# 3. Keep the longest result.

# Explanation:
# This is a classic expand-around-center technique.
