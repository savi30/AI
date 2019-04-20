from functools import wraps


def func_timer(orig_func):
    import time

    @wraps(orig_func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = orig_func(*args, **kwargs)
        end = time.time() - start
        print('{} ran in: {} sec'.format(orig_func.__name__, end))
        return result

    return wrapper
