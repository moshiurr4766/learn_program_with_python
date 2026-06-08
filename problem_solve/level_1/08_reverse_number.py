"""Problem: Reverse a number."""

# Problem:
# Reverse the digits of a number.

number = 12345
reversed_number = 0

# Solution:
while number > 0:
    digit = number % 10
    reversed_number = reversed_number * 10 + digit
    number //= 10

print("Reversed number:", reversed_number)

# Logic:
# 1. Take the last digit using % 10.
# 2. Add it to the reversed result.
# 3. Remove the last digit using integer division.

# Explanation:
# This builds the reverse digit by digit.
