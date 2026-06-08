"""Problem: Compress a string using run-length encoding."""

# Problem:
# Compress repeated characters into character-count pairs.

text = "aaabbcddd"

# Solution:
encoded = ""
count = 1

for i in range(1, len(text)):
    if text[i] == text[i - 1]:
        count += 1
    else:
        encoded += text[i - 1] + str(count)
        count = 1

encoded += text[-1] + str(count)
print("Encoded string:", encoded)

# Logic:
# 1. Count repeated consecutive letters.
# 2. Add the letter and count when the sequence changes.
# 3. Handle the last group at the end.

# Explanation:
# This is a useful text compression pattern.
