"""Problem: Create a simple URL shortener."""

# Problem:
# Map long URLs to short codes.


class UrlShortener:
    def __init__(self):
        self.url_map = {}
        self.code_map = {}
        self.counter = 1

    def shorten(self, long_url):
        if long_url in self.url_map:
            return self.url_map[long_url]
        code = f"url{self.counter}"
        self.counter += 1
        self.url_map[long_url] = code
        self.code_map[code] = long_url
        return code

    def expand(self, code):
        return self.code_map.get(code, "Unknown code")


# Solution:
shortener = UrlShortener()
code = shortener.shorten("https://example.com/python/oop")
print("Short code:", code)
print("Long URL:", shortener.expand(code))

# Logic:
# 1. Save long URL to short code mapping.
# 2. Keep the reverse mapping too.
# 3. Return the same code if the URL already exists.

# Explanation:
# This is a tiny version of a real mapping service.
