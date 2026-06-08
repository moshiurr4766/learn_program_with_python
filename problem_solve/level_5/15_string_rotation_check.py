"""Problem: Check whether one string is a rotation of another."""

# Problem:
# Determine if one string is a rotated version of another.

text_one = "waterbottle"
text_two = "erbottlewat"

# Solution:
is_rotation = len(text_one) == len(text_two) and text_two in (text_one + text_one)
print("Is rotation:", is_rotation)

# Logic:
# 1. Both strings must have the same length.
# 2. Join the first string with itself.
# 3. Check whether the second string appears inside it.

# Explanation:
# String rotation often has a very compact solution.
