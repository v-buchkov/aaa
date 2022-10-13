# Алгоритм двух указателей
def merge_linear(a, b):

    i_a, i_b = 0, 0
    c = []

    while i_a < len(a) and i_b < len(b):
        if a[i_a] < b[i_b]:
            c.append(a[i_a])
            i_a += 1
        else:
            c.append(b[i_b])
            i_b += 1

    if i_a < len(a):
        # All elements to the end of the array
        c.extend(a[i_a:])
    else:
        c.extend(b[i_b:])

    return c
