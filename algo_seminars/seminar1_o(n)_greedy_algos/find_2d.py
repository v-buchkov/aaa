import dis
from typing import List
import timeit


# Complexity = len(arr) * len(row) * const
def find_2d(arr: List[List[int]], item: int) -> bool:
    for row in arr:
        for el in row:
            if el == item:
                return True
    return False


dis.dis(find_2d)
