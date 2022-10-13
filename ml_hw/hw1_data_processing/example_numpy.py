""" Task 1 """
# import numpy as np
#
#
# def solution():
#     n, m, k = map(int, input().split())
#     lines = [input().split() for line in range(m)]
#
#     M = np.array([list(map(int, row)) for row in lines])
#
#     potential_sums = []
#
#     for j in range(k - n + 1):
#         for i in range(m - n + 1):
#             potential_sums.append(M[np.ix_(list(reversed([i + n - s for s in range(1, n + 1)])),
#                                            list(reversed([j + n - s for s in range(1, n + 1)])))].sum())
#
#     max_sum = max(potential_sums)
#
#     print(str(int(max_sum)))
#
#
# solution()

""" Task 2"""


import example_numpy as np


def solution():
    v = np.array(list(map(float, input().split())))
    n, t = input().split()
    n, t = int(n), float(t)

    us = np.array([input().split() for u in range(n)]).astype(float)

    indices = np.concatenate(np.argwhere(np.array([np.linalg.norm(v - u) for u in us]) <= t))

    print(' '.join(map(str, indices)))


solution()
