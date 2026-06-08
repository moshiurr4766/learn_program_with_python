"""Problem: Count vowels in a string."""

# Problem:
# Count how many vowels are in a given string.

text = "Hello Python World"
vowels = "aeiouAEIOU"
count = 0

# Solution:
for char in text:
    if char in vowels:
        count += 1

print("Vowel count:", count)

# Logic:
# 1. Loop through each character.
# 2. Check whether it is a vowel.
# 3. Increase count when a vowel is found.

# Explanation:
# Membership checking with `in` keeps the code simple.
