import dis


def find(arr: list, item: int) -> bool:
    for el in arr:
        if el == item:
            return True
    return False


print(dis.dis(find))
