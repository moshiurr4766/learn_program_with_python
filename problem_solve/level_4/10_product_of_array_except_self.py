"""Problem: Product of array except self."""

# Problem:
# Build a list where each position is the product of all other values.

numbers = [1, 2, 3, 4]

# Solution:
prefix = [1] * len(numbers)
suffix = [1] * len(numbers)
result = [1] * len(numbers)

for i in range(1, len(numbers)):
    prefix[i] = prefix[i - 1] * numbers[i - 1]

for i in range(len(numbers) - 2, -1, -1):
    suffix[i] = suffix[i + 1] * numbers[i + 1]

for i in range(len(numbers)):
    result[i] = prefix[i] * suffix[i]

print("Result:", result)

# Logic:
# 1. Store products from the left.
# 2. Store products from the right.
# 3. Multiply the matching left and right values.

# Explanation:
# Prefix and suffix arrays solve this without division.
