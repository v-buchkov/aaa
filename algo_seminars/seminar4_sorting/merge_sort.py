def merge_sort(array: list):
    n = len(array)
    if n > 1:
        mid = int(n / 2)
        return merge(merge_sort(array[:mid]), merge_sort(array[mid:]))
    else:
        return array


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


to_sort = [4, 1, 14, 54, 5, 9, 66]
print(merge_sort(to_sort))
