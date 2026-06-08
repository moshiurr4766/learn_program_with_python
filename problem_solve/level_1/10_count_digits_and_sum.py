"""Problem: Count digits and calculate digit sum."""

# Problem:
# Find how many digits a number has and also add its digits.

number = 9876
temp = number
digit_count = 0
digit_sum = 0

# Solution:
while temp > 0:
    digit = temp % 10
    digit_sum += digit
    digit_count += 1
    temp //= 10

print("Digit count:", digit_count)
print("Digit sum:", digit_sum)

# Logic:
# 1. Take one digit at a time.
# 2. Increase the count.
# 3. Add the digit to the running sum.

# Explanation:
# One loop can solve both tasks together.
