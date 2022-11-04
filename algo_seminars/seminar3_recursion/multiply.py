def multiply(x: int, y: int):

    if y == 0:
        return 0

    return x + multiply(x, y - 1)


print(multiply(3, 2))
