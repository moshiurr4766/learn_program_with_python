"""Problem: Check whether a number is prime."""

# Problem:
# A prime number has only two divisors: 1 and itself.

number = 29

# Solution:
is_prime = True

if number < 2:
    is_prime = False
else:
    for i in range(2, number):
        if number % i == 0:
            is_prime = False
            break

if is_prime:
    print(number, "is prime")
else:
    print(number, "is not prime")

# Logic:
# 1. Numbers below 2 are not prime.
# 2. Check divisibility from 2 to n-1.
# 3. If any divisor exists, the number is not prime.

# Explanation:
# A prime number cannot be divided evenly by other numbers.
