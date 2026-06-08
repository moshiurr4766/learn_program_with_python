"""Problem: Build a tiny LRU cache demo."""

# Problem:
# Store a small number of recent items and evict the oldest one.


class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}

    def put(self, key, value):
        if key in self.cache:
            del self.cache[key]
        elif len(self.cache) >= self.capacity:
            oldest_key = next(iter(self.cache))
            del self.cache[oldest_key]
        self.cache[key] = value

    def get(self, key):
        if key not in self.cache:
            return None
        value = self.cache[key]
        del self.cache[key]
        self.cache[key] = value
        return value


# Solution:
cache = LRUCache(2)
cache.put("a", 1)
cache.put("b", 2)
print(cache.get("a"))
cache.put("c", 3)
print(cache.cache)

# Logic:
# 1. Keep keys in insertion order.
# 2. Remove the oldest item when full.
# 3. Move used items to the end.

# Explanation:
# This is a simple idea behind least-recently-used caching.
