import random


def median_3(a, b, c):
    return max(min(a, b), min(b, c), min(a, c))


def median_3_another(a, b, c):
    return min(max(a, b), max(b, c), max(a, c))


def partition(array: list, l: int, r: int):
    # pivot = array[l]  # неэффективный, если будет неравномерное разбиение
    # pivot = array[random.randint(l, r - 1)]  # самый простой из более эффективных
    pivot = median_3(array[l], array[int((l + r) / 2)], array[r])
    while l <= r:
        while array[l] < pivot:
            l += 1

        while array[r] > pivot:
            r -= 1

        if l <= r:
            array[l], array[r] = array[r], array[l]
            l += 1
            r -= 1

    return l, r


def quick_sort(array: list, l: int, r: int):
    if l < r:
        new_l, new_r = partition(array, l, r)
        quick_sort(array, l, new_r)
        quick_sort(array, new_l, r)


to_sort = [4, 1, 14, 54, 5, 9, 66]
# to_sort = [6, 7, 6, 6, 1, 9]
# Ничего не возвращает, только сортирует (in place)
# Не делает копию (чтобы экономить память)
# Если не экономить, то чистая функция (не меняет входных данных в отличие от in place функции)
quick_sort(to_sort, l=0, r=len(to_sort) - 1)
print(to_sort)
