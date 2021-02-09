# def uppercase(func):
#     def wrapper():
#         origin = func()
#         modified = origin.upper()
#         return modified
#     return wrapper
#
# @uppercase
# def greet():
#     return 'hello adam!'
#
# print(greet())

import functools

def trace(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f'TRACE: calling {func.__name__}() '
            f'with {args}, {kwargs}')
        original_result = func(*args, **kwargs)
        print(f'TRACE: {func.__name__}() '
            f'returned {original_result!r}')
        return original_result
    return wrapper

@trace
def say(name, line):
    """This is sample docstring."""
    return f'{name}: {line}'

print(say('Adam', 'Kielar'))
print(say.__name__)
print(say.__doc__)