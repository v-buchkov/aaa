import dis


# Complexity = len(arr) * const
def find(arr: list, item: int) -> bool:
    for el in arr:
        if el == item:  # complexity = const
            return True
    return False


dis.dis(find)
