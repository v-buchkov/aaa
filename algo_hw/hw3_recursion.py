"""Task 1"""
# def fib(n, n_2 = 0, n_1 = 1):
#     if n == 0:
#         return n_2
#     elif n == 1:
#         return n_1
#     else:
#         return fib(n - 1, n_1, n_1 + n_2)
#
#
# def solution():
#     n = int(input().strip())
#     c = fib(n + 1)
#     print(c)
#
#
# solution()


"""Task 2"""
def get_sums_subsets(original_set: list):
    all_sums = [0]
    if not original_set:
        return [0]

    for k, item in enumerate(original_set):
        all_sums += [s + item for s in get_sums_subsets(original_set[k + 1:])]

    return all_sums


# 6 - True, 8 - False
print(get_sums_subsets([1, 2, 3]))
