def oops_decorator(func):
    def wrapper():
        print('Oops')
        func()
        print('Oops again')
    return wrapper


@oops_decorator
def greet_upper():
    print('Hi, Slava')


if __name__ == '__main__':
    greet_upper()
