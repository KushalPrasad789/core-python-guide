from functools import lru_cache

# Use @lru_cache to optimize a recursive factorial function.

@lru_cache(maxsize=None)
def factorial(n):
    if n < 2:
        return 1
    return n * factorial(n - 1)

# Example usage
print(factorial(5))  # Output: 120