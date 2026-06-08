"""Problem: Print all prime numbers up to n."""

# Problem:
# Show every prime number from 2 to n.

n = 30

# Solution:
primes = []

for number in range(2, n + 1):
    is_prime = True
    for divisor in range(2, int(number ** 0.5) + 1):
        if number % divisor == 0:
            is_prime = False
            break
    if is_prime:
        primes.append(number)

print("Prime numbers:", primes)

# Logic:
# 1. Check each number from 2 to n.
# 2. Try dividing it up to its square root.
# 3. Keep the numbers that have no divisor.

# Explanation:
# This version is faster than checking every number below it.
