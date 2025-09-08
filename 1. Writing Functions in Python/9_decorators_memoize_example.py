import time

def memoize(func):
    """
    Store the result of the decorated func for fast lookup
    Args:
        func (callable): Func to be wrapped

    Returns:
        callable: Wrapped func
    """
    # Store the results in  a dict that maps arguments to results.
    cache = {}
    # Define the wrapper func to return.
    def wrapper(*args, **kwargs):
        # Define a hashable key for 'kwargs'.
        kwargs_key = tuple(sorted(kwargs.items()))
        # If these arguments have been used before
        if (args, kwargs_key) not in cache:
            # Call func() and store the result.
            cache[(args, kwargs_key)] = func(*args, **kwargs)
        return cache[(args, kwargs_key)]
    return wrapper

@memoize
def slow_funct(a, b):
    print('Sleeping ...')
    time.sleep(5)
    return a + b

print(slow_funct(3,4))
print(slow_funct(3,4))
print(slow_funct(5,3))