from functools import wraps
import time

def timer(func):
    """
    A decorator that prints how long a func took to run.
    Args:
        func (callable): The func being decorated.

    Returns:
        callable: The decorated func.
    """
    @wraps(func)    # With this decorator the wrapper func inherits the metadata of the parametric func
    def wrapper(*args, **kwargs):
        t_start = time.time()
        result = func(*args, **kwargs)
        t_total = time.time() - t_start
        print(f"Func '{func.__name__}' took a total of: ''{t_total}'' sec.")
        return result
    return wrapper

def sleep_n_seconds(n=10):
    """
    Pause processing for n seconds.
    Args:
        n (int): The number of seconds to pause for.

    Returns:
        None
    """
    time.sleep(n)

@timer
def sleep_n_seconds_2(n=10):
    """
        Pause processing for n seconds.
        Args:
            n (int): The number of seconds to pause for.

        Returns:
            None
        """
    time.sleep(n)

print(sleep_n_seconds.__doc__)
print(sleep_n_seconds.__name__)
print(sleep_n_seconds.__defaults__)
print()
"""
We'll observe metadata related to the original func is not passed to the wrapper func, so partially is lost, but if we 
add the decorator '@wraps'(line 13), the wrapper func inherits this metadata and is available again.
"""
print(sleep_n_seconds_2.__doc__)
print(sleep_n_seconds_2.__name__)
print(sleep_n_seconds_2.__defaults__)
print()

# We can also access the original func using the param __wrapped__
original_func = sleep_n_seconds_2.__wrapped__
print(original_func.__doc__)
print(original_func.__name__)
print(original_func.__defaults__)
print()