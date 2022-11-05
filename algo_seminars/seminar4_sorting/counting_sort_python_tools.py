from random import sample
from collections import Counter


def counting_sort(array: list):
    c = Counter(array)
    output_array = []
    for v in sorted(c):
        output_array.extend([v for _ in range(c[v])])
    return output_array


to_sort = list(sample(range(0, 1000), 1000))
counting_sort(to_sort)
print(counting_sort(to_sort))
