"""Problem: Check whether a number is an Armstrong number."""

# Problem:
# An Armstrong number equals the sum of its digits raised to the power of the number of digits.

number = 153
temp = number
digits = len(str(number))
total = 0

# Solution:
while temp > 0:
    digit = temp % 10
    total += digit ** digits
    temp //= 10

if total == number:
    print(number, "is an Armstrong number")
else:
    print(number, "is not an Armstrong number")

# Logic:
# 1. Count the digits.
# 2. Raise each digit to that power.
# 3. Add the results and compare with the original number.

# Explanation:
# Armstrong problems are a good step beyond palindrome logic.
