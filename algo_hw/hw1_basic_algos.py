""" Task 1 """
#
#
# def is_palindrome(a: int) -> bool:
#
#     int_parts = []
#     i = 0
#
#     while a // (10 ** i) > 0:
#         int_parts.append(a // (10 ** i) % 10)
#         i += 1
#     int_parts.reverse()
#     a_backwards = sum([int_parts[i] * (10 ** i) for i in range(len(int_parts))])
#
#     if a_backwards == a:
#         return True
#     else:
#         return False
#
#
# def solution():
#     a = int(input())
#     c = is_palindrome(a)
#     print(c)
#
#
# solution()

""" Task 2 """
# from math import factorial, log2, sqrt
#
# n = 10000
#
# print(1.00001 ** n - 1.00001 ** (n - 50))
# print(sqrt(n) / log2(n) - sqrt(n - 50) / log2(n - 50))
# print(log2(n) - log2(n - 50))
# print(n - (n - 50))
# print(log2(factorial(n)) - log2(factorial(n - 50)))
# print(n * log2(n) - (n - 50) * log2(n - 50))
# print(n ** 2 - (n - 50) ** 2)
# print(13 ** log2(n) - 13 ** log2(n - 50))
# print(n ** 535 - (n - 50) ** 535)
# print(2 ** n - 2 ** (n - 50))
# print(factorial(n) - factorial(n - 50))

""" Task 3 """
#
#
# def max_even_sum(numbers: list) -> int:
#     total_sum = sum(numbers)
#     if total_sum // 2 != total_sum / 2:
#         odd_nums = [num for num in numbers if num // 2 != num / 2]
#         total_sum -= min(odd_nums)
#     return total_sum
#
#
# def solution():
#     numbers = [int(x) for x in input().split()]
#     result = max_even_sum(numbers)
#     print(result)
#
#
# solution()

""" Task 4 """


def max_div3_sum(numbers: list) -> int:
    initial_sum = sum(numbers)
    if initial_sum // 3 == initial_sum / 3:
        return initial_sum
    else:
        num_sorted = sorted(numbers)
        for i in range(len(numbers)):
            total_sum = initial_sum - num_sorted[i]
            if total_sum // 3 == total_sum / 3:
                return total_sum
            else:
                for j in range(i):
                    if num_sorted[i] + num_sorted[j] < num_sorted[i + 1]:
                        total_sum -= num_sorted[j]
                        if total_sum // 3 == total_sum / 3:
                            return total_sum
                    else:
                        break
    return 0


def solution():
    numbers = [int(x) for x in input().split()]
    result = max_div3_sum(numbers)
    print(result)


solution()
