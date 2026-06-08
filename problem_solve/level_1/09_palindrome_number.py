"""Problem: Check whether a number is a palindrome."""

# Problem:
# A palindrome number reads the same forward and backward.

number = 121
temp = number
reversed_number = 0

# Solution:
while temp > 0:
    digit = temp % 10
    reversed_number = reversed_number * 10 + digit
    temp //= 10

if number == reversed_number:
    print(number, "is a palindrome")
else:
    print(number, "is not a palindrome")

# Logic:
# 1. Reverse the digits of the number.
# 2. Compare the original number with the reversed one.
# 3. If both are equal, it is a palindrome.

# Explanation:
# The pattern is the same in both directions.
