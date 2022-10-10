def print_iterable(iterable):
    it = iter(iterable)
    while True:
        try:
            print(next(it), end=' ')
        except StopIteration:
            break


if __name__ == '__main__':
    print_iterable([1, 2, 3, 4])
