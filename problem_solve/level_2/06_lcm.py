"""Problem: Find the LCM of two numbers."""

# Problem:
# Find the least common multiple.

a = 12
b = 15

# Solution:
gcd_a, gcd_b = a, b

while gcd_b != 0:
    gcd_a, gcd_b = gcd_b, gcd_a % gcd_b

gcd = gcd_a
lcm = (a * b) // gcd

print("LCM:", lcm)

# Logic:
# 1. First find the GCD.
# 2. Use the formula LCM = (a * b) / GCD.
# 3. Use integer division for the result.

# Explanation:
# GCD and LCM are strongly connected.
