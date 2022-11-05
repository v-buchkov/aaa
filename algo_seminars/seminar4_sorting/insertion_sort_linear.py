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


to_sort = [4, 1, 14, 54, 5, 9, 66]
# Ничего не возвращает, только сортирует (in place)
# Не делает копию (чтобы экономить память)
# Если не экономить, то чистая функция (не меняет входных данных в отличие от in place функции)
insertion_sort(to_sort)
print(to_sort)
