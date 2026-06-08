"""Dynamic programming examples."""

# Example 1: Fibonacci with memoization
memo = {0: 0, 1: 1}

def fib(n):
    if n not in memo:
        memo[n] = fib(n - 1) + fib(n - 2)
    return memo[n]

print("Fib 10:", fib(10))

# Example 2: climbing stairs
def ways(n):
    if n <= 2:
        return n
    a, b = 1, 2
    for _ in range(3, n + 1):
        a, b = b, a + b
    return b

print("Ways 5:", ways(5))

# Example 3: coin change count
coins = [1, 2, 5]
amount = 5
dp = [0] * (amount + 1)
dp[0] = 1
for coin in coins:
    for value in range(coin, amount + 1):
        dp[value] += dp[value - coin]
print("Ways to make 5:", dp[amount])

# Logic:
# 1. Save repeated results.
# 2. Build answers from smaller subproblems.
# 3. Reuse previous work instead of recomputing.

# Explanation:
# Dynamic programming is controlled reuse of earlier results.
