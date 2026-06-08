"""Problem: Make change using greedy approach."""

# Problem:
# Use the fewest coins possible for a given amount.

amount = 87
coins = [50, 20, 10, 5, 2, 1]

# Solution:
used = {}

for coin in coins:
    count = amount // coin
    if count > 0:
        used[coin] = count
        amount %= coin

print("Coins used:", used)

# Logic:
# 1. Use the largest coin first.
# 2. Take as many as possible.
# 3. Move to smaller coins for the remainder.

# Explanation:
# Greedy works well for common coin systems like this one.
