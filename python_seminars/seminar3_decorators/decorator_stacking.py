def apply_transform(tag: str):
    def decorator(func):
        def wrapper(username):
            return '<{t}>{message}</{t}>'.format(t=tag, message=func(username))
            # return f'<{tag}>{func(username)}</{tag}>'
        return wrapper
    return decorator


# Transform executed from top to bottom
@apply_transform('p')
@apply_transform('strong')
def greet_upper(username):
    return f'Hi, {username}'


if __name__ == '__main__':
    print(greet_upper('Slava'))
