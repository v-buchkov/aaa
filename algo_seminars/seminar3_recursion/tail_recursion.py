from dis import dis


# Not tail recursive => !!! keep all the stack to call the function
def factorial(n: int):
    if n == 0:
        return 1
    return n * factorial(n - 1)


# print(dis(factorial))

# Tail recursive => add accrual parameters
def factorial_tail(n: int, acc: int = 1):
    if n == 0:
        return acc
    return factorial_tail(n - 1, acc * n)


# print(dis(factorial_tail))

# print(factorial(5))
# print(factorial_tail(5))

"""
How it works:
factorial_tail(5, 1) -> factorial_tail(4, 5) -> factorial_tail(3, 20) -> factorial_tail(2, 60) -> factorial_tail(1, 120)

Does not need to keep the whole stack (accrued parameter does that)

Compilators (not Python) will transfer into loop

Widely applied in functional programming
"""
