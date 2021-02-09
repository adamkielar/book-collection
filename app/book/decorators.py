import functools
from django.db import connection


def count_query(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if "GET" or "POST" in args[1].method:
            print(func.__name__)
            print(f"Total queries: {len(connection.queries)}")
        return result
    return wrapper
