def fib(n, memo: dict):

    if n in memo:
        return memo[n]

    if n <= 1:
        return 1

    ans = fib(n - 1, memo) + fib(n - 2, memo)
    memo[n] = ans
    return ans


memo = {}
print(fib(100, memo))
# Fast, but not optimal by memory (O(n) by memory)
