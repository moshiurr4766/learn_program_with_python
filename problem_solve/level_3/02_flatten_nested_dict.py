"""Problem: Flatten a nested dictionary."""

# Problem:
# Convert a nested dictionary into dot-separated keys.

nested = {
    "user": {
        "name": "Moshiur",
        "contact": {
            "email": "moshiur@example.com"
        }
    }
}

flat = {}


def flatten_dict(data, parent_key=""):
    for key, value in data.items():
        new_key = f"{parent_key}.{key}" if parent_key else key
        if isinstance(value, dict):
            flatten_dict(value, new_key)
        else:
            flat[new_key] = value


# Solution:
flatten_dict(nested)
print(flat)

# Logic:
# 1. Walk through each dictionary item.
# 2. Build a full key path using dots.
# 3. Recurse again if the value is another dictionary.

# Explanation:
# This is useful when nested data must be stored in a simple format.
