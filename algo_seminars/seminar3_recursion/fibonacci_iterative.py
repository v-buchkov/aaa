def fib(n):
    fib0, fib1 = 1, 1
    for i in range(n):
        fib0, fib1 = fib1, fib1 + fib0
    return fib0


print(fib(100))
