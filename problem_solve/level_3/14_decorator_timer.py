"""Problem: Measure function time using a decorator."""

# Problem:
# Wrap a function so it prints timing information.

import time


def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} took {end - start:.6f} seconds")
        return result

    return wrapper


@timer
def greet(name):
    return f"Hello, {name}"


# Solution:
print(greet("Moshiur"))

# Logic:
# 1. A decorator receives a function.
# 2. The wrapper runs code before and after it.
# 3. The original result is returned unchanged.

# Explanation:
# Decorators help add behavior without changing the original function.
