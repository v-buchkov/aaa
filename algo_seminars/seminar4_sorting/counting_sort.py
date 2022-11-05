from random import sample


def counting_sort(array: list):
    output_array = []
    c = [0 for _ in range(max(array) + 1)]
    for v in array:
        c[v] += 1

    for i, v in enumerate(c):
        if v > 0:
            output_array.extend([i for _ in range(v)])
    return output_array


to_sort = list(sample(range(0, 1000), 1000))
counting_sort(to_sort)
print(counting_sort(to_sort))
