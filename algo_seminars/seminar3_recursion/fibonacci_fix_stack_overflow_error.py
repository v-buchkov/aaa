from functools import lru_cache
from sys import setrecursionlimit

setrecursionlimit(10000)


# Least recently used
# Need maxsize=3 to keep 2 and not delete required
@lru_cache(maxsize=3)
def fib(n):
    if n <= 1:
        return 1
    return fib(n - 1) + fib(n - 2)


print(fib(2000))
