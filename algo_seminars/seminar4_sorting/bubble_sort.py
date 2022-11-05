def bubble_sort(array: list) -> None:
    for i in range(len(array)):
        order_errors = 0
        for j in range(len(array) - i - 1):  # i == 0 => j in (0, n - 1)
            if array[j] > array[j + 1]:
                array[j + 1], array[j] = array[j], array[j + 1]
                order_errors += 1

        if order_errors == 0:
            return


to_sort = [4, 1, 14, 54, 5, 9, 66]
# Ничего не возвращает, только сортирует (in place)
# Не делает копию (чтобы экономить память)
# Если не экономить, то чистая функция (не меняет входных данных в отличие от in place функции)
bubble_sort(to_sort)
print(to_sort)
