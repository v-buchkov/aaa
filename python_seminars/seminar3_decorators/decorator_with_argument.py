def apply_transform(transform):
    def decorator(func):
        def wrapper(username):
            return func(transform(username))
        return wrapper
    return decorator


@apply_transform(str.upper)
def greet_upper(username):
    return f'Hi, {username}'


@apply_transform(str.lower)
def greet_lower(username):
    return f'Hi, {username}'


if __name__ == '__main__':
    print(greet_upper('Slava'))
    print(greet_lower('Slava'))
