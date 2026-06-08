"""Problem: Check whether a sentence is a palindrome."""

# Problem:
# Ignore spaces and case when checking a palindrome sentence.

text = "Never odd or even"

# Solution:
clean_text = ""

for char in text:
    if char.isalnum():
        clean_text += char.lower()

if clean_text == clean_text[::-1]:
    print("The sentence is a palindrome.")
else:
    print("The sentence is not a palindrome.")

# Logic:
# 1. Remove spaces and punctuation.
# 2. Convert everything to lowercase.
# 3. Compare the string with its reverse.

# Explanation:
# Normalizing text is important in string problems.
