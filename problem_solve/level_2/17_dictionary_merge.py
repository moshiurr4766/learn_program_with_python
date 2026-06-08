"""Problem: Merge two dictionaries."""

# Problem:
# Combine two dictionaries into one.

dict_one = {"a": 1, "b": 2}
dict_two = {"b": 5, "c": 3}

# Solution:
merged = dict_one.copy()

for key, value in dict_two.items():
    merged[key] = merged.get(key, 0) + value

print("Merged dictionary:", merged)

# Logic:
# 1. Start with the first dictionary.
# 2. Add values from the second dictionary.
# 3. If a key repeats, combine the values.

# Explanation:
# This version is useful when values should be added together.
