"""Greedy examples."""

# Example 1: activity selection
activities = [(1, 2), (3, 4), (0, 6), (5, 7), (8, 9)]
activities.sort(key=lambda item: item[1])
selected = []
last_end = -1
for start, end in activities:
    if start >= last_end:
        selected.append((start, end))
        last_end = end
print("Selected activities:", selected)

# Example 2: coin change
amount = 87
coins = [50, 20, 10, 5, 2, 1]
used = {}
for coin in coins:
    count = amount // coin
    if count:
        used[coin] = count
        amount %= coin
print("Coins:", used)

# Example 3: minimum platforms style idea
arrivals = [900, 940, 950, 1100]
departures = [910, 1200, 1120, 1130]
arrivals.sort()
departures.sort()
print("Arrivals:", arrivals)
print("Departures:", departures)

# Logic:
# 1. Choose the locally best option first.
# 2. Sort when ordering helps the decision.
# 3. Keep the state small and simple.

# Explanation:
# Greedy methods work when local choices lead to a good global result.
