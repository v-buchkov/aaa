from random import sample


def insertion_sort(array: list) -> None:

    for i in range(1, len(array)):
        key = array[i]
        # Начинаем с конца отсортированного
        j = i - 1

        # Linear, better use binary
        while j >= 0 and key < array[j]:
            # "Просыпается" через все элементы, которые больше
            # Можно не менять каждый раз, а пройтись и найти правильную позицию
            array[j + 1] = array[j]
            j = j - 1

        array[j + 1] = key


def merge(array1: list, array2: list):
    output_list = []
    c_1, c_2 = 0, 0
    n_1, n_2 = len(array1), len(array2)
    while c_1 < n_1 or c_2 < n_2:
        if c_1 >= n_1:
            output_list.append(array2[c_2])
            c_2 += 1
            continue

        if c_2 >= n_2:
            output_list.append(array1[c_1])
            c_1 += 1
            continue

        if array1[c_1] <= array2[c_2]:
            output_list.append(array1[c_1])
            c_1 += 1
        else:
            output_list.append(array2[c_2])
            c_2 += 1
    return output_list


def merge_sort(array: list):
    n = len(array)
    if n > 1:
        mid = int(n / 2)
        return merge(merge_sort(array[:mid]), merge_sort(array[mid:]))
    else:
        return array


def hybrid_sort(array: list):
    n = len(array)
    if n <= 64:
        # Меняется только база рекурсии
        insertion_sort(array)
        return

    mid = int(n / 2)
    return merge(merge_sort(array[:mid]), merge_sort(array[mid:]))


to_sort = list(sample(range(0, 1000), 1000))
hybrid_sort(to_sort)
print(hybrid_sort(to_sort))
