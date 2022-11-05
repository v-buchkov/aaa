def selection_sort(array: list) -> None:
    for i in range(len(array)):
        min_index = i
        # Находим минимальный элемент и его индекс
        for j in range(i, len(array)):
            if array[j] < array[min_index]:
                min_index = j

        # Меняем местами
        array[i], array[min_index] = array[min_index], array[i]


to_sort = [4, 1, 14, 54, 5, 9, 66]
# Ничего не возвращает, только сортирует (in place)
# Не делает копию (чтобы экономить память)
# Если не экономить, то чистая функция (не меняет входных данных в отличие от in place функции)
selection_sort(to_sort)
print(to_sort)
