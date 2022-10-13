# Complexity = len(arr) * const
from datetime import datetime


def timeit(func):
    def time(arr, item):
        start = datetime.now()
        func(arr, item)
        print(datetime.now() - start)
    return time


@timeit
def find(arr: list, item: int) -> bool:
    for el in arr:
        if el == item:  # complexity = const
            return True
    return False


find(list(range(10**6)), 10**7)

# Approx two times faster
find(list(range(10**6)), 5*10**5)
