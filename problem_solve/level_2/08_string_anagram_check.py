"""Problem: Check whether two strings are anagrams."""

# Problem:
# Two strings are anagrams if they contain the same letters in a different order.

text_one = "listen"
text_two = "silent"

# Solution:
if sorted(text_one) == sorted(text_two):
    print("The strings are anagrams.")
else:
    print("The strings are not anagrams.")

# Logic:
# 1. Sort both strings.
# 2. Compare the sorted versions.
# 3. If they match, the strings are anagrams.

# Explanation:
# Sorting is a simple way to compare letter order fairly.
