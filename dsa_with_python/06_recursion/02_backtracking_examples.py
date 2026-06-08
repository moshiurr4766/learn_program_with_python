"""Backtracking examples."""

# Example 1: subsets
def subsets(items):
    result = [[]]
    for item in items:
        result += [current + [item] for current in result]
    return result

print(subsets([1, 2, 3]))

# Example 2: permutations
def permute(items):
    if len(items) <= 1:
        return [items]
    result = []
    for i in range(len(items)):
        remaining = items[:i] + items[i + 1:]
        for p in permute(remaining):
            result.append([items[i]] + p)
    return result

print(permute([1, 2, 3]))

# Logic:
# 1. Try a choice.
# 2. Recurse on the remaining problem.
# 3. Collect all valid outcomes.

# Explanation:
# Backtracking is recursion plus systematic exploration.
