"""Superset - subset of all subsets

If requires brute-force algo (полный перебор)
"""
"""-----------------------------------------"""
"""
(1, 2) => {}, {1}, {2}, {1, 2} => O(2 ** n)
"""
"""-----------------------------------------"""


def get_subsets(original_set: list):
    all_subsets = [[]]
    if not original_set:
        return [[]]

    for k, item in enumerate(original_set):
        all_subsets += [sublist + [item] for sublist in get_subsets(original_set[k + 1:])]

    return all_subsets


print(get_subsets([1, 2, 3, 4]))

# Complexity => T(n) = O(n * 2 ** n) (have 2 ** n subset, for each need n operations)
